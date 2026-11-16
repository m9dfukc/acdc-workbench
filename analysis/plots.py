"""Abbildungen. Alle Funktionen schreiben eine PNG-Datei und geben den Pfad zurück."""

from __future__ import annotations

import math
import os
import tempfile
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", os.path.join(tempfile.gettempdir(), "mpl-acdc"))
import matplotlib  # noqa: E402

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
from matplotlib.gridspec import GridSpecFromSubplotSpec  # noqa: E402
from matplotlib.ticker import FixedLocator, FuncFormatter, NullLocator  # noqa: E402
from scipy.signal import spectrogram  # noqa: E402

from .spectra import pow_db, welch_spectrum_db  # noqa: E402

F_TICKS = [20, 50, 100, 200, 500, 1_000, 2_000, 5_000, 10_000, 20_000, 40_000]
FAMILY_COLORS = {"fs8": "tab:blue", "usb1k": "crimson", "led": "tab:green", "mains50": "tab:orange",
                 "imd": "tab:olive", "other1": "tab:purple", "other2": "tab:pink"}
DPI = 120


def hz_fmt(v, _pos=None):
    return f"{v / 1000:g}k" if v >= 1000 else f"{v:g}"


def fmt_hz(f):
    return f"{f:.2f} Hz" if f < 1000 else f"{f / 1000:.4f} kHz"


def fam_color(key):
    return FAMILY_COLORS.get(key, "0.3")


def style_log_f(ax, fmin, fmax, axis="y", labels=True):
    getattr(ax, f"set_{axis}scale")("log")
    getattr(ax, f"set_{axis}lim")(fmin, fmax)
    a = ax.yaxis if axis == "y" else ax.xaxis
    a.set_major_locator(FixedLocator([t for t in F_TICKS if fmin <= t <= fmax]))
    a.set_minor_locator(NullLocator())
    a.set_major_formatter(FuncFormatter(hz_fmt) if labels else FuncFormatter(lambda *_: ""))


def _label_peaks(ax, peaks, n=8):
    chosen = []
    for p in peaks:
        if all(abs(math.log10(p["freq"]) - math.log10(q["freq"])) > 0.065 for q in chosen):
            chosen.append(p)
        if len(chosen) >= n:
            break
    for p in chosen:
        key = (p.get("family") or "").split("·")[0]
        col = fam_color(key) if key else "0.2"
        ax.plot(p["level_db"], p["freq"], "o", ms=3.5, color=col, zorder=5)
        tag = f" [{p['family']}]" if p.get("family") else ""
        ax.annotate(f"{fmt_hz(p['freq'])}  {p['level_db']:.0f} dB{tag}", (p["level_db"], p["freq"]),
                    xytext=(4, 0), textcoords="offset points", fontsize=7, va="center", color=col,
                    bbox=dict(boxstyle="round,pad=0.1", fc="white", ec="none", alpha=0.75))


def spectrogram_grid(rec, results, out: Path, vmin=None, vmax=None):
    """Pro Kanal: Spektrogramm (log-f) + gemitteltes Spektrum mit markierten Linien."""
    fs, n_ch = rec.fs, rec.n_channels
    nperseg = 8192 if fs > 50_000 else 4096
    hop = max(nperseg // 8, math.ceil(rec.data.shape[0] / 1500))
    cols = 2 if n_ch > 1 else 1
    rows = math.ceil(n_ch / cols)
    note_h = 0.35 * (rec.meta.get("note", "").count("\n") + 1) + 0.6 if rec.meta.get("note") else 0.0
    height = 7.2 * rows + 2.5 + note_h
    fig = plt.figure(figsize=(12 * cols, height), dpi=DPI)
    outer = fig.add_gridspec(rows, cols, left=0.05, right=0.92, top=1 - 1.3 / height,
                             bottom=(1.2 + note_h) / height, hspace=0.3, wspace=0.13)
    fmax = fs / 2
    sig_like = max(r["rms_db"] for r in results) > -40
    vmin = vmin if vmin is not None else -140
    vmax = vmax if vmax is not None else (0 if sig_like else -60)
    mesh = None
    for c in range(n_ch):
        x, res = rec.data[:, c], results[c]
        f, t, s = spectrogram(x, fs, window="hann", nperseg=nperseg, noverlap=nperseg - hop,
                              scaling="spectrum", mode="psd")
        gs = GridSpecFromSubplotSpec(1, 2, subplot_spec=outer[c // cols, c % cols], width_ratios=[3.2, 1.4],
                                     wspace=0.04)
        ax_s, ax_p = fig.add_subplot(gs[0]), None
        ax_p = fig.add_subplot(gs[1], sharey=ax_s)
        mesh = ax_s.pcolormesh(t, f[1:], pow_db(2 * s[1:]), shading="auto", cmap="magma",
                               vmin=vmin, vmax=vmax, rasterized=True)
        style_log_f(ax_s, 20, fmax)
        ax_s.set_xlabel("Zeit [s]")
        ax_s.set_ylabel("Frequenz [Hz]")
        ax_s.set_title(f"{rec.labels[c]}  ·  DC {rec.dc[c] * 100:+.1f} % FS  ·  AC-RMS {res['rms_db']:.1f} dB  ·  "
                       f"Störanteil {res['lines_share'] * 100:.0f} %", fontsize=10.5, loc="left",
                       fontweight="bold")
        if fmax > 20_000:
            ax_s.axhline(20_000, color="white", lw=0.6, ls="--", alpha=0.6)
        fw, pw = welch_spectrum_db(x, fs, 32768)
        sel = (fw >= 20) & (fw <= fmax)
        ax_p.plot(pw[sel], fw[sel], lw=0.6, color="black")
        _label_peaks(ax_p, res["peaks"])
        ax_p.set_xlim(vmin - 12, vmax + 30)
        ax_p.set_xlabel("Pegel [dBFS] (Welch, gemittelt)")
        ax_p.tick_params(axis="y", labelleft=False)
        ax_p.grid(axis="x", alpha=0.3)
    cax = fig.add_axes([0.935, 0.25, 0.01, 0.55])
    cb = fig.colorbar(mesh, cax=cax)
    cb.set_label(f"Pegel pro Bin [dBFS, Sinus-Skala]  (Auflösung {fs / nperseg:.1f} Hz)")
    m = rec.meta
    fig.suptitle(m.get("title", rec.name), fontsize=17, fontweight="bold", x=0.05, ha="left")
    sub = " · ".join(str(v) for v in (m.get("device"), m.get("gain"), m.get("usb"), f"{fs} Hz",
                                       f"{rec.duration:.1f} s") if v)
    sub += " · Markierte Linien: präzise Frequenz aus Voll-FFT, [Familie·k] = Zuordnung"
    fig.text(0.05, 1 - 0.95 / height, sub, fontsize=9.5, color="0.3")
    if m.get("note"):
        fig.text(0.05, 0.012, m["note"], fontsize=10, va="bottom", ha="left", linespacing=1.5,
                 bbox=dict(boxstyle="round,pad=0.6", fc="#f4f4f0", ec="0.75"))
    out.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out)
    plt.close(fig)
    return out


def psd_plot(rec, results, out: Path, ref=None, ref_results=None, nperseg=65536):
    """Langzeit-Spektrum pro Kanal, log-f, Familien-Harmonische markiert, optional Referenz grau."""
    n_ch = rec.n_channels
    fig, axes = plt.subplots(n_ch, 1, figsize=(16, 3.4 * n_ch + 1), dpi=DPI, sharex=True, squeeze=False)
    fmax = rec.fs / 2
    for c in range(n_ch):
        ax = axes[c, 0]
        if ref is not None and c < ref.n_channels:
            fr, pr = welch_spectrum_db(ref.data[:, c], ref.fs, nperseg)
            ax.plot(fr[1:], pr[1:], lw=0.6, color="0.65", label=f"Referenz {ref.name}")
        fw, pw = welch_spectrum_db(rec.data[:, c], rec.fs, nperseg)
        ax.plot(fw[1:], pw[1:], lw=0.6, color="black", label=rec.name)
        top = np.percentile(pw[(fw > 20) & (fw < min(fmax, 20000))], 99.9) + 8
        for fam in results[c]["families"]:
            fr_ = [h["freq"] for h in fam["harmonics"]]
            ax.plot(fr_, [top] * len(fr_), "v", ms=5, color=fam_color(fam["key"]),
                    label=f"{fam['label']}: f0 = {fam['f0']:.4f} Hz, {fam['n']} Linien")
        style_log_f(ax, 10, fmax, axis="x")
        ax.set_ylabel("dBFS pro Bin")
        ax.set_title(f"{rec.labels[c]}  ·  Welch {nperseg} Punkte ({rec.fs / nperseg:.2f} Hz)", loc="left",
                     fontsize=10, fontweight="bold")
        ax.grid(alpha=0.25)
        ax.legend(fontsize=7.5, loc="lower left", ncol=2)
    axes[-1, 0].set_xlabel("Frequenz [Hz]")
    fig.suptitle(f"Langzeit-Spektrum – {rec.meta.get('title', rec.name)}", x=0.01, ha="left",
                 fontweight="bold")
    fig.tight_layout(rect=(0, 0, 1, 0.98))
    fig.savefig(out)
    plt.close(fig)
    return out


def comb_profile(rec, results, out: Path):
    """Pegel jeder Harmonischen k pro Familie, alle Kanäle."""
    keys = []
    for r in results:
        for fam in r["families"]:
            if fam["key"] not in keys and fam["key"] != "imd":
                keys.append(fam["key"])
    if not keys:
        return None
    fig, axes = plt.subplots(len(keys), 1, figsize=(14, 2.8 * len(keys) + 0.8), dpi=DPI, squeeze=False)
    markers = "osD^v<>p"
    for i, key in enumerate(keys):
        ax = axes[i, 0]
        label = key
        for c, r in enumerate(results):
            fam = next((f for f in r["families"] if f["key"] == key), None)
            if not fam:
                continue
            label = fam["label"]
            ks = [h["k"] + (c - 1.5) * 0.08 for h in fam["harmonics"]]
            ax.plot(ks, [h["level_db"] for h in fam["harmonics"]], markers[c % 8], ms=4, ls="-", lw=0.5,
                    label=f"{rec.labels[c]} (f0 {fam['f0']:.4f} Hz, Anteil {fam['share'] * 100:.1f} %)")
        ax.set_title(label, loc="left", fontsize=10, fontweight="bold", color=fam_color(key))
        ax.set_ylabel("dBFS")
        ax.grid(alpha=0.3)
        ax.legend(fontsize=7.5, ncol=2)
    axes[-1, 0].set_xlabel("Harmonische k")
    fig.tight_layout()
    fig.savefig(out)
    plt.close(fig)
    return out


def timeline(rec, stab, envs, click_res, out: Path):
    """f0-Abweichung (ppm) und Pegel je Familie über die Zeit, darunter HP-Hüllkurve mit Klicks."""
    keys = list(stab[0][0].keys()) if stab else []
    n_rows = len(keys) + 1
    fig, axes = plt.subplots(n_rows, 2, figsize=(16, 2.6 * n_rows + 0.8), dpi=DPI, squeeze=False)
    for i, key in enumerate(keys):
        for c, (series, _summ) in enumerate(stab):
            s = series.get(key)
            if not s:
                continue
            t, f0, lv = np.array(s["t"]), np.array(s["f0"]), np.array(s["rms_db"])
            ok = np.isfinite(f0)
            if ok.sum():
                axes[i, 0].plot(t[ok], (f0[ok] / np.mean(f0[ok]) - 1) * 1e6, ".-", lw=0.8, label=rec.labels[c])
            axes[i, 1].plot(t, lv, ".-", lw=0.8, label=rec.labels[c])
        axes[i, 0].set_ylabel(f"{key}\nf0-Abw. [ppm]", color=fam_color(key))
        axes[i, 1].set_ylabel("Pegel [dB RMS]")
        for a in axes[i]:
            a.grid(alpha=0.3)
    if keys:
        axes[0, 0].legend(fontsize=7, ncol=4)
        axes[0, 0].set_title("f0 relativ zum Mittelwert", loc="left", fontsize=10)
        axes[0, 1].set_title("Familienpegel (Summe der Harmonischen)", loc="left", fontsize=10)
    ax = axes[-1, 0]
    t, env = envs[0]
    step = max(1, len(env) // 20000)
    env_db = pow_db(env[::step] ** 2)
    ax.plot(t[::step], env_db, lw=0.4, color="0.3")
    core = env_db[env_db > -250]
    if len(core):
        ax.set_ylim(np.median(core) - 15, max(core.max(), pow_db(click_res[0]["threshold"] ** 2)) + 5)
    ax.axhline(pow_db(click_res[0]["threshold"] ** 2), color="crimson", lw=0.8, ls="--", label="Schwelle")
    for e in click_res[0]["events"]:
        ax.axvline(e["t"], color="crimson", lw=0.6, alpha=0.6)
    ax.set_title(f"{rec.labels[0]}: Hochpass-Hüllkurve ({click_res[0]['hp_hz']:.0f} Hz), "
                 f"{click_res[0]['n']} Klicks", loc="left", fontsize=10)
    ax.set_xlabel("Zeit [s]")
    ax.legend(fontsize=7)
    ax = axes[-1, 1]
    for c, cr in enumerate(click_res):
        ax.bar(c, cr["n"], color="crimson" if cr["n"] else "0.7")
    ax.set_xticks(range(len(click_res)), [lab for lab in rec.labels[: len(click_res)]])
    ax.set_ylabel("Klicks")
    ax.set_ylim(0, max(1, max(cr["n"] for cr in click_res)) * 1.2)
    fig.suptitle(f"Zeitverlauf – {rec.meta.get('title', rec.name)}", x=0.01, ha="left", fontweight="bold")
    fig.tight_layout(rect=(0, 0, 1, 0.975))
    fig.savefig(out)
    plt.close(fig)
    return out
