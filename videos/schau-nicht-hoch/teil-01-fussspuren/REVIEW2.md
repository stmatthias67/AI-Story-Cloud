# REVIEW2: Teil 1 „Fußspuren im Schnee“ (Checker, round 2)

**Verdict: NOT READY. 6 FAIL items** (all in SPEC §11 checklist; BRIEF quality criteria 1–8 have 0 FAIL).

Scope: read-only check. No project file was edited, nothing committed, nothing rendered. Written from `hyperframes@0.9.17 check --json`, `snapshot` at the 20 requested times (`/tmp/hf/check2-snaps/`, 21 frames incl. 29.75 s, plus contact sheets 1–3), ffmpeg/Python on the audio, and code reading of `index.html`, `captions.html`, `hud.html`, `labels.html`, `s1`–`s8` compositions and `assets/figure.js`.

---

## 0. Tooling evidence

| Check | Result |
|---|---|
| `check --json` | `ok: true`, errors **0**, warnings **0** (lint 0, runtime 0, contrast 0, motion 0, craft 0, audio 0). Layout: 0 warnings, 5 info `container_overflow` (5.0 s `#s2-cam`, 8.33 s `#s3-hof`, 11.67 s `#s4-flur`, 15.0 s `#s5-cam`, 21.67 s `#s7-cam`). Info only. Round 1 had 12 warnings. Now 0. |
| `snapshot` | 21 frames + 3 contact sheets written to `/tmp/hf/check2-snaps/`. |
| Audio `assets/sfx-bed.wav` | 48 kHz stereo, 30.00 s. 18.45–19.60 s: mean −79 dB; residual max −48.5 dBFS only in 18.45–18.90 (fade tail). 25.90–30 s: −91 dB (silent). 2–6 s: mean −38.9 dB vs original −42.4 dB, i.e. +3.5 dB = file gain 1.5 × `data-volume` 1 = effective 0.45 as SPEC §7 requires. |
| Audio `assets/hits.wav` | 48 kHz stereo, 30.00 s. Silent 0–6 s, 18.45–19.60 s, 25.90–30 s. True peak −1.8 dBTP. 39 onsets detected: snow 6.43…10.21 (10), stair 10.58…12.45 (9), floor 12.29/12.45/12.61 (3), door 12.93 (1), lock click 13.73…14.33 (7), deadbolt 15.53 (1), crack 16.98 (1), rumble 17.13 (1), ceiling 20.65…22.05 (6). Every onset is +30 ms against SPEC §7, one frame, which matches the SPEC rule "peaks one frame later (33 ms)". |
| Banned-pattern grep | No `Math.random`, `Date`, `fetch`, `https://`, Google Fonts, `radial` gradients, U+2713 glyph. `scripts/make_hits.py` imports only `math, os, struct, wave`; LFSR seed 0xACE1. |
| Fonts | `assets/fonts/` has Archivo Black 400 and Inter 700/900 (woff2), with `@font-face` in `index.html`. |

---

## 1. Round-1 defects D1–D17 (independent verification)

| ID | Round-1 defect | Round-2 status | Evidence |
|---|---|---|---|
| D1 | Bed not edited | **FIXED** | `sfx-bed.wav` silent 18.45–19.60, silent after 25.90; `#sfx` uses `sfx-bed.wav`, `data-volume="1"`. |
| D2 | `hits.wav` missing | **FIXED** | File exists; 39 onsets match SPEC §7 cue list (+1 frame); `#hits` audio tag present. |
| D3 | No figure in S5/S6 | **FIXED** | `s6-treppenhaus.html` figure at (540,1480), feet (540,1690). `s7-decke.html` figure at (200,1555.6), feet (200,1760). Both visible in frames 17.5, 18.5, 20.6, 22.0. |
| D4 | Ceiling prints count/timing/orientation | **PARTLY FIXED** | Six prints at 20.62…22.02 with correct W and centres. Orientation is `rotate(180)` (toes down), not SPEC §9.2 `rot 0°`. See A7. |
| D5 | Footprints on wall, 12 prints | **FIXED** | Ten prints `#s3-p0`…`#s3-p9` at §3.2 centres and W, times 6.40…10.18 (0.42 s step), 174°/186° alternation. Frame 8.5 s and 10 s: prints only on the snow. |
| D6 | S1 figure does not reach window | **NOT FIXED** | Scale is now H 520 with feet at (300,1300), but the arm pose is wrong. Frame 4.3 s: hand ends near (500,850), not at the glass lower edge (460,960). See item 11. |
| D7 | Figure body size | **FIXED** | Limb lengths match SPEC §0.4 at H 520. |
| D8 | Fonts not bundled | **FIXED** | See §0. |
| D9 | ✓ glyph | **FIXED (glyph removed), NEW DEFECT (draw)** | Polyline replaces the glyph. But `stroke-dasharray=40` on an 88.6 px path hides the second stroke. Frame 16.5 s shows a short "V" fragment, not a full check. See A10. |
| D10 | Lock beats wrong | **FIXED** | Bolt +60 px at 15.20–15.45 (`s5-schloss.html` `tl.to("#s5-bolt",{x:60})` at rel 1.60); knob id `s5-knob`, rattle 13.70–14.28 at 6 Hz; camera push removed; escutcheon rect at 640,840 in `s3`. Snap sound at 15.53 (+1 frame). |
| D11 | Crack/flash/shake | **FIXED** | Crack on right wall at 16.95 (`s6-crack`, 0.12 s draw); flash 0.55→0 over 16.95–17.30; shake table at 0.05 s steps; flinch at 16.95–17.05 (torso +8, power4.out). |
| D12 | Captions: scrim, slide, merged C17/C18 | **PARTLY FIXED** | Scrim `rgba(7,11,20,0.55)` present; `y` slide removed; C17/C18 split (`cap-14a`/`cap-14b`). New problems: merged groups cap-02, cap-04, cap-05 (item 6) and keywords (item 18). |
| D13 | Radial gradients / glow | **PARTLY FIXED** | No radial gradients remain. A new halo circle `#s1-lamp` (r 70, opacity 0.35) is in `s1-titel.html`. See item 17. |
| D14 | HUD labels | **FIXED** | Labels in `labels.html`: Draußen, Schlafzimmer, Hof, Haustür, Schloss, Treppenhaus, Decke, Umfrage. |
| D15 | Check warnings 12 | **FIXED** | 0 warnings; compositions split into `hud.html`, `labels.html`, `captions.html`. |
| D16 | S3 stairs 8 treads, not 9 | **NOT FIXED** | Still 8 visible treads. Tread j=0 is zero width (`x=1080`, `width 0.00`). See item 3. |
| D17 | Folge tag timing 26.5 s | **FIXED** | `#s8-folge` starts at rel 2.1 (27.6 s). |

---

## 2. BRIEF.md quality criteria (1–8)

| # | Criterion | Verdict | Evidence |
|---|---|---|---|
| Q1 | 0–2 s title card only, no narration | **PASS** | Frames 0.5, 1.0, 1.9 s: only FUSSSPUREN / IM SCHNEE / HUD. First caption `cap-01` starts 2.00 (fade from 2.02). |
| Q2 | Footprints on snow, spread gate to door, never on glass, pointing to door | **PASS** | Frame 8.5 s and 10 s: prints on the yard snow, toes toward the door, growing toward the viewer. None on the window or the wall. |
| Q3 | Staircase ≥12 steps, banister, landing | **PASS** | `s6-treppenhaus`: 13 treads (tops 977.8…1533.3), two rails, landing, sign "2. OG". Frames 17.5 and 18.5 s. |
| Q4 | ≥8 identifiable objects per scene | **PASS** | Code and frames: S0 ≥9, S1 18, S2 12+10 prints, S3 ≥12, S4 ≥8, S5 22, S6 11, S7 ≥10. |
| Q5 | HUD constant; location label changes per scene | **PASS** | HUD present in all 21 frames. Label changes at 2.00, 6.30, 10.50, 13.60, 16.70, 19.10, 25.50 (SPEC asks 10.60; see A4). |
| Q6 | Captions in sync (±0.15 s), never two groups at once | **PASS** | Start/end times match BRIEF anchors within ±0.07 s. No overlaps. (Group-size problems are under SPEC item 6.) |
| Q7 | `check --json`: no errors, no contrast or layout warnings | **PASS** | errors 0, warnings 0, contrast 0. Layout has 5 info-level `container_overflow` only. |
| Q8 | Abspann: poll visible, each text ≥2 s | **PASS** | Question from 25.60, red button 26.0, green 26.2, hint 26.5, folge tag 27.6 to 30.00 (2.4 s). Frame 27.5, 29, 29.75 s show all text. (Motion problem is A1, not a timing problem.) |

BRIEF result: **8 PASS, 0 FAIL.**

---

## 3. SPEC.md §11 checklist (1–22)

| # | Item | Verdict | Evidence / note |
|---|---|---|---|
| 1 | 0–2 s title only; first caption at 2.00 | **PASS** | As Q1. |
| 2 | 10 prints §3.2, on snow, gate to door, toward door, growing | **PASS** | `s3-hof.html` `#s3-p0`…`#s3-p9`. Centres and W match the table. Times 6.40 + 0.42k. |
| 3 | S5 13 treads with rails, landing, sign; S3 9 treads plus floor | **FAIL** | S5 PASS (13 treads). S3 `s4-flur.html` (10.50–13.60 s, see A4): 8 visible treads at x 484–918 step 22.2 (rects 1057.8, 1035.6, 1013.4, 991.2, 969, 946.8, 924.6, 902.4 with widths growing). The j=0 rect (`x=1080.00 width=0.00`, line ~`y=520`) is invisible. Frame 13.2 s shows the stairs at the right edge, 8 steps. **Fix:** in `s4-flur.html`, replace the cumulative tread rects with non-cumulative ones for j=0…8: `x = 1080 − 22.2·(j+1)`, `width = 22.2`, `y = 520 + 90·j` (same top y and height 76 as now). Keep the rail (1040, 480–1310) and feet timing. |
| 4 | ≥8 objects per scene | **PASS** | See Q4. |
| 5 | HUD on every frame; label per scene | **PASS** | See Q5. |
| 6 | Captions per §5.1: 2–4 words per group; C11/C16 one word | **FAIL** | Three groups are merged and exceed 4 words, all in `captions.html`: (a) `#cap-02` 3.35–4.65 "schaue ich aus dem Fenster." (5 words; SPEC C2 3.30–3.95 "SCHAUE ICH AUS" + C3 4.00–4.67 "DEM FENSTER."). Frame 4.3 s shows the 5-word group. (b) `#cap-04` 6.75–7.68 "Sie führen nicht vom Haus weg." (6 words; SPEC C5 6.72–7.22 + C6 7.25–7.72). (c) `#cap-05` 8.32–10.03 "Sie führen direkt auf meine Tür zu." (7 words; SPEC C7 8.30–8.95 + C8 9.00–10.07). Frame 7.0 s shows (b); frame 8.5 s shows (c). **Fix:** replace each with two groups at the SPEC times: `cap-02a` "SCHAUE ICH AUS" 3.30–3.95, `cap-02b` "DEM FENSTER." 4.00–4.67; `cap-04a` "SIE FÜHREN NICHT" 6.72–7.22, `cap-04b` "VOM HAUS WEG." 7.25–7.72; `cap-05a` "SIE FÜHREN DIREKT" 8.30–8.95, `cap-05b` "AUF MEINE TÜR ZU." 9.00–10.07. Each with the 0.12 s fades and hard kill. C11 and C16 are one word already. |
| 7 | `check --json` clean: no errors, no contrast, no layout warnings | **PASS** | See §0. |
| 8 | Abspann: question, two buttons, hint, folge tag; each ≥2 s | **PASS** | Content and visibility times OK (see Q8). Motion violation logged as A1. |
| 9 | All on-screen text German | **PASS** | HUD, captions, labels, poll, badge, folge tag all German. |
| 10 | Figure motion by rotated limbs; stair run 9 treads at 0.19 s | **PASS** | `s4-flur`: 9 steps at 10.55 + 0.19j (rel 0.05…1.57), limb rotations (thigh ±28, shin 40, arm ±35). S1, S3, S5, S6 use limb rigs. |
| 11 | S1 arm raised to glass 3.40–5.20, hand on glass | **FAIL** | `s2-schlafzimmer.html`, rel 1.40–2.20 (abs 3.40–4.20): `#s2-fig-uaR` rotation −70 and `#s2-fig-faR` rotation −35. Frame 4.3 s: the figure stands at x≈290 outside the window frame (x 360–940). The hand ends at ≈(500,850), above the sill, in the glass middle, not at the lower edge (y 974) near (460,960). **Fix:** set `#s2-fig-uaR` to rotation −53 and `#s2-fig-faR` to rotation 0 (elbow ≈(388,906), hand ≈(468,966)). Keep the timing (power2.out / expo.out 0.8 s) and the hold to 5.20. |
| 12 | S2 prints one by one at §3.2 times, scale-in | **PASS** | `s3-hof`: 6.40…10.18 step 0.42; entrance scaleY 0.6→1, opacity →0.9, 0.12 s power2.out. |
| 13 | S3: stair run, door, lock escutcheon and knob, rattle 13.70–14.30 | **PASS (wording conflict)** | Stair run, door, escutcheon (640,840 100×130 #c9ced8) and knob (690,880 r34) present in `s4-flur`. The rattle 13.70–14.28 with ±10°, 6 Hz, is in `s5-schloss` (S4), which is the SPEC §6.2 location. S3 itself ends at 13.60, so the item's wording cannot be met literally. Spec wording should be corrected. |
| 14 | S4 deadbolt slides 15.20–15.45 right 60 px; lock snap sound at 15.50 | **PASS** | `s5-schloss` bolt x +60, 0.25 s power3.out at rel 1.60. Slot flash at 15.50. `hits.wav` onset 15.53 (one frame). |
| 15 | S5 crack 16.95, flash 16.95–17.30, shake table, flinch 16.95–17.05 | **PASS** | `s6-treppenhaus`: crack `#s6-crack` at rel 0.25, flash 0.55→0 over 0.35 s, shake keyframes at 0.05 s, torso +8 power4.out 0.10 s at rel 0.25. Crack visible on right wall in frame 17.5 s. |
| 16 | S6 six prints at 20.62…22.02 with red pulses, thumps, pendant swing, figure looks up and holds from 22.02 | **FAIL** | Timing and count PASS (20.62 … 22.02 in `s7-decke`). Three defects: (a) Red pulse is a flat full-frame rect at opacity 0.4 (`#s7-red`, 0.08 in / 0.17 out). SPEC §9.4 wants 0 → 0.8 inset glow (`inset 0 0 260px 120px rgba(255,59,59,0.45)`); this is a flat wash, not an inset edge. (b) Figure does not hold still from 22.02: `#s7-fig-tor` rotation −1 tween runs from rel 2.5 for 1.0 s, to 22.6 s. (c) Ceiling prints use `rotate(180)` (see A7). **Fix:** (a) replace `#s7-red` with an inset-shadow overlay `box-shadow: inset 0 0 260px 120px rgba(255,59,59,0.45)`, opacity 0 → 0.8 (power2.out 0.08) → 0 (power2.in 0.17) per print at 20.62, 20.90, 21.18, 21.46, 21.74, 22.02. (b) change the tween starting at rel 2.5 to `duration: 0.42` and end with `rotation: 0` at rel 2.92 (22.02). |
| 17 | Light and colour: flat fills, no glow, no bloom, no gradients on ground | **FAIL** | `s1-titel.html` `<circle id="s1-lamp" cx="899" cy="1150" r="70" fill="#ffe9a0" opacity="0.35"/>` is a halo around the street lamp (tween `#s1-lamp` to 0.12 / 0.40 at 1.10 and 1.16). Visible as a grey ring in frame 1.0 s and 1.9 s. **Fix:** delete that circle and its two tweens. The lamp bulb circle (r 10) stays. |
| 18 | Caption scrim rgba(7,11,20,0.55), not full-width; yellow keyword per §5.1 | **FAIL** | Scrim PASS (`.cap .scrim`, 0.55, not full width). Keywords FAIL in `captions.html`: `cap-02` yellow "Fenster." (SPEC AUS); `cap-04` yellow "nicht vom Haus weg." (SPEC NICHT, one word); `cap-05` yellow "auf meine Tür zu." (SPEC DIREKT, one word); `cap-07` yellow "das Schloss." (SPEC SCHLOSS); `cap-10` yellow "knackt es." (SPEC KNACKT); `cap-11` yellow "zweiten Stock." (SPEC STOCK); `cap-12` "Und dann …" has no keyword (SPEC DANN). **Fix:** one yellow `.k` word per group as in §5.1; use the split groups from item 6 and wrap only the keyword in `<span class="k">`. |
| 19 | Sound: bed edited, hits deterministic, cues per §7, bed silent after 25.90 | **PASS** | See §0 audio. Cue onsets match within one frame. Hit-to-bed margin (3–6 dB) NOT VERIFIED (see §4). |
| 20 | No Math.random, Date, fetch, CDN; GSAP local; fonts bundled | **PASS** | See §0. |
| 21 | ✓ drawn as SVG polyline, not a glyph | **PASS** | `s5-schloss` polyline `#s5-check`. No U+2713 in the project. (Draw defect is A10.) |
| 22 | Handle stays @deinhandle | **PASS** | `hud.html` watermark. Frames show it in all snapshots. |

SPEC checklist result: **16 PASS (incl. 13 with note), 6 FAIL (items 3, 6, 11, 16, 17, 18), 0 NOT VERIFIED.**

---

## 4. NOT VERIFIED

| Item | Why |
|---|---|
| SPEC §7 loudness (voice −16 LUFS integrated, true peak ≤ −1 dBTP for the mix) | Needs a render and `npx hyperframes audio <mp4>`. Not run (no render, per instructions). Hits alone measure −1.8 dBTP. |
| SPEC §7 "every hit 3–6 dB above the bed at its time" | Not measured per hit. Bed level in the cue windows was not isolated. |
| BRIEF: voice is ElevenLabs "Vincent Crowe" | Speaker identity cannot be checked from the WAV. Only the silence map was checked against the BRIEF anchors (speech starts 2.02 s per round-1 notes; not re-measured here). |

---

## 5. Additional deviations from SPEC body text (not checklist lines, not counted in the FAIL total)

These do not appear as checklist items but contradict binding SPEC text. Fix them, or amend the SPEC.

| ID | Time | Element | Deviation and exact fix |
|---|---|---|---|
| A1 | 25.50–27.50 | `s8-abspann.html` | SPEC §10.2: "Nothing moves after it lands"; §10.2 and BANNED list: no sliding. Question slides `y: 40 → 0`; red button `x: −40 → 0`; green `x: 40 → 0`; folge tag `scale 0.8 → 1` (back.out); figure arm `#s8-fig-uaR` rotates −165° at 26.9. **Fix:** question, buttons, hint and folge use opacity (and blur) only, no `x`, `y`, `scale`. Delete the stick figure (`#s8-fig`, not in SPEC §10.1) and its tweens. |
| A2 | 6.30–6.80 | `s2-schlafzimmer.html` | SPEC §2.6 window zoom-through (frame group scale 1 → 3.2 about 650,650, power3.in, 0.50 s) is missing. Scene is a hard cut. **Fix:** add a `tl.to` on a frame group (objects 3–7) scale 3.2, `transformOrigin 650 650`, duration 0.5, power3.in, at rel 0. |
| A3 | 10.60 | scene boundaries | `index.html` sets S3 start to 10.50 (`s3-hof` duration 4.20). SPEC §0.2: 10.60. The S3 dip cut at 10.60 (§4, 3 frames at 60 %) is not implemented. **Fix:** `s3-hof` duration 4.30; `s4-flur` `data-start="10.60"` duration 3.00 and its timeline offsets are relative, so the steps stay at 10.55 + 0.19j only if `s4-flur` starts at 10.50. Keep steps; set `data-start="10.50"` and move the label `#loc-4` and the cut to 10.60 in `labels.html`. |
| A4 | 0–30 s | `labels.html` | Label switch times follow the scene starts (10.50 for Haustür, not 10.60). Covered by A3. |
| A5 | 0–2 s | `s1-titel.html` | Title typography: `FUSSSPUREN` 120 px at top 690 (SPEC 150 px, y 720–880). Letter blur 14 px and stagger 0.067 s (SPEC blur 4 px, stagger 0.10 s, 0.13 s each). Moon at (800,330) r 92 #fff6dd (SPEC (830,300) r 70 #dfe8f5). Houses: 3 polygons (SPEC 6 at y 1100–1240). Snowflakes: 35 (SPEC 18). Frame-0 rule (SPEC §1 "title ≥30 % opacity at frame 0") is not met: letters start at opacity 0 at 0.15 s. **Fix:** set font-size 150 and top 720; letters blur 4 px, stagger 0.10, duration 0.13; moon to (830,300) r 70 #dfe8f5; start the letter tween at 0 with opacity 0.3. |
| A6 | 19.10–25.50 | `s7-decke.html` pendant | SPEC §9.1: amplitude 4° at 20.62, adds 2° per thump, **decays** (time constant 1.2 s). The tweens grow amplitude (4, 6, 8, 10, 12, 14). **Fix:** use the decaying amplitude sequence from §9.1. |
| A7 | 20.62–22.02 | `s7-decke.html` `#s7-p1`…`#s7-p6` | SPEC §9.2: `rot 0°` (toes up, "upside down relative to floor prints"). Index uses `rotate(180)`, following round-1 D4. The prints use `#05070c` at 0.85 on `#14101a`. Frame 22.0 s: the prints are barely visible. **Decision needed:** choose `rot 0` (SPEC literal) or 180 (round-1 D4) and update the SPEC. Raise print contrast if the SPEC colour is kept. |
| A8 | 16.95–17.30 | `s6-treppenhaus` flash | Flash is a full-frame `#ff3b3b` rect at 0.55, as SPEC §8.1. OK. (No action.) |
| A9 | 20.62 | `s7-decke` breathing | Covered by item 16. |
| A10 | 14.70–14.90 | `s5-schloss.html` `#s5-check` | Check draws incompletely: polyline length ≈ 32 + 57 = 88.6 px, `stroke-dasharray="40"`, so the second stroke (40–80 px) is never drawn. Frame 16.5 s shows a short fragment. **Fix:** add `pathLength="100"` to the polyline, set `stroke-dasharray="100"` and animate `stroke-dashoffset` 100 → 0 over 0.20 s starting 14.70 (rel 1.10). |
| A11 | 1.52–3.1 s | `s3-hof` / `s1` | Snowflakes in S1 (35) and S2/S3 use fixed positions; SPEC §0.3 defines 18 per scene. Harmless visually; fix only if the SPEC count is binding. |

---

## 6. Summary

- Checklist FAIL items (counted): **6**: item 3 (S3 stairs, 8 visible treads, 10.55–12.07 s), item 6 (captions 3.35–4.65, 6.75–7.68, 8.32–10.03 merged), item 11 (S1 arm, 3.40–4.20 s), item 16 (S6 red pulse, figure motion after 22.02 s), item 17 (`s1-titel` lamp halo, 0–2 s), item 18 (caption keywords at 3.35, 6.75, 8.32, 10.50, 16.70, 17.77, 19.14 s).
- BRIEF quality criteria: 8 PASS, 0 FAIL.
- Round-1 defects fixed: D1, D2, D3, D5, D7, D8, D9 (glyph), D10, D11, D14, D15, D17. Partly fixed: D4, D9 (draw), D12, D13. Not fixed: D6 (arm pose), D16 (stairs).
- Check: 0 errors, 0 warnings; 5 info only.
- Audio: bed silent 18.45–19.60 and after 25.90; hits at the SPEC times (+1 frame).
- Additional deviations A1–A11 are not counted, but A1 and A2 break explicit SPEC text.

**Recommendation:** NOT READY. Fix items 3, 6, 11, 16, 17, 18 and A1, A2, A10, then re-run `check --json` and snapshot. Decide A7 (ceiling print rotation) in the SPEC before the next round.
