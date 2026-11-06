# REVIEW: Teil 1 „Fußspuren im Schnee“ (Checker)

**Verdict: NOT READY. 18 FAIL rows** (15 distinct defects, see section 2).

Checked: `index.html`, `compositions/s1..s8`, `assets/` (figure.js, voice-timed.wav, sfx.wav) against BRIEF.md (criteria 1–8) and SPEC.md (checklist 1–22). No project file was edited. Evidence came from `hyperframes check --json`, `hyperframes snapshot` (frames in `/tmp/hf/check-snaps/`), code reading, and ffmpeg on the audio. No final MP4 was rendered.

---

## 1. Acceptance table

Evidence key: "frame t" = snapshot at t s; "code" = read from the composition source.

### BRIEF quality criteria

| # | Criterion | Result | Evidence |
|---|---|---|---|
| B1 | 0–2 s shows only title card, no narration | PASS | Frames 0.5 s, 1.0 s, 1.9 s show only FUSSSPUREN / IM SCHNEE / HUD. First caption `#cap-01` starts 2.02 s (code). |
| B2 | Footprints on snow, spread gate→door, never on glass, pointing at door | FAIL | Prints on snow at 8.5 s and 10 s (frame 8.5 s, correct). But `#s3-p10` (y 1337) and `#s3-p11` (y 1503) sit on the house wall/door panel (wall rects y 1380+, door x 396–684), not on snow. Prints are a narrow column x 474–517, not spread from gate (x 296–384) to door. |
| B3 | Staircase ≥ 12 steps, banister, landing | PASS | `s6-treppenhaus`: 14 tread polygons (fill #1b2233), two rails, sign „2. OG“. Frame 18 s shows the full stepped stair. |
| B4 | ≥ 8 identifiable objects per scene | PASS | Every scene has 9–22 objects in code and in the frames. |
| B5 | HUD constant, location label changes per scene | PASS | HUD present in all 19 snapshots. Label set differs from SPEC §0.2 (see D14). |
| B6 | Captions match speech segments ±0.15 s, never two groups at once | PASS | Caption start/end times in `index.html` match all BRIEF anchors within ±0.02 s (e.g. cap-03 5.27–6.28, cap-10 16.72–17.28 fade, cap-13 20.56). Structural deviation: SPEC §5.1 splits 21.91–25.42 into C17/C18; index has one group (D12). |
| B7 | `check --json`: no errors, no contrast or layout warnings | FAIL | errors 0; contrast 37/37 passed; layout 0 warnings but 4 info (container_overflow). Lint: **12 warnings** (`timeline_track_too_dense`, 11× `nested_structure_needs_subcomposition`). |
| B8 | Abspann poll, each text ≥ 2 s | PASS | Question 25.5–30, red button 26.0–30, green 26.2–30, hint 26.5–30, folge tag 26.5–30 (code, `s8-abspann`). Frame 29.75 s shows all texts and the folge tag. |

### SPEC checklist (§11)

| # | Item | Result | Evidence |
|---|---|---|---|
| S1 | 0–2 s title only; first caption at 2.00 | PASS | As B1. Caption at 2.02 matches BRIEF anchor. |
| S2 | 10 prints, §3.2 positions and times, on snow, grow toward viewer | FAIL | 12 prints `#s3-p0`–`#s3-p11`, appear 6.75–9.83 s in 0.28 s steps (spec 6.40–10.18, 0.42 s). Positions differ from §3.2 table. p10/p11 on the door (see B2). |
| S3 | S5 stair 13 treads with rails, landing, sign; S3 stair 9 treads | FAIL | S5 OK (14 treads, D3 passes). S3 `s4-flur` has **8** treads (rects x 484–918 step 62), spec 9. |
| S4 | ≥ 8 objects per scene | PASS | See B4. |
| S5 | HUD on every frame, label per scene (§0.2 names) | PASS | HUD present in all snapshots. Label names differ (D14). |
| S6 | Captions per §5.1, groups ≤ 4 words, C11/C16 one word | FAIL | Timing OK (B6). Groups differ from §5.1: C17+C18 merged into `#cap-14` (21.93–25.40, 4 words). Minor. |
| S7 | `check --json` clean | FAIL | See B7. |
| S8 | Abspann content and timing | PASS | See B8. |
| S9 | All on-screen text German | PASS | HUD, captions, labels, poll, badge text, folge tag are German. |
| S10 | Figure motion by rotated limbs, run down stairs 9 treads at 0.19 s | FAIL | Limb rig used in `s4-flur`, `s2-schlafzimmer`, `s8-abspann`. Run is 8 steps (`k` 1–8, step 0.14 s, not 9 × 0.19 s). S5 (`s6-treppenhaus`) and S6 (`s7-decke`) have **no figure at all**. |
| S11 | S1 arm raised to glass 3.40–5.20, hand on glass | FAIL | Frames 4.3 s / 5.5 s: arm reaches about x 280, window glass starts x 386 (spec hand at 460,960), curtain x 270–340 in between. Figure is at left 110 (`#s2-fig`), arm length 94 px (rig scale 330 px high, spec 520). |
| S12 | S2 prints one by one 6.40–10.18, step 0.42, scale-in | FAIL | Times 6.75–9.83, step 0.28 (see S2). Entry is `scale 0.4→1 back.out` and opacity to 0.92, not scaleY 0.6→1, opacity 0→0.9, 0.12 s. |
| S13 | S3: stair run, door, lock escutcheon + knob, rattle 13.70–14.30 | FAIL | Stair run, door, knob present. **No lock escutcheon** (spec 640,840). Knob rotation `#s4-knob` at 12.6 s, door wobble 12.8–13.2 s (not 13.70–14.30). |
| S14 | S4 deadbolt slides 15.20–15.45 right 60 px; lock snap sound at 15.50 | FAIL | `#s5-bolt` moves **left** −300 px at 13.95–14.55 s. No lock-snap sound (no hits.wav, D2). |
| S15 | S5 crack 16.95, red flash 16.95–17.30, shake table, flinch 16.95–17.05 | FAIL | `#s6-crack` at 17.1 s (draws 0.5 s, spec 0.12 s) on the **left** wall. Flash `#s6-flash` at 17.4–17.64 s. No shake table. No flinch (no figure). |
| S16 | S6 six ceiling prints at 20.62 … 22.02, red pulses, thumps, pendant swing, figure looks up | FAIL | `#s7-p0`–`#s7-p10`: **11 prints** at 20.60–24.90 s (spec 6 prints at 20.62–22.02). Pendant swing `#s7-pend` OK. No figure. No thump sound (D2). Frame 21 s: prints barely visible, not clearly inverted (D4). |
| S17 | Flat fills, no glow/bloom/gradient on ground | FAIL | `radial-gradient` backgrounds in `s1-titel` (`#s1-sky`) and `s8-abspann`; radial overlay in `s2-schlafzimmer`; light-cone radial gradient `#s7-light`; halo ellipse in `s6-lamp` (opacity 0.08). |
| S18 | Caption scrim rgba(7,11,20,0.55) behind text | FAIL | No scrim in `index.html` `.cap` (only text-shadow). Captions also slide (`y: 16 → 0`), which the BANNED list forbids. Keyword yellow is correct. |
| S19 | Sound: bed edited 18.45–19.60 silent, hits.wav generated, cue list, bed silent after 25.90, bed gain 0.45 | FAIL | `assets/sfx.wav` is the unedited original: 18.45–19.60 mean −20.0 dB, **max −4.2 dBFS** (the impact the spec removes). 25–26 s still audible (mean −29.8, max −20.2). `assets/hits.wav` does not exist. Index bed gain `data-volume="0.3"` (spec 0.45). Footstep hits (6.40…10.18, 10.55…12.07, 20.62…22.02) absent. See D1/D2. |
| S20 | No Math.random, Date, fetch, CDN; GSAP local; fonts Archivo Black and Inter only, bundled | FAIL | No `Math.random`, `Date`, `fetch`, or CDN in project code (grep clean). GSAP local. **Fonts not bundled**: `assets/` has no font files; check log says fonts were fetched from Google Fonts at compile time (D8). |
| S21 | ✓ drawn as inline SVG polyline, not a glyph | FAIL | `compositions/s5-schloss.html`: badge text `VERRIEGELT ✓` uses U+2713. No SVG check. |
| S22 | Handle stays `@deinhandle` | PASS | `#watermark` in `index.html`, visible in all frames. |

### Not verified

| Item | Status | Why |
|---|---|---|
| SPEC §7 loudness (voice −16 LUFS, true peak ≤ −1 dBTP) and hit peaks | NOT VERIFIED | Needs a render and `npx hyperframes audio <mp4>`. Not run, per instructions (no MP4). |

---

## 2. Defects, most severe first

Each entry: time, element/file, what is wrong, exact fix.

**D1. Sound bed not edited (critical).** Time 18.45–19.60 s. File `assets/sfx.wav` (also `index.html` `#sfx`, `data-volume="0.3"`).
Wrong: the original impact is still in the bed, max −4.2 dBFS, which the picture does not match.
Fix: write `assets/sfx-bed.wav` (do not overwrite the source) with `ffmpeg -i assets/sfx.wav -af "afade=t=out:st=18.40:d=0.05,volume=enable='between(t\,18.45\,19.60)':volume=0,afade=t=in:st=19.60:d=0.05,volume=0.45/0.3,afade=t=out:st=25.40:d=0.50,atrim=0:25.90,apad=whole_dur=30" -ar 48000 -ac 2 assets/sfx-bed.wav`, then point `#sfx` at `assets/sfx-bed.wav` with `data-volume="1"`. Verify with `ffmpeg -af volumedetect` on 18.45–19.60 (must be < −60 dB mean) and 26–30 s (silent).

**D2. Missing `assets/hits.wav` (critical).** Times: 6.40–10.18 (snow crunch ×10), 10.55–12.07 (stair step ×9), 12.26/12.42/12.58 (floor), 12.90 (door thump), 13.70–14.30 (lock click ×7), 15.50 (deadbolt snap), 16.95 (crack), 17.10 (rumble), 20.62–22.02 (ceiling thump ×6).
Fix: write `scripts/make_hits.py` (stdlib only, no `random`, LFSR seed 0xACE1), output 48 kHz stereo, 30 s, `assets/hits.wav`, with the hit types in SPEC §7 at the listed times. Add `<audio id="hits" src="assets/hits.wav" data-start="0" data-duration="30" data-volume="1">` to `index.html`.

**D3. No stick figure in S5 Treppenhaus or S6 Decke (critical).** Files `compositions/s6-treppenhaus.html` (16.70–19.10) and `compositions/s7-decke.html` (19.10–25.50).
Fix: add a figure with `Fig.init` and the SPEC §8.2 pose (feet 540,1690, H 390, facing up the stairs) to s6, with the 16.95 flinch (`#…-torso` rotation +8° power4.out 0.10 s) and sway. In s7, add the SPEC §9.3 figure (feet 200,1760, H 380, head −20°) with knee dips at 20.62, 20.90, 21.18, 21.46, 21.74. Use `Fig.cycle`/`Fig.rest` pattern from `figure.js` for limbs.

**D4. Ceiling prints: count, timing, orientation (critical).** `compositions/s7-decke.html` `#s7-p0`–`#s7-p10`, `#s7-d0`–`#s7-d10`, and the timeline lines 30–95.
Wrong: 11 prints at 20.60–24.90 s (spec 6 at 20.62–22.02). Rotation is `rotate(0 30 50)`. The glyph's default orientation already has toes at the top, so these look upright, not inverted (this confirms the builder's open point).
Fix: delete `#s7-p0`, `#s7-p1`, `#s7-p7`–`#s7-p10` and their `#s7-d*` rings. Keep six prints p1–p6 from SPEC §9.2 table, but with the coordinates from SPEC: (260,600,W40), (330,700,W46), (300,800,W54), (380,900,W62), (350,1010,W70), (430,1120,W80). Set `transform="translate(...) scale(W/60) rotate(180 30 50)"` so the toes point down, i.e. inverted against the glyph's upright. Timing: `tl.fromTo` at absolute 20.62, 20.90, 21.18, 21.46, 21.74, 22.02 (relative 1.52, 1.80, 2.08, 2.36, 2.64, 2.92 for `s7` starting 19.10), entrance scale 1.25→1.00 power4.out 0.10 s and opacity 0→0.85 in 0.08 s. Red pulse per print 0.25 s (SPEC §9.4).

**D5. Footprints on the door and wall; wrong count and timing (critical).** `compositions/s3-hof.html` `#s3-p0`–`#s3-p11`, timeline lines 30–41.
Wrong: `#s3-p10` (y 1337) and `#s3-p11` (y 1503) sit on the house wall and door panel. There are 12 prints, not 10. Appearance 6.75–9.83 s, not 6.40–10.18 s.
Fix: remove `#s3-p10`, `#s3-p11`. Keep 10 prints with the SPEC §3.2 table (centres and W: (312,700,25), (371,750,28), (359,800,32), (418,850,35), (405,900,39), (465,950,42), (452,1000,46), (511,1050,49), (499,1100,53), (558,1150,56)). Alternate `rotate(174)`/`rotate(186)` as in the spec. Appearance at 6.40 + 0.42·k. Entrance: scaleY 0.6→1.0 and opacity 0→0.9 in 0.12 s, power2.out.

**D6. S1 figure does not reach the window (critical).** `compositions/s2-schlafzimmer.html` `#s2-fig` (left 110, top 1252, 160×330).
Wrong: the figure stands left of the curtain at x 110–270, and the arm (about 94 px) stops near x 280. Spec: feet (300,1300), hand on glass at (460,960).
Fix: rebuild the figure at H 520 (`viewBox` height 520, SPEC §0.4 lengths). Place the div so the feet sit at (300,1300) and hip at (300,1020). Arm upper 110 + forearm 100 reaches the glass at (460,960). Apply rotations from SPEC §2.2 (upper arm 0→70, forearm 0→−35, 3.40–4.20 s, power2.out/expo.out).

**D7. Figure bodies are wrong size and do not match SPEC scale (major).** Same file as D6. Fixed by D6 fix.

**D8. Fonts not bundled (major).** `assets/` has no font files, `index.html` has no `@font-face`.
Fix: copy `ArchivoBlack-Regular.woff2` and `Inter` variable woff2 (weights 700, 900) into `assets/fonts/`. Add to `index.html` `<style>`:
`@font-face{font-family:"Archivo Black";src:url("assets/fonts/ArchivoBlack-Regular.woff2") format("woff2");font-weight:400}` and the same for Inter with `font-weight:700 900`. Remove any dependence on Google Fonts.

**D9. Lock badge uses glyph ✓ (major).** `compositions/s5-schloss.html` `#s5-badge` text `VERRIEGELT ✓`, time 14.55–16.70.
Fix: replace the text with `<text>VERRIEGELT</text>` plus `<polyline points="900,335 920,360 960,320" fill="none" stroke="#ffffff" stroke-width="14" stroke-linecap="round" stroke-dasharray="40" stroke-dashoffset="40"/>` and animate `stroke-dashoffset` 40→0 over 0.20 s starting at 14.70 (SPEC §6.3). Badge `scale 1.20→1.00` and opacity 0→1 over 0.20 s at 14.55 (SPEC §6.2). Keep badge visible until 16.70.

**D10. Lock beats wrong (major).** `compositions/s5-schloss.html` and `index.html` lines 98–100.
Wrong: `#s5-bolt` slides left −300 at 13.95; should slide right +60 px at 15.20–15.45. No lock snap sound at 15.50. The rattle is absent: the knob circle (line 12 `circle cx="540" cy="960" r="96"`) has no id and no rotation. No lock escutcheon in `s4-flur` (SPEC §4.1 #8 at 640,840, 100×130, #c9ced8). Camera `#s5-cam` pushes 1→1.07 over 3.1 s; SPEC S4 says camera fixed.
Fix: give the knob `id="s5-knob"`; add `tl.to("#s5-knob",{rotation:10,...})` at 6 Hz (sine) 13.70–14.30 with `svgOrigin 540 960`. Add `shake` of `#s5-cam` ±3 px sine 6 Hz over 13.70–14.30. Change the bolt tween to `x: 60, duration: 0.25, ease: "power3.out"` at 15.20 and reset the lever. Set `#s5-cam` scale to 1 (remove the push). Add the escutcheon rect to `s4-flur`. Add the snap sound via `hits.wav` at 15.50 (D2).

**D11. S5 crack and flash timed wrong; crack on wrong wall; no shake table (major).** `compositions/s6-treppenhaus.html` `#s6-crack` (line 20), `#s6-flash` (line 21), `#s6-cam` (line 23).
Fix: crack starts at relative 0.25 (16.95) with duration 0.12 power2.out, path per SPEC §8.1 (`M960 1040 L985 1120 L950 1200 L1000 1290 L975 1400`, plus branches), stroke black 4 px, on the right wall. Flash `#s6-flash` 0.55→0 over 16.95–17.30 (relative 0.25–0.60), power2.in. Shake `#s6-cam` at 16.95 with keyframes (+8,−5), (−8,+4), (+6,−3), (−4,+2), (+2,−1), (0,0) every 0.05 s (fixed table).

**D12. Captions: missing scrim, slide motion, merged group (major).** `index.html` `.cap` CSS (lines 55–59) and `#cap-14` (line 115 and timeline 164–166).
Fix: wrap each caption text in `<span class="scrim">` styled `display:inline-block;background:rgba(7,11,20,0.55);padding:6px 22px;border-radius:6px`. Remove `y` in the `fromTo` calls (lines 125–164). Split `#cap-14` into `#cap-14a` "GENAU ÜBER" (21.91–23.30) and `#cap-14b` "MEINEM KOPF." (23.35–25.42) with the same 0.12 s fades.

**D13. Radial gradients and glow against BANNED list (minor-major).** `compositions/s1-titel.html` line 15 (`#s1-sky` radial-gradient), `compositions/s8-abspann.html` line 12 (background radial-gradient), `compositions/s2-schlafzimmer.html` line 12 (radial-gradient overlay), `compositions/s7-decke.html` `#s7-light` (radialGradient), `compositions/s6-treppenhaus.html` `#s6-lamp` (halo ellipse, opacity 0.08).
Fix: replace each background with a flat fill (`#0a1730` for s1 sky, `#0a0d16` for s8, drop the s2 overlay rect, use a solid polygon at opacity 0.5 in s7, delete the s6 halo ellipse).

**D14. HUD location labels differ from SPEC §0.2 (minor).** `index.html` lines 92, 94, 95, 98.
Fix: `#loc-2` text "Fenster" → "Schlafzimmer"; `#loc-4` "Flur" → "Haustür"; `#loc-5` "Haustür" → "Schloss"; `#loc-8` "Entscheidung" → "Umfrage".

**D15. Check warnings: 12 structural (minor, but fails B7/S7).** `index.html`.
Fix: move `#hud`, `#wm`, the eight `#loc-*` divs, and `#captions` into `compositions/hud.html` and `compositions/captions.html`, mounted with `data-composition-src`. Split the timeline into sub-compositions so track 3 has fewer than 8 timed items. Re-run `check --json` until warnings are 0.

**D16. Stairs in S3 have 8 treads, not 9 (minor).** `compositions/s4-flur.html` treads at x 918, 856, 794, 732, 670, 608, 546, 484. Fix: add one tread at x 422 (y 1288), extend the rail polyline and the step timing to 9 steps at 0.19 s (SPEC §4.3).

**D17. Abspann folge tag timing (cosmetic).** `compositions/s8-abspann.html` line 23: folge tag starts at 26.5 (spec 27.6). Fix: set `tl.fromTo("#s8-folge", …, 27.6-25.5)` = 2.1 s relative. Other abspann timings are fine.

---

## 3. Check summary

- `npx --yes hyperframes@0.9.17 check --json`: **ok: true, errors 0, warnings 12, info 4**.
  - lint: 0 errors, 12 warnings (`timeline_track_too_dense` ×1, `nested_structure_needs_subcomposition` ×11), 9 files scanned.
  - layout: 0 errors, 0 warnings, 4 info (`container_overflow` at 8.33 s `#s3-hof` circle, 15 s `#s5-cam`, 18.33 s `#s6-cam`, 21.67 s `#s7-cam`).
  - contrast: 37 of 37 passed. runtime, motion, craft, audio: 0 findings.
- Snapshots: 19 frames (0.5 … 29.75 s) in `/tmp/hf/check-snaps/`, contact sheets `contact-sheet-1..3.jpg`.
- Audio (`ffmpeg volumedetect`, `sfx.wav`): 18.45–19.60 s mean −20.0 dB, max −4.2 dBFS (fails). Quiet elsewhere (5–6 s mean −42.6 dB). 25–26 s mean −29.8 dB (bed not faded out).
- Voice `voice-timed.wav` silence map matches BRIEF anchors: speech starts 2.02 s, pauses at 4.65, 6.28, 7.68, 10.03, 12.91, 14.51, 16.17, 17.40, 18.45, 20.19, 21.52, 25.40. Good.
- Bans grep: no `Math.random`, `Date`, `fetch`, or CDN URL. One `✓` glyph (D9).
