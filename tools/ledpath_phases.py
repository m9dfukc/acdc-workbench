"""Per-phase levels of a SchliereLedPath recording (owl/test/SchliereLedPathPatch.hpp) taken
at an interface input, referred to the AC/DC output (messlog D74, D91).

Phase 7 carries a 300 Hz tone with amplitude 0.001 (AC/DC full scale) on Out 1. Its onsets
fix the phase grid (10 phases x 5 s) and its level the calibration. Each phase is measured
from 1.0 to 4.5 s after its start, averaged in power over all cycles in the recording.
Columns: RMS >= 20 Hz, sine amplitude at 40 Hz (LED blink rate), strongest line near 1 kHz
(999.80-1000.01 Hz, the USB comb), 6000 and 12000 Hz, all in dB re AC/DC full scale.

Usage:
  UV_CACHE_DIR=.uv-cache uv run python tools/ledpath_phases.py recordings/<file>.wav [--channel 1]
"""
import argparse
import numpy as np
import soundfile as sf
from scipy.signal import butter, sosfiltfilt

ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
ap.add_argument("wav")
ap.add_argument("--channel", type=int, default=1, help="channel of the WAV, 1-based (default 1)")
args = ap.parse_args()
wav = args.wav
ch = args.channel - 1
x, sr = sf.read(wav)
x = x[:, ch] if x.ndim > 1 else x

# envelope of 300 Hz
sos = butter(4, [280, 320], btype="band", fs=sr, output="sos")
env = np.abs(sosfiltfilt(sos, x))
k = int(0.05 * sr)
env = np.convolve(env, np.ones(k) / k, mode="same")
thr = 0.5 * np.percentile(env, 99.5)
on = np.flatnonzero((env[1:] > thr) & (env[:-1] <= thr)) / sr
onsets = []
for t in on:
    if not onsets or t - onsets[-1] > 10:
        onsets.append(t)


def amp(seg, f):
    t = np.arange(len(seg)) / sr
    A = np.c_[np.sin(2 * np.pi * f * t), np.cos(2 * np.pi * f * t)]
    a = np.linalg.lstsq(A, seg - seg.mean(), rcond=None)[0]
    return float(np.hypot(*a))


def seg(t0, a=1.0, b=4.5):
    i0, i1 = int((t0 + a) * sr), int((t0 + b) * sr)
    if i0 < 0 or i1 > len(x):
        return None
    return x[i0:i1]


cal = []
for t7 in onsets:
    s = seg(t7)
    if s is not None:
        cal.append(amp(s, 300.0))
cal_amp = float(np.median(cal))
# 1 UMC full scale = 0.001 / cal_amp AC/DC full scale
g = 0.001 / cal_amp
print(f"{wav.split('/')[-1]} ch{ch+1}: tone onsets {[round(float(t), 3) for t in onsets]}, "
      f"tone {20*np.log10(cal_amp):.2f} dBFS UMC, 1 FS UMC = {g:.5f} FS AC/DC")

hp = butter(4, 20, btype="high", fs=sr, output="sos")
names = ["Schliere aus", "Schliere blink", "null aus", "null blink", "null aus",
         "null 4 rot", "null aus", "Eichton", "4xIn1 aus", "4xIn1 blink"]
lines = {"40": 40.0, "1k": None, "6k": 6000.0, "12k": 12000.0, "2k": 2000.0}
print("phase            RMS>=20Hz  40Hz    comb1k   6000    12000   (dB re AC/DC FS, output-referred)")
rows = {}
for p in range(10):
    vals = []
    for t7 in onsets:
        s = seg(t7 + (p - 7) * 5.0)
        if s is None:
            continue
        y = sosfiltfilt(hp, s)
        rms = np.sqrt(np.mean(y ** 2)) * g
        # comb f0 near 999.86: search fine
        best = max(amp(s, f) for f in np.arange(999.80, 1000.01, 0.01)) * g
        vals.append([rms, amp(s, 40.0) * g, best, amp(s, 6000.0) * g, amp(s, 12000.0) * g])
    if not vals:
        continue
    v = np.sqrt(np.mean(np.square(vals), axis=0))
    rows[names[p]] = 20 * np.log10(v)
    print(f"{p} {names[p]:<15}" + "".join(f"{d:8.1f}" for d in 20 * np.log10(v)))
