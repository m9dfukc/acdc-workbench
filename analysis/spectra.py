"""Spektren, Peak-Interpolation, Rauschboden.

Pegelkonventionen (überall gleich):
- Linienpegel in dBFS als **Sinus-Amplitude**: Vollaussteuerungs-Sinus = 0 dBFS.
- RMS-Pegel als 20·log10(RMS): Gleichspannung bei Vollaussteuerung = 0 dB, Vollaussteuerungs-Sinus = −3,0 dB.
"""

from __future__ import annotations

import numpy as np
from scipy import signal


def to_db(a, floor=1e-12):
    return 20 * np.log10(np.maximum(a, floor))


def pow_db(p, floor=1e-30):
    return 10 * np.log10(np.maximum(p, floor))


def refine(f, a_db, i):
    """Parabolische Interpolation auf dem dB-Spektrum um Bin i → (Frequenz, Pegel).

    Mit Hann-Fenster liegt der Frequenzfehler weit unter einem Zehntel Bin.
    """
    if i <= 0 or i >= len(a_db) - 1:
        return float(f[i]), float(a_db[i])
    a, b, c = a_db[i - 1], a_db[i], a_db[i + 1]
    den = a - 2 * b + c
    p = 0.0 if den == 0 else float(np.clip(0.5 * (a - c) / den, -0.5, 0.5))
    return float(f[i] + p * (f[1] - f[0])), float(b - 0.25 * (a - c) * p)


def floor_curve(a_db, df, block_hz=10.0):
    """Lokaler Rauschboden: Median des dB-Spektrums in Blöcken von block_hz, interpoliert.

    Schmale Linien belegen nur wenige Bins und verschieben den Median kaum.
    """
    b = max(5, int(round(block_hz / df)))
    n = len(a_db) // b * b
    med = np.median(a_db[:n].reshape(-1, b), axis=1)
    centers = np.arange(len(med)) * b + b / 2
    return np.interp(np.arange(len(a_db)), centers, med)


class Spectrum:
    """Hann-FFT über das ganze Signal plus Werkzeuge zur Liniensuche."""

    def __init__(self, x, fs):
        w = signal.windows.hann(len(x), sym=False)
        amp = np.abs(np.fft.rfft(x * w)) * 2.0 / w.sum()
        self.fs = fs
        self.f = np.fft.rfftfreq(len(x), 1.0 / fs)
        self.df = float(self.f[1])
        self.db = to_db(amp)
        self.floor = floor_curve(self.db, self.df)
        self.claimed = np.zeros(len(self.f), bool)

    def idx(self, freq):
        return int(round(freq / self.df))

    def search(self, center, tol, allow_claimed=False, min_snr=None, closest=False):
        """Lokales Maximum in center ± tol → dict oder None.

        closest=False: das stärkste. closest=True: das der Vorhersage nächste mit snr ≥ min_snr
        (wichtig in dichten Spektren, wo eine stärkere Nachbarlinie im Fenster liegt).
        """
        lo = max(1, self.idx(center - tol))
        hi = min(len(self.f) - 2, self.idx(center + tol))
        if hi < lo:
            return None
        cand = [i for i in range(lo, hi + 1)
                if self.db[i] >= self.db[i - 1] and self.db[i] >= self.db[i + 1]
                and (allow_claimed or not self.claimed[i])]
        if min_snr is not None:
            cand = [i for i in cand if self.db[i] - self.floor[i] >= min_snr]
        if not cand:
            return None
        if closest:
            i = min(cand, key=lambda j: abs(self.f[j] - center))
        else:
            i = max(cand, key=lambda j: self.db[j])
        freq, level = refine(self.f, self.db, i)
        return {"bin": i, "freq": freq, "level_db": level, "snr_db": level - float(self.floor[i])}

    def claim(self, i, half=2):
        self.claimed[max(0, i - half) : i + half + 1] = True


def welch_spectrum_db(x, fs, nperseg):
    """Welch, skaliert auf Sinus-Amplitude (dBFS pro Bin), für Darstellung."""
    nperseg = min(nperseg, len(x))
    f, p = signal.welch(x, fs, window="hann", nperseg=nperseg, scaling="spectrum")
    return f, pow_db(2 * p)


def welch_density(x, fs, nperseg=65536):
    nperseg = min(nperseg, len(x))
    return signal.welch(x, fs, window="hann", nperseg=nperseg, scaling="density")


def band_ms(f, psd, lo, hi):
    """Mittleres Quadrat (Leistung) im Band [lo, hi) aus einer Dichte."""
    sel = (f >= lo) & (f < hi)
    return float(np.trapezoid(psd[sel], f[sel])) if sel.sum() > 1 else 0.0


def a_weighting(f):
    """A-Bewertung (IEC 61672), linearer Betrag, 1 kHz = 1."""
    f2 = np.asarray(f, float) ** 2
    ra = (12194.0**2 * f2**2) / (
        (f2 + 20.6**2) * np.sqrt((f2 + 107.7**2) * (f2 + 737.9**2)) * (f2 + 12194.0**2)
    )
    return ra * 10 ** (2.0 / 20)
