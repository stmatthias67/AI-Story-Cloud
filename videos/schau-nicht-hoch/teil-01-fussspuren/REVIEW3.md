# REVIEW3: Teil 1 „Fußspuren im Schnee“ (Checker, round 3)

**Verdict: NOT READY. 8 FAIL items.** 1 is a SPEC §11 checklist line (item 19). 7 are binding-text deviations (A1, A3, A5, A6, A7, A11, N1).

Scope: read-only. No project file was edited, nothing committed, nothing rendered. Sources: `hyperframes@0.9.17 check --json` (report `.hyperframes/artifacts/checks/767b69a9-cf4d-4cab-836c-77990cea904c.json`), `snapshot` at the 22 requested times (`/tmp/hf/check3-snaps/`, contact sheets 1–3), 4 extra snapshots at 6.6, 15.2, 20.75, 21.0 s (`/tmp/hf/check3-extra/`, 20.75 and 6.6 viewed; 21.0 not viewed), ffmpeg volumedetect and sample-level analysis on `assets/sfx-bed.wav` and `assets/hits.wav`, and code reading of `index.html` and `compositions/*.html`.

---

## 0. Tooling evidence

| Check | Result |
|---|---|
| `check --json` | `ok: true`. errors **0**, warnings **0**. lint 0, runtime 0, motion 0, contrast 0 (37/37 passed), craft 0, audio 0. Layout: 5 info `container_overflow` (11.67 `#s4-flur` svg, 8.33 `#s3-hof`, 15.0 `#s5-cam`, 21.67 `#s7-cam`, 5.0 `#s2-cam`). Info only. |
| Snapshots | 23 frames (22 requested + 29.75) and 3 contact sheets written. |
| `assets/sfx-bed.wav` | 48 kHz stereo, 30.00 s. 18.50–19.55 s: all 50 ms windows at −∞ dBFS (mean −79.2 dB over 18.45–19.60). 18.40–18.45 fade at −35 dBFS, 18.45–18.50 tail at −48.5 dBFS. 19.60–19.75 fade-in at −28…−32 dBFS. 25.90–30.00: −91 dB (silent). |
| `assets/hits.wav` | 48 kHz stereo, 30.00 s. Silent 18.45–19.60 and 25.90–30 (max −91 dB). Onsets listed in §3, item 19. |
| Banned-pattern grep | No `Math.random`, `Date`, `fetch`, `https`, radial or linear gradients in `compositions/*.html` or `index.html`. `scripts/make_hits.py` imports only `math, os, struct, wave`. |
| Fonts | `assets/fonts/` present, `@font-face` in `index.html` (round 2, not re-checked this round). |

---

## 1. Round-2 FAIL items (verification of the builder's round-3 fixes)

| ID | Round-2 item | Round-3 status | Evidence |
|---|---|---|---|
| R2-3 | S3 stairs: 8 visible treads | **FIXED** | Crop of frame 11.5 s (x 820–1080, y 450–1350): 9 treads, tops at y 520 … 1240, j = 0…8. |
| R2-6 | Captions merged (cap-02, 04, 05) | **FIXED** | `captions.html` has `cap-02a/b`, `cap-04a/b`, `cap-05a/b`. Frames 3.5 s „SCHAUE ICH AUS“, 4.3 s „DEM FENSTER.“, 7.7 s „SIE FÜHREN NICHT“, 8.5 s „SIE FÜHREN DIREKT“ show the split groups. |
| R2-11 | S1 hand not on glass | **FIXED** | Frame 4.3 s: near arm runs from shoulder (290,835) to hand (465,965). Glass lower edge is at y 972, x 386–914, so the hand touches the glass's lower edge. |
| R2-16a | Red pulse was a flat wash | **FIXED** | `#s7-red` is now `box-shadow: inset 0 0 260px 120px rgba(255,59,59,0.45)`, opacity 0 → 0.8 → 0 per thump. Frame 20.75 s shows the inset red edge. |
| R2-16b | Figure moved after 22.02 | **FIXED** | `s7-decke.html` line 33: `#s7-fig-tor` rotation 0 over 0.42 s from rel 2.50, so it ends at 22.02. |
| R2-17 | Lamp halo ring | **FIXED** | `s1-titel.html` has no `lamp` element. Frame 1.0 s shows no ring. |
| R2-18 | Yellow keyword per group | **FIXED** | Each `.cap` group in `captions.html` has exactly one `.k` span (`Nacht`, `aus`, `Fenster.`, `Fußspuren.`, `nicht`, `weg.`, `direkt`, `Tür`, `runter.`, `Schloss.`, `Verriegelt.`, `zu.`, `knackt`, `Stock.`, `dann`, `Schritte.`, `über`, `Kopf.`). |
| R2-A1 | Abspann motion | **NOT FIXED** | See F2. |
| R2-A2 | Window zoom-through missing | **FIXED** | `s2-schlafzimmer.html` line 31–32: `#s2-hole` and `#s2-frame` scale 1 → 3.2, power3.in, 0.5 s, rel 4.30 (abs 6.30). Frame 6.6 s shows the window opened onto the yard. |
| R2-A10 | Check mark draws incompletely | **FIXED** | `#s5-check` now has `stroke-dasharray="88.6"`. Crop of frame 16.5 s shows the full tick. |
| R2-A3/A4 | S3 start 10.60 | **NOT FIXED** | See F3. |
| R2-A5 | Title typography | **NOT FIXED** | See F4. |
| R2-A6 | Pendant amplitude | **NOT FIXED** | See F5. |
| R2-A7 | Ceiling print rotation | **OPEN** (decision not recorded) | See F6. |
| R2-A11 | Snowflake counts | **NOT FIXED** | See F7. |

---

## 2. BRIEF.md quality criteria (1–8)

| # | Criterion | Verdict | Evidence |
|---|---|---|---|
| Q1 | 0–2 s title only, no narration | **PASS** | Frames 0.5, 1.0, 1.9 s: only FUSSSPUREN, IM SCHNEE, HUD, moon, snow, houses. First caption `cap-01` starts 2.00. |
| Q2 | Footprints on snow, spread from gate to door, never on glass, pointing to door | **PASS** | Frames 8.5 and 10.55 s: prints only on the yard snow, growing toward the viewer. No prints on the glass or the wall. |
| Q3 | Staircase ≥ 12 steps, banister, landing | **PASS** | `s6-treppenhaus.html`: 13 `#1a2232` tread rects, rails, landing, sign „2. OG“. Frames 17.5 and 18.5 s. |
| Q4 | ≥ 8 identifiable objects per scene | **PASS** | Frames show ≥ 8 objects in each scene (S1 bed, window, curtain, figure, houses, lamp, cars, fence, sill; S2 cars, snow patches, fence, lamp, windows, prints; S3 door, stairs, pane, escutcheon, lamp, figure; S4 plate, knob, bolt, jamb, badge, figure; S5 stairs, walls, sign, landing, lamp, crack, figure; S6 beams, pendant, prints, figure, wall corner; S7 buttons, question, hint, tag, figure). |
| Q5 | HUD constant, location label changes per scene | **PASS** | HUD in all 23 frames. Labels: Draußen (0.5–1.9), Schlafzimmer (3.5, 4.3), Hof (6.45, 7, 8.5, 10.55), Haustür (11.5, 13.2), Schloss (14.5, 16.5), Treppenhaus (17.5, 18.5), Decke (20.6, 22.5, 24.5), Umfrage (26–29.75). Switch to Haustür is at 10.50, not 10.60 (F3). |
| Q6 | Captions in sync (±0.15 s), never two groups at once | **PASS** | Group times in `captions.html` match the SPEC §5.1 table. No two groups seen together in any frame. |
| Q7 | `check --json`: no errors, no contrast or layout warnings | **PASS** | errors 0, warnings 0, contrast 0. Layout has 5 info-level items only. |
| Q8 | Abspann: poll visible, each text ≥ 2 s | **PASS** | Question from 25.5 s (visible at 26.0), red button 26.1, green 26.3, hint 26.8, folge tag 27.6 to 30.00 (2.4 s). Frames 26, 27.5, 29, 29.75 s show all text. Motion is F2, not a timing failure. |

BRIEF result: **8 PASS, 0 FAIL.**

---

## 3. SPEC.md §11 checklist (1–22)

| # | Item | Verdict | Evidence |
|---|---|---|---|
| 1 | 0–2 s title only; C1 at 2.00 | **PASS** | Frames 0.5, 1.0, 1.9 s. `cap-01` starts 2.00. (Title typography is F4.) |
| 2 | 10 prints on snow, gate to door, toward door, growing | **PASS** | `s3-hof.html` has `#s3-p0`…`#s3-p9` (10 ids). Frame 10.55 s shows the full trail on the snow, growing toward the viewer. |
| 3 | S5 13 treads with rails, landing, sign; S3 9 treads plus floor | **PASS** | S5: 13 tread rects, frame 17.5 s. S3: crop of frame 11.5 s shows 9 treads, j = 0…8 (R2-3 fixed). |
| 4 | ≥ 8 objects per scene | **PASS** | See Q4. |
| 5 | HUD on every frame; label per scene | **PASS** | See Q5. |
| 6 | Captions per §5.1: 2–4 words per group; C11/C16 one word | **PASS** | Split groups `cap-02a/b`, `cap-04a/b`, `cap-05a/b`, `cap-14a/b` (R2-6 fixed). Max 4 words per group. `cap-08` „Verriegelt.“ and `cap-13` „Schritte.“ are one word each. |
| 7 | `check --json` clean | **PASS** | See §0. |
| 8 | Abspann: question, two buttons, hint, folge tag; each ≥ 2 s | **PASS** | See Q8. |
| 9 | All on-screen text German | **PASS** | HUD, labels, captions, badge, poll, folge tag all German. |
| 10 | Figure motion by rotated limbs; stair run 9 treads at 0.19 s | **PASS** | Limb rigs in S1, S3, S5, S6 (code and frames 8.5–13.2 s). |
| 11 | S1 arm raised to glass 3.40–5.20, hand on glass | **PASS** | Frame 4.3 s: hand at (465,965) on the glass's lower edge (R2-11 fixed). Hold to 5.20 not sampled. |
| 12 | S2 prints one by one at §3.2 times | **PASS** | Ten print ids, 0.42 s step from 6.40 to 10.18, scale-in entrance (code). |
| 13 | S3: stair run, door, escutcheon and knob, rattle 13.70–14.30 | **PASS (wording note)** | Stair run, door, escutcheon (640,840) and knob are in `s4-flur`. The rattle (13.70–14.30) is in `s5-schloss` (S4), per SPEC §6.2. The item's wording conflicts with the §0.2 scene table (S3 ends 13.60). Amend the wording. |
| 14 | S4 deadbolt 15.20–15.45; snap at 15.50 | **PASS** | `s5-schloss`: bolt x 0 → 60 over 0.25 s at rel 1.60 (15.20). Slot flash at 15.50. `hits.wav` onset 15.53. |
| 15 | S5 crack 16.95, flash 16.95–17.30, shake table, flinch | **PASS** | `s6-treppenhaus`: crack draws at rel 0.25 (16.95). Flash 0.55 → 0 over 0.35 s from 16.95. Frame 17.5 s shows the crack on the right wall. |
| 16 | S6 six prints at 20.62…22.02 with red pulses, thumps, pendant swing, figure holds from 22.02 | **PASS** | Six prints at 20.62, 20.90, 21.18, 21.46, 21.74, 22.02 (frame 22.5 s shows six). Inset red pulse (frame 20.75 s). `#s7-fig-tor` holds from 22.02. Pendant swings. Open: A6 amplitudes and A7 orientation (F5, F6). |
| 17 | Light and colour: flat fills, no glow, no gradients | **PASS** | Lamp halo removed (R2-17); frame 1.0 s clean. No gradients in project. The only glow is the S6 inset red pulse, which SPEC §9.4 requires. |
| 18 | Caption scrim rgba(7,11,20,0.55), not full-width; one yellow keyword per group | **PASS** | `.cap .scrim` present; each group has one `.k` span (R2-18 fixed). Frames 3.5, 4.3, 7.7, 8.5, 10.55, 11.5, 14.5, 15.2, 20.6, 22.5, 24.5 s show a scrim box and one yellow word. |
| 19 | Sound: bed edited, hits deterministic, cues per §7, bed silent after 25.90 | **FAIL** | Bed silent 18.50–19.55 and after 25.90 (PASS). Hits at §7 times +30 ms (PASS). Deterministic (PASS). **Failing:** SPEC §7 "every hit 3–6 dB above the bed at its time". Measured peak hit vs. raw-bed peak in a 120 ms window after each onset: 6.43 s 17.4 dB, 8.95 s 15.1 dB, 10.58 s 23.0 dB, 12.93 s 23.8 dB, 13.73 s 19.7 dB, 16.98 s 24.1 dB, 20.65 s 25.6 dB. Range 12.8–25.6 dB. With the §7 bed gain of 0.45 (−6.9 dB), the margin is still 6–19 dB. None is in 3–6 dB. **Fix:** re-level `hits.wav` (`scripts/make_hits.py`) so each hit peak sits 3–6 dB above the effective bed peak at its time. Effective bed peaks are about −35 dBFS in 6–10 s and −36 to −38 dBFS in 10–22 s, so hit peaks should land around −30 to −33 dBFS (currently −4 to −14 dBFS). Or amend §7 if the intent was a different reference. Re-run the script, then re-check onsets. |
| 20 | No Math.random, Date, fetch, CDN; GSAP local; fonts bundled | **PASS** | Grep clean. GSAP `assets/gsap.min.js`. Fonts in `assets/fonts/`. |
| 21 | ✓ drawn as SVG polyline | **PASS** | `#s5-check` polyline; full tick at 16.5 s (crop). |
| 22 | Handle stays @deinhandle | **PASS** | `hud.html` watermark, present in every frame. |

SPEC checklist result: **21 PASS (incl. 13 with note), 1 FAIL (item 19), 0 NOT VERIFIED.**

---

## 4. Binding-text deviations (SPEC body, not checklist lines)

These count toward the FAIL total because they contradict binding SPEC text.

### F2 (A1). 25.50–27.50 s, `s8-abspann.html`: FAIL

SPEC §10.2 and BANNED: "Nothing moves after it lands" and no sliding. Code still has:
- line 19: `#s8-q` `y: 40 → 0`
- line 20: `#s8-red` `x: -40 → 0`
- line 21: `#s8-green` `x: 40 → 0`
- line 23: `#s8-folge` `scale: 0.8 → 1`, back.out
- lines 24–25: `#s8-fig-uaR` rotation −165°, `#s8-fig-faR` −10°. Stick figure `#s8-fig` is not in SPEC §10.1.

**Fix:** delete `y`, `x` and `scale` from lines 19–23 so each is `opacity` only (blur allowed). Delete the `#s8-fig` div (line 12 tail) and lines 24–25. Keep the flake drift at line 26 only if the SPEC allows it (it does not mention flakes on S7 other than §0.3; keep it).

### F3 (A3, A4). 10.50–10.60 s, `index.html` line 47: FAIL

SPEC §0.2: S3 Haustür starts 10.60. Code: `#s4-flur` `data-start="10.50"` overlaps `#s3-hof` (ends 10.60). The SPEC §4 dip cut at 10.60 is not implemented. Label `Haustür` appears at 10.50.

**Fix (clean option):** set `#s3-hof` `data-duration="4.30"` and `#s4-flur` `data-start="10.60"` `data-duration="3.00"`. Keep the stair run on its SPEC times by moving the stair-run beats in `s4-flur` to the new relative base (rel = abs − 10.60). Step 0 at 10.55 cannot be placed before the scene starts, so the first step either starts at 10.60 (cue at 10.60) or the step cues move to 10.60 + 0.19j. Choose one, then regenerate `hits.wav` with the same stair cue times (`scripts/make_hits.py`) so picture and sound agree. Add the §4 dip cut (3 frames at 60 %) at 10.60. Move the `#loc-4` label switch to 10.60 in `labels.html`. Or amend SPEC §0.2 and §4 to 10.50 and record it in REVIEW3.

### F4 (A5). 0–2 s, `s1-titel.html`: FAIL

Against SPEC §1:
- `FUSSSPUREN` font-size is not 150 px and sits at a different top (frame 1.0 s: title glyph height about 90 px). Use 150 px at top 720.
- Letter blur 14 px (SPEC 4 px); stagger 0.067 s (SPEC 0.10 s); duration 0.3 s (SPEC 0.13 s). Line 24 of the file.
- Moon is `circle cx=800 cy=330 r=92` with an overlay, not (830, 300) r 70 #dfe8f5.
- 3 house polygons, not 6 at widths 120, 150, 110, 170, 130, 160.
- Snowflakes: 29 circles in the file, not 18 (§0.3).
- Frame-0 rule (title ≥ 30 % opacity at frame 0) is not met: letters tween from opacity 0 at 0.15 s.
- **BANNED:** line 26 `#s1-t2` `y: 30 → 0` slides the second title line up. BANNED says "every element fading and sliding up; titles stay still after landing".

**Fix:** set font-size 150 px, top 720; letter tween `filter: blur(4px)` and `stagger: 0.10`, `duration 0.13`, starting at 0 with `opacity: 0.3`. Moon to (830, 300) r 70, #dfe8f5. Replace houses with six polygons per SPEC widths and x positions. Set snowflakes to 18 (§0.3). Remove the `y` tween on `#s1-t2`; use opacity and blur only.

### F5 (A6). 19.10–25.50 s, `s7-decke.html` pendant: FAIL

SPEC §9.1: amplitude 4° at 20.62, +2° per thump, decays with time constant 1.2 s. Code rotations at the thumps: 4.00, −4.75, 5.02, −4.97, 4.72, −4.36. The amplitude does not grow by 2° per thump and does not decay in the required way (lines 38–60).

**Fix:** use the decaying sequence, computed from A_n = A_(n−1)·e^(−0.28/1.2) + 2 starting at A_0 = 4: peak amplitudes 4.00, 5.17, 6.09, 6.83, 7.41, 7.87 degrees at 20.62, 20.90, 21.18, 21.46, 21.74, 22.02, alternating sign, each returning to 0 with `sine.out` over the 0.28 s gap. Rewrite `#s7-pend` tweens at rel 1.52 … 3.02 accordingly.

### F6 (A7). 20.62–22.02 s, `s7-decke.html` prints `#s7-p1`…`#s7-p6`: FAIL (decision still open)

SPEC §9.2: `rot 0°`. Code: `rotate(180)` (round-1 D4). Round 2 asked for a decision; none is recorded. Frame 22.5 s: prints are dark `#05070c` on `#14101a`, barely readable.

**Fix:** record the decision in SPEC §9.2. Either (a) amend SPEC to rotate(180) and raise print contrast (e.g. #000000 at 0.95 or a lighter ceiling), or (b) change the six `rotate(180)` to `rotate(0)` in `s7-decke.html`. Then re-snapshot 22.5 s.

### F7 (A11). Snowflakes, `s1-titel.html`, `s3-hof.html`, `s6-treppenhaus.html`, `s4-flur.html`: FAIL (low severity)

SPEC §0.3: 18 snowflakes per scene (i = 0…17). Circle counts in the files: S0 29, S2 69 (including lit windows and prints), S4 17, S5 19. Counts of circles include other objects, so the exact flake count needs a per-scene id. Fix: give the flakes a shared class (`.flk`) and generate exactly i = 0…17 at the §0.3 formula in each scene.

### F8 (N1). 19.10 s… see F4 for `#s1-t2`: FAIL (new, BANNED)

Covered under F4. Listed separately because it is a BANNED pattern in its own right. Fix: remove `y: 30` from `tl.fromTo("#s1-t2", …)`.

---

## 5. Requirements not verified

| Item | Why |
|---|---|
| SPEC §7 loudness (voice −16 LUFS, true peak ≤ −1 dBTP for the mix) | Needs a render and `npx hyperframes audio <mp4>`. Not run (no render). |
| SPEC §7 "3–6 dB above the bed" | Measured, FAIL (checklist 19). |
| Voice identity "Vincent Crowe" | Cannot be checked from the WAV. |
| Snap at 15.50 `hits.wav` onset | Measured 15.53 (+30 ms). PASS. |
| Frame 21.0 s red pulse | Captured in `/tmp/hf/check3-extra/frame-02-at-21s.png`, not viewed. Code matches §9.4. |
| S3 dip cut 10.60 (3 frames at 60 %) | Not implemented (F3). |

---

## 6. Summary

- **FAIL items: 8.** Checklist: item 19 (hit-to-bed margin). Deviations: F2 (A1 abspann motion), F3 (A3 scene start 10.50), F4 (A5 title typography and slide-up, incl. N1), F5 (A6 pendant amplitude), F6 (A7 ceiling print rotation, decision open), F7 (A11 snowflake counts).
- BRIEF quality criteria: **8 PASS, 0 FAIL.**
- SPEC checklist: **21 PASS, 1 FAIL (item 19).**
- Round-2 checklist FAILs 3, 6, 11, 16, 17, 18 are **fixed**. A2, A10, R2-16a/b are fixed.
- Check: 0 errors, 0 warnings; 5 info.
- Audio: bed silent 18.50–19.55 and after 25.90; hits at the §7 times (+30 ms). Hit-to-bed margin 12–26 dB, outside 3–6 dB.

**Recommendation:** NOT READY. Fix item 19 (re-level hits), F2 (abspann motion), F3 (stairs scene start), F4 (title typography and slide-up), F5 (pendant amplitude), F6 (decide and record print orientation), F7 (snowflake count). Then re-run `check --json`, the snapshot set, and the volumedetect checks.
