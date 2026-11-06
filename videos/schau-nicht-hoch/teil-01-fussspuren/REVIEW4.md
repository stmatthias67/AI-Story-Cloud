# REVIEW4: Teil 1 „Fußspuren im Schnee“ (Checker, round 4)

**Verdict: NOT READY. 6 FAIL items.**

Scope: read-only. No project file was edited, nothing committed, pushed or rendered. Report written only.

Sources: `hyperframes@0.9.17 check --json` (saved to `/tmp/hf/check4.json`), `snapshot` at the 21 requested times (`/tmp/hf/check4-snaps/`, contact sheets 1–3 and frames), close crops of frames 11.5 s (stairs), 16.5 s (check mark), 22.5 s (ceiling prints) and 0.5 s (title) in `/tmp/hf/crops4/`, a numpy analysis of `assets/sfx-bed.wav` and `assets/hits.wav` (48 kHz, 30 s), ffmpeg volumedetect, and code reading of `index.html`, `compositions/*.html`, `scripts/make_hits.py`.

---

## 0. Tooling evidence

| Check | Result |
|---|---|
| `check --json` | `ok: true`. errors **0**, warnings **0**. lint 0, runtime 0, motion 0, contrast 0, craft 0, audio 0. Layout: 5 info `container_overflow` (`#s1-flk`, `#s2-cam`, `#s3-hof` svg g, `#s4-flur` svg g, `#s5-cam`). Info only, not warnings. |
| Snapshots | 21 frames written (all 21 requested times) plus 3 contact sheets. |
| volumedetect | `sfx-bed.wav` max −16.8 dB, mean −34.4 dB. `hits.wav` max −19.8 dB, mean −52.3 dB. |
| Banned patterns | No `Math.random`, `Date`, `fetch`, `https`, gradients, or `✓` glyph in `compositions/*.html`, `index.html`, or `assets/figure.js`. `make_hits.py` imports only `math, os, struct, wave`, uses LFSR seed `0xACE1`. GSAP local. Three fonts bundled as woff2. |
| Scene timing (`index.html`) | s1 0–2, s2 2.00–6.80 (zoom to 6.80), s3 6.30–10.60, s4 10.60–13.60, s5 13.60–16.70, s6 16.70–19.10, s7 19.10–25.50, s8 25.50–30.00. Matches SPEC §0.2. |
| Labels (`labels.html`) | Draußen 0, Schlafzimmer 2.00, Hof 6.30, Haustür 10.60, Schloss 13.60, Treppenhaus 16.70, Decke 19.10, Umfrage 25.50. Matches §0.2. |

---

## 1. Builder's REVIEW3 items 1–7

| Item | Builder status | Checker verdict | Evidence |
|---|---|---|---|
| 1 Title typography (F4, A5) | fixed | **PASS** (with documented deviation) | `s1-titel.html`: 150 px at top 720, blur 4 px → 0, stagger 0.10, dur 0.13, start opacity 0.3. Moon (830,300) r70 #dfe8f5. Six houses at the §1 widths and x. 18 snowflakes. The `y` tween on `#s1-t2` is removed. Title is on one line at 0.5, 1.0 and 1.9 s. Letter-spacing −0.06em is the documented deviation, not a failure. The title spans nearly the full width (about 25 px left, 18 px right margin at 1080 px). Crop of 0.5 s confirms the one-line layout. |
| 2 End card motion (F2, A1) | fixed | **PASS** | `s8-abspann.html` tweens are opacity and blur only. No `x`, `y` or `scale`. Stick figure removed. Frames 26, 27.5, 29 and 29.75 s show the poll static. |
| 3 Stairs S3 start 10.60 (F3, A3/A4) | fixed | **PASS** | `s3-hof` 6.30 + 4.30 = 10.60. `s4-flur` starts 10.60. Dip darkening 10.50–10.60 at opacity 0.4 (60 % brightness), hard cut at 10.60. Label Haustür switches at 10.60. Stair-run sync is a separate FAIL (see §4, item F-S3). |
| 4 Pendant amplitude (F5, A6) | fixed | **PASS** | `s7-decke.html` `#s7-pend`: peaks 4.00, −5.17, 6.09, −6.83, 7.41, −7.87 at 20.62, 20.90, 21.18, 21.46, 21.74, 22.02. Matches the decaying sequence in REVIEW3 F5. |
| 5 Ceiling print rotation (F6, A7) | decision recorded | **PASS** (per SPEC Änderungen) | SPEC `## Änderungen` (Fix-Runde 4) records the decision: `rotate(180)` kept, colour raised to `#dfe8f5`. Crop of 22.5 s shows six prints, light grey on dark, legible. |
| 6 Snowflake counts (F7, A11) | partly fixed | **FAIL** | See §3. S0, S1, S2, S5, S6 have 18 (PASS). S3 (`s4-flur`) has 0 (needs 18). S7 (`s8-abspann`) has 23 (needs 6). |
| 7 Sound re-level (checklist 19) | partly fixed | **FAIL** | Silence, cue times and bed fade are correct. The hit-to-bed margin still fails 3–6 dB (see §4, item F-S1). |

Builder claimed items 1–7 fixed, item 7 partly fixed. Checker confirms 1–5 fixed, 6 and 7 still open.

---

## 2. BRIEF.md quality criteria 1–8

| # | Criterion | Verdict | Evidence |
|---|---|---|---|
| B1 | 0–2 s title only, no narration | **PASS** | Frames 0.5, 1.0, 1.9 s show only FUSSSPUREN, IM SCHNEE, HUD, moon, snow, houses, and the watermark. Title is on one line. First caption `cap-01` starts 2.02. |
| B2 | Footprints on snow, spread gate to door, never on glass, pointing at door | **PASS** | Frames 6.45, 7, 8.5, 10.55 s: 10 prints on the yard snow, growing toward the viewer, none on the glass or wall. |
| B3 | Stairs ≥ 12 steps, banister, landing | **PASS** | S5 `s6-treppenhaus`: 13 treads (`#1a2232` rects), rails, landing, sign „2. OG“ (frames 17.5, 18.5 s). Note: the S3 hall stair has 9 treads by SPEC §4, which is a separate item. |
| B4 | ≥ 8 identifiable objects per scene | **PASS** | Every scene in the frames has at least 8 identifiable objects (see SPEC §11 item 4 below). |
| B5 | HUD constant, location label changes per scene | **PASS** | HUD in every frame. Labels verified by code and frames (Draußen, Schlafzimmer, Hof, Haustür, Schloss, Treppenhaus, Decke, Umfrage). |
| B6 | Captions in sync ±0.15 s, never two groups at once | **PASS** | `captions.html` group times within ±0.15 s of the BRIEF segments. Gap checks between consecutive groups show no overlap (e.g. cap-02a ends 3.95, cap-02b starts 4.00). Single-group frames confirmed in contact sheets. |
| B7 | `check --json` clean | **PASS** | errors 0, warnings 0. Five layout info items only. |
| B8 | End card: poll visible, each text ≥ 2 s | **PASS** | Question from 25.50 (visible 26.0), red button 26.10, green 26.30, hint 26.80, folge tag 27.60 to 30.00 (2.4 s). All texts legible at 26, 27.5, 29 and 29.75 s. Layout deviations are separate, see F-S7. |

BRIEF result: **8 PASS, 0 FAIL.**

---

## 3. Snowflakes per scene (SPEC §0.3 and §10.1)

§0.3: 18 snowflakes in all scenes except S4 (Schloss, `s5-schloss`). §10.1 for S7: six snowflakes, i = 0…5. §10.1 is the more specific rule, so S7 is held to six.

| Scene | File | Count now | Required | Verdict |
|---|---|---|---|---|
| S0 Titel | `s1-titel.html` (`#s1-flk`) | 18 | 18 | PASS (formula checked for i=0 and i=17) |
| S1 Schlafzimmer | `s2-schlafzimmer.html` (`#s2-flk`) | 18 | 18 | PASS |
| S2 Hof | `s3-hof.html` (`#s3-flk`) | 18 | 18 | PASS |
| S3 Haustür | `s4-flur.html` | **0** | 18 | **FAIL** (F-S2) |
| S4 Schloss | `s5-schloss.html` | 0 | none | PASS |
| S5 Treppenhaus | `s6-treppenhaus.html` (`#s6-flk`) | 18 | 18 | PASS |
| S6 Decke | `s7-decke.html` (`#s7-flk`) | 18 | 18 | PASS |
| S7 Abspann | `s8-abspann.html` (`.s8-flk`) | **23** | 6 | **FAIL** (F-S7) |

The user's note said s4-flur has none. That is correct as observed, but §0.3 does not exempt S3, so it is a FAIL. Only s5-schloss (S4) is exempt.

---

## 4. FAIL items

### F-S1. 6.40–22.02 s, `hits.wav` and SPEC §7 / checklist 19: FAIL

SPEC §7: "Every hit is 3–6 dB above the bed at its time." Measured margin (hit peak in the 120 ms after onset, against `sfx-bed.wav` × 0.45 in the same window, both in dBFS):

| Cue (s) | Margin (dB) | In 3–6 dB? |
|---|---|---|
| 6.40 | 6.5 | no (over) |
| 8.08 | 1.0 | no |
| 10.18 | 2.4 | no |
| 13.90 | 6.4 | no (over) |
| 20.62 | 2.4 | no |
| 20.90 | 2.0 | no |
| 21.18 | 1.8 | no |
| 21.46 | 2.3 | no |
| 22.02 | 1.7 | no |

The other 29 cues fall between 3.4 and 6.2 dB. Onsets all sit +33 ms after the cue (matches the one-frame rule). Silence checks pass: `hits.wav` silent 18.45–19.60 and after 25.90, `sfx-bed.wav` silent 18.50–19.55 (−240 dBFS), fade-in begins at 19.60 (−28.5 dBFS), and the bed fades 25.40 → 25.90 (−17 → −39 dBFS, then silent).

Method note: peak-to-peak in a 120 ms window, not RMS. A different window or RMS measure may move individual values by about 1 to 2 dB. The nine failing cues are clearly outside the window, so the verdict holds.

**Fix:** in `scripts/make_hits.py`, scale each hit so its peak sits at the effective bed peak plus 4.5 dB at its onset (the bed × 0.45 peak in the same window). Concretely, for cues 6.40, 13.90 lower the hit by about 2 dB; for 8.08, 10.18, 20.62, 20.90, 21.18, 21.46, 22.02 raise by about 2 to 3.5 dB. Re-run the script, then re-measure the nine cues and the silence windows. Alternatively amend §7 to name a different reference. Either way, record it in SPEC `## Änderungen`.

Checklist 19 is FAIL because of this item. Its other parts (bed silence, hit times, determinism) pass.

### F-S2. 10.60–13.60 s, `s4-flur.html` (S3 Haustür), SPEC §0.3: FAIL

No snowflake group. §0.3 requires 18 in every scene except S4.

**Fix:** add `<g id="s4-flk">` with i = 0…17, `x = (i*397+61)%1080`, `y = (i*613+97)%1920`, `r = 2+(i%3)`, `fill="#dfe8f5" opacity="0.85"`, and add `tl.to("#s4-flk", { y: 220, duration: 3.0, ease: "none" }, 0);`. The formula values are the same ones used in `s1-titel.html`.

### F-S3. 10.55–12.26 s, `s4-flur.html` stair run versus §4.3 / §7 cue table: FAIL

§7 puts stair steps at 10.55 + 0.19j (j = 0…8, last 12.07). Code derived from the tweens: the first step tween starts at relative −0.05 (abs 10.55, before the scene starts at 10.60) and each tween lands 0.19 s after it starts. Landings are therefore at 10.74 + 0.19k (k = 0…8, last 12.26). The tweens run to line 84 and the pattern continues; the last landing was not read past line 84 and is inferred from the pattern. Result: the picture lags the sound by one step (0.19 s) for every stair, and the first step's motion begins before the scene starts.

This is the same conflict REVIEW3 flagged: §4.3 places the first landing at 10.55, which is before the scene's 10.60 start.

**Fix (choose one):** (a) keep the picture and move the eight-stair hits to 10.74 + 0.19k, k = 0…8, in `make_hits.py` and in the §7 cue table, leaving the floor and door cues unchanged; or (b) start the stair tweens at 10.60 with step spacing 0.19 and cue the first hit at 10.60. Either way, amend SPEC §4.3 and §7 in `## Änderungen`. Confirm by frame at 10.8 and 11.0 s after the change.

### F-S4. 1.40–4.30 s, `s2-schlafzimmer.html` figure near arm, SPEC §2.2: FAIL (numeric)

§2.2 beats: near arm upper arm 0° → +70°, forearm 0° → −35°, expo.out, 3.40–4.20. Code: `#s2-fig-uaR` → −53°, `#s2-fig-faR` → 0° (line 25–26, at rel 1.40, 0.8 s). The hand does reach the lower edge of the glass at 4.3 s (checklist 11 PASS visually), so the mismatch is in the numbers, not the outcome.

**Fix:** set `#s2-fig-uaR` to +70 and `#s2-fig-faR` to −35, then re-snapshot 4.3 s and confirm the hand still touches the glass lower edge (`(460, 960)`). If it does not, amend §2.2 with the measured angles and note the change in `## Änderungen`.

### F-S7. 25.50–30.00 s, `s8-abspann.html`, SPEC §10.1 snowflakes and layout: FAIL

Two parts.

**(a) Snowflakes:** 23 `.s8-flk` circles at positions and colours that do not follow §0.3 / §10.1. Colour `#eef4ff` at opacity 0.24–0.40, not `#dfe8f5` at 0.85. Required: six, i = 0…5 (§10.1 items 10–15), r 2–4. **Fix:** delete the 17 extra circles and set the remaining six to (61,97) r2, (458,710) r3, (855,1323) r4, (172,16) r2, (569,629) r3, (966,1242) r4, fill `#dfe8f5` opacity 0.85. Keep `y: 220` over 4.5 s. (If the intent is 18 for S7, §10.1 must be amended instead.)

**(b) End-card layout versus §10.1:**

| Element | Spec (§10.1) | Code | Fix |
|---|---|---|---|
| question | top 600 (line 1 y 600–720) | top 560 | set top 600 |
| red button | 130,920 820×150 | 130,880 | set top 920 |
| green button | 130,1110 820×150 | 130,1070 | set top 1110 |
| hint | left 60, y 1300–1340, Inter 900 40 px | top 1270 | set top 1300 |
| folge tag | 140,1440 700×84, Inter 900 44 px | left 230, top 1400, width 400, 38 px | set left 140, top 1440, width 700, height 84, 44 px |
| door-frame left/right | 0,0 36×1920 and 1044,0 36×1920, #161a24 | missing | add both rects |

The code also has a zig-zag polygon at the bottom (`#111824`) and a background of `#0a0d16` instead of `#0d0f16`. Neither is in §10.1. Either remove them or amend §10.1.

Motion, timing and text content of the end card pass (see BRIEF B8).

---

## 5. SPEC checklist (§11, items 1–22)

| # | Item | Verdict | Evidence / note |
|---|---|---|---|
| 1 | 0–2 s title only; C1 at 2.00 | **PASS** | Frames 0.5, 1.0, 1.9 s. `cap-01` starts 2.02 (BRIEF narration start, within tolerance). |
| 2 | 10 prints on snow, gate to door, toward door, growing | **PASS** | `s3-hof.html` has `#s3-p0`…`#s3-p9`. Frame 10.55 s shows the full trail. |
| 3 | S5 13 treads; S3 9 treads plus floor | **PASS** | S5 13 `#1a2232` treads (code count). S3 9 treads in crop of 11.5 s (j = 0…8). |
| 4 | ≥ 8 objects per scene | **PASS** | S0 9 (sky, moon, six houses, ground, two titles, flakes); S1 ≥ 8 (bed, window, curtain, figure, houses, lamp, cars, fence, sill); S2 ≥ 8 (cars, snow patches, fence, lamp, windows, prints); S3 ≥ 8 (door, stairs, pane, escutcheon, lamp, figure, stairs rail); S4 ≥ 8 (plate, knob, bolt, jamb, badge, figure, rivets); S5 ≥ 8 (stairs, walls, sign, landing, lamp, crack, figure); S6 ≥ 8 (beams, pendant, prints, figure, wall corner); S7 ≥ 8 (buttons, question, hint, tag, figure-free but bg, watermark). |
| 5 | HUD on every frame; label per scene | **PASS** | HUD in all 21 frames. Labels per §0.2 (see §0 above). |
| 6 | Captions per §5.1: 2–4 words; C11/C16 one word | **PASS** | Split groups `cap-02a/b`, `cap-04a/b`, `cap-05a/b`, `cap-14a/b` present. Max 4 words per group. `cap-08` „Verriegelt.“ and `cap-13` „Schritte.“ are one word each. |
| 7 | `check --json` clean | **PASS** | errors 0, warnings 0 (see §0). |
| 8 | End card: question, two buttons, hint, folge tag; ≥ 2 s each | **PASS** (content and timing) | See F-S7(b) for layout. |
| 9 | All on-screen text German | **PASS** | HUD, labels, captions, sign „2. OG“, badge, poll, folge tag. |
| 10 | Figure motion by rotated limbs; stair run 9 treads at 0.19 s | **PASS** (cadence) | Limb rigs in S1, S3, S5, S6. Cadence is 0.19 s. Sync is F-S3. |
| 11 | S1 arm raised to glass 3.40–5.20, hand on glass | **PASS** (visual) | Frame 4.3 s: hand on glass lower edge. Angles differ, see F-S4. |
| 12 | S2 prints one by one at §3.2 times | **PASS** | `s3-hof.html` p0…p9 at rel 0.10, 0.52, 0.94 … 3.88 (abs 6.40 … 10.18, step 0.42). Scale 0.6 → 1.0 and opacity entrance. Print widths W not re-measured. |
| 13 | S3 stair run, door, escutcheon, knob, rattle 13.70–14.30 | **PASS** | Frame 13.2 s shows door, escutcheon, knob, figure. Rattle at 13.70–14.30 is in `s5-schloss` (see REVIEW3 wording note). |
| 14 | S4 deadbolt 15.20–15.45, snap at 15.50 | **PASS** | `s5-schloss.html` bolt tween at rel 1.60 (15.20), dur 0.25. Snap at rel 1.90 (15.50). Hit at 15.533 (+33 ms). |
| 15 | S5 crack 16.95, flash 16.95–17.30, shake table, flinch | **PASS** | Crack draw at rel 0.25 (16.95), flash 0.55 → 0 over 0.35 s. Shake keyframes match §8 table. Flinch 16.95–17.05. Frame 17.5 s shows crack. |
| 16 | S6 prints 20.62…22.02, red pulses, thumps, pendant swing, figure holds from 22.02 | **PASS** | Six prints at rel 1.52…2.92 (abs 20.62…22.02). Red pulses at same times. Pendant per F5. Figure torso holds from 22.02. Ceiling print orientation per SPEC Änderungen. |
| 17 | Light and colour: flat fills, no glow, no gradients | **PASS** | No gradients. Only glow is the required S6 red inset pulse (§9.4). |
| 18 | Captions scrim rgba(7,11,20,0.55), one yellow keyword per group | **PASS** | Scrim visible in frames 3.5, 4.3, 7.7, 8.5, 10.55, 11.5, 14.5, 15.2, 20.6, 22.5, 24.5. Each group has one `.k` span. |
| 19 | Sound: bed edited, hits deterministic, cues per §7, bed silent after 25.90 | **FAIL** | Silence, determinism, cue times and bed fade pass. Hit-to-bed margin fails (F-S1). |
| 20 | No Math.random, Date, fetch, CDN; GSAP local; fonts bundled | **PASS** | Grep clean in compositions, index and `assets/figure.js`. GSAP from `assets/gsap.min.js`. Three fonts in `assets/fonts/`. |
| 21 | ✓ drawn as SVG polyline | **PASS** | No ✓ glyph anywhere. Crop of 16.5 s shows the full tick. |
| 22 | Handle stays `@deinhandle` | **PASS** | Watermark in every frame. |

SPEC checklist result: **19 PASS (incl. notes), 1 FAIL (item 19), 0 NOT VERIFIED from items 1–22 as written.** Item 19 is FAIL. Items 8, 10, 11 and 12 pass on the checklist wording but have linked FAILs (F-S7(b), F-S3, F-S4) that the checklist wording does not cover.

---

## 6. Binding-text deviations (SPEC body)

| Item | Status | Note |
|---|---|---|
| Title letter-spacing −0.06em | **Deviation, not a failure** | Title stays on one line at 0.5, 1.0, 1.9 s. |
| ceiling prints rot 180°, colour `#dfe8f5` | **Documented deviation** | SPEC `## Änderungen` (F6). Accepted. |
| S3 dip cut 10.50–10.60 | PASS | See item 3 in §1. |
| S0 title timing and houses | PASS | See item 1 in §1. |

---

## 7. NOT VERIFIED

| Item | Why |
|---|---|
| Voice loudness (−16 LUFS integrated, true peak ≤ −1 dBTP for the mix) | Needs a render (`npx hyperframes audio <mp4> --json`). Not run (no render, per instructions). |
| Voice identity "Vincent Crowe" | Cannot be checked from the WAV. |
| Stair-run stick-figure anchor coordinates (§4.3 feet at 1040 → 760 and tread-by-tread y) | Anchor values in code (`#s3-fig-pos` start 1040, 304.62) differ from the §4.3 feet formula; not reconciled. Visual check at 10.7 s and 11.5 s is consistent with the stairs. |
| Print widths W in §3.2 and §9.2 | Not re-measured; counts and times pass. |
| Ceiling print frame 21.0 s red pulse | Not captured this round. |

---

## 8. Summary

- **FAIL items: 6.** F-S1 (checklist 19, hit-to-bed margin, 9 cues outside 3–6 dB), F-S2 (S3 snowflakes 0 vs 18), F-S3 (stair-run sync, one-step lag), F-S4 (S1 arm angles vs §2.2), F-S7(a) (end-card snowflakes 23 vs 6), F-S7(b) (end-card layout coordinates and folge tag size, plus missing door frames).
- BRIEF criteria: **8 PASS, 0 FAIL.**
- SPEC checklist: **19 PASS, 1 FAIL (item 19), 0 NOT VERIFIED from items 1–22.**
- Check: 0 errors, 0 warnings, 5 info.
- Audio: bed silent 18.50–19.55 and after 25.90. Hits silent 18.45–19.60 and after 25.90. Hits at §7 times (+33 ms). Hit-to-bed margin 1.0–6.5 dB, nine cues outside 3–6 dB.
- Builder's REVIEW3 items 1–5 confirmed fixed. Items 6 (snowflakes) and 7 (sound) still open.

**Recommendation:** NOT READY. Fix F-S1 (re-level hits, then re-measure), F-S2 (add 18 flakes to `s4-flur`), F-S3 (align stair sound or picture, then amend §4.3 / §7), F-S4 (arm angles), F-S7 (remove extra flakes, fix end-card coordinates and folge size). Then re-run `check --json`, the snapshot set, and the volumedetect checks. Do not render until the checks pass.
