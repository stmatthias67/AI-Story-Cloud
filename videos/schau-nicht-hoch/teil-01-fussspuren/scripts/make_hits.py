#!/usr/bin/env python3
"""Erzeugt assets/hits.wav: deterministische Schritt- und Schlag-Töne für Teil 1.

Nur Standardbibliothek. Kein random-Modul, kein Datum, keine Netzwerkzugriffe.
Rauschen kommt aus einem LFSR mit festem Startwert 0xACE1 (16 Bit, Taps 16/14/13/11).
Ausgabe: 48 kHz, Stereo, 16 Bit, 30 s (wie assets/sfx.wav).
Jeder Schlag beginnt 33 ms nach seinem Bildstart, damit der Peak einen Frame später liegt (SPEC 7).

Aufruf:  python3 scripts/make_hits.py
"""
import math
import os
import struct
import wave

SR = 48000
DUR = 30.0
N = int(DUR * SR)
LATENCY = 0.033
SEED = 0xACE1

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "assets", "hits.wav")
BED = os.path.join(HERE, "..", "assets", "sfx-bed.wav")
# SPEC 7: Bett-Gain in der Mischung (index.html data-volume 0.45). Schläge werden auf das
# effektive Bett gepegelt: Peak jedes Schlags im Fenster [Einsatz, Einsatz+WINDOW] liegt TARGET_DB
# über dem Peak des Betts (mit BED_GAIN) im gleichen Fenster. Einsatz = Cue + LATENCY.
# 4.5 dB ist die Mitte von 3-6 dB. Messfenster 66 ms ab Einsatz: kürzer als der Abstand der
# Klicks (0.10 s), damit der nächste Schlag nicht mitzählt (ein 120-ms-Fenster überlappt die Klicks).
BED_GAIN = 0.45
TARGET_DB = 4.5
WINDOW = 0.066


class Lfsr:
    def __init__(self, seed):
        self.s = seed & 0xFFFF

    def next(self):
        s = self.s
        bit = ((s >> 0) ^ (s >> 2) ^ (s >> 3) ^ (s >> 5)) & 1
        self.s = ((s >> 1) | (bit << 15)) & 0xFFFF
        return self.s / 32768.0 - 1.0  # gleichverteilt in [-1, 1)


def db(g):
    return 10.0 ** (g / 20.0)


def decay(t, tau90):
    """Exponentieller Abfall, auf 1 % nach tau90 Sekunden."""
    return math.exp(-t * math.log(100.0) / tau90)


def load_bed_abs():
    """Absoluter Samplewert (max. beider Kanäle, 0..1) des unveränderten Betts."""
    with wave.open(BED, "rb") as w:
        assert w.getframerate() == SR and w.getnchannels() == 2 and w.getsampwidth() == 2
        assert w.getnframes() == N
        raw = w.readframes(N)
    vals = struct.unpack("<%dh" % (2 * N), raw)
    return [max(abs(vals[2 * i]), abs(vals[2 * i + 1])) / 32768.0 for i in range(N)]


class Bus:
    def __init__(self):
        self.buf = [0.0] * N
        self.rng = Lfsr(SEED)
        self.bed = load_bed_abs()
        self.cue = 0.0
        self.kind = ""
        self.report = []

    def add(self, t0, length, fn):
        i0 = int(round(t0 * SR))
        n = int(length * SR)
        local = [0.0] * n
        for k in range(n):
            if 0 <= i0 + k < N:
                local[k] = fn(k / SR)
        self.level(i0, local)

    def level(self, i0, local):
        # i0 ist der Einsatz des Schlags (Sample), local[0] liegt bei i0
        j0 = i0
        j1 = min(N, i0 + int(round(WINDOW * SR)))
        bed_peak = max(self.bed[j0:j1]) * BED_GAIN
        hit_peak = 0.0
        for k in range(0, j1 - j0):
            if k < len(local):
                hit_peak = max(hit_peak, abs(local[k]))
        if bed_peak <= 0.0 or hit_peak <= 0.0:
            raise ValueError("no level reference at cue %.2f" % self.cue)
        target = bed_peak * 10.0 ** (TARGET_DB / 20.0)
        g = target / hit_peak
        for k, v in enumerate(local):
            i = i0 + k
            if 0 <= i < N:
                self.buf[i] += g * v
        self.report.append((self.cue, self.kind, 20 * math.log10(bed_peak),
                            20 * math.log10(target), 20 * math.log10(g)))

    def hit(self, cue, kind):
        self.cue = cue
        self.kind = kind
        t0 = cue + LATENCY
        rng = self.rng

        # Bandpass-Rauschen als Differenz zweier Tiefpässe (1.5-4 kHz)
        lp_hi_state = [0.0]
        lp_lo_state = [0.0]
        a_hi = 1 - math.exp(-2 * math.pi * 4000 / SR)
        a_lo = 1 - math.exp(-2 * math.pi * 1500 / SR)

        def bandnoise(_):
            x = rng.next()
            lp_hi_state[0] += a_hi * (x - lp_hi_state[0])
            lp_lo_state[0] += a_lo * (x - lp_lo_state[0])
            return lp_hi_state[0] - lp_lo_state[0]

        if kind == "snow":  # 60 ms Burst, Abfall 0.08 s, -16 dB
            g = db(-16) * 2.6
            cache = {}

            def fn(t):
                e = 1.0 if t < 0.06 else decay(t - 0.06, 0.08)
                if t not in cache:
                    cache[t] = bandnoise(t)
                return g * e * cache[t]
            self.add(t0, 0.16, fn)

        elif kind in ("step", "floor"):  # 40 ms Rauschen + 110 Hz Sinus, -10 / -13 dB
            g = db(-10 if kind == "step" else -13)

            def fn(t):
                noise = rng.next() * decay(t, 0.04) * 0.6
                tone = math.sin(2 * math.pi * 110 * t) * decay(t, 0.12)
                return g * (noise + tone)
            self.add(t0, 0.20, fn)

        elif kind == "door":  # 70 Hz Sinus 0.30 s + 0.04 s Rauschen, -6 dB, schwer
            g = db(-6)

            def fn(t):
                tone = math.sin(2 * math.pi * 70 * t) * decay(t, 0.30)
                noise = rng.next() * decay(t, 0.04) * 0.5
                return g * (tone + noise)
            self.add(t0, 0.40, fn)

        elif kind in ("click", "snap"):  # 25 ms Rauschen + 1800 Hz, Schloss
            g = db(-12 if kind == "click" else -8)

            def fn(t):
                noise = rng.next() * decay(t, 0.025)
                tone = math.sin(2 * math.pi * 1800 * t) * decay(t, 0.02)
                extra = 0.0
                if kind == "snap":
                    extra = math.sin(2 * math.pi * 900 * t) * decay(t, 0.06) * db(-6)
                return g * (noise * 0.8 + tone * 0.6 + extra)
            self.add(t0, 0.12, fn)

        elif kind == "crack":  # 250 ms Breitband, 10 ms Anstieg, Abfall 0.20 s, -3 dB
            g = db(-3)

            def fn(t):
                env = t / 0.01 if t < 0.01 else decay(t - 0.01, 0.20)
                return g * 0.7 * rng.next() * min(1.0, env)
            self.add(t0, 0.25, fn)

        elif kind == "rumble":  # 45 Hz Sinus, 0.80 s, -6 dB
            g = db(-6)

            def fn(t):
                return g * math.sin(2 * math.pi * 45 * t) * decay(t, 0.80)
            self.add(t0, 1.0, fn)

        elif kind == "ceiling":  # 70 Hz 0.35 s + 0.03 s Rauschen, -4 dB
            g = db(-4)

            def fn(t):
                tone = math.sin(2 * math.pi * 70 * t) * decay(t, 0.35)
                noise = rng.next() * decay(t, 0.03) * 0.5
                return g * (tone + noise)
            self.add(t0, 0.45, fn)

        else:
            raise ValueError(kind)


def cues():
    c = []
    # Schnee: zehn Schritte in den Schnee (SPEC 7)
    for k in range(10):
        c.append((round(6.40 + 0.42 * k, 2), "snow"))
    # Treppe: acht Stufen auf Treppenfeld 1-8, Bodenkontakt wie im Bild (SPEC 4.3, 7): 10.74 + 0.19 k
    for k in range(8):
        c.append((round(10.74 + 0.19 * k, 2), "step"))
    # Boden: drei leichtere Schritte, dann Tür
    for t in (12.26, 12.42, 12.58):
        c.append((t, "floor"))
    c.append((12.90, "door"))
    # Schloss rattert: sieben Klicks
    for t in (13.70, 13.80, 13.90, 14.00, 14.10, 14.20, 14.30):
        c.append((t, "click"))
    c.append((15.50, "snap"))
    c.append((16.95, "crack"))
    c.append((17.10, "rumble"))
    # Decke: sechs Stöße
    for t in (20.62, 20.90, 21.18, 21.46, 21.74, 22.02):
        c.append((t, "ceiling"))
    return c


def main():
    bus = Bus()
    for t, kind in cues():
        bus.hit(t, kind)
    for cue, kind, bed_db, tgt_db, gain_db in bus.report:
        print("%6.2f %-8s bed_eff %6.2f dBFS  hit_target %6.2f dBFS  gain %6.2f dB" % (cue, kind, bed_db, tgt_db, gain_db))
    peak = max(abs(x) for x in bus.buf)
    limit = db(-1)  # True-Peak-Grenze -1 dBFS (Sample-Peak als Näherung)
    scale = min(1.0, limit / peak) if peak > 0 else 1.0
    frames = bytearray()
    for x in bus.buf:
        v = int(round(max(-1.0, min(1.0, x * scale)) * 32767))
        frames += struct.pack("<hh", v, v)
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with wave.open(OUT, "wb") as w:
        w.setnchannels(2)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes(bytes(frames))
    print("wrote", os.path.normpath(OUT), "peak %.3f scale %.3f" % (peak, scale))


if __name__ == "__main__":
    main()
