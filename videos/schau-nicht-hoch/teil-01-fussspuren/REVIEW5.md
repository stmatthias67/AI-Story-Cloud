# REVIEW5: Teil 1 „Fußspuren im Schnee“ (Checker, round 5)

**Verdict: NOT READY. 5 FAIL items.**

Scope: read-only. No project file was edited, nothing committed, pushed or rendered. Report written only.

Sources: `hyperframes@0.9.17 check --json` (saved to `/tmp/hf/check5.json`), `snapshot` at the 19 requested times (`/tmp/hf/check5-snaps/`, contact sheets 1–3, frames), full-resolution crops in `/tmp/hf/c5_*.png`, numpy analysis of `assets/hits.wav` and `assets/sfx-bed.wav` (48 kHz), code reading of `compositions/*.html`, `index.html`, `SPEC.md` (incl. `## Änderungen`), `BRIEF.md`, `REVIEW4.md`.

---

## 0. Tooling evidence

| Check | Result |
|---|---|
| `check --json` | `ok: true`. lint 0/0, runtime 0/0, motion 0/0, contrast 0/0, craft 0/0, audio 0/0. Layout: 0 errors, **0 warnings**, 5 info `container_overflow` (`#s1-flk`, `#s2-cam`, `#s3-hof` svg g, `#s4-flur` svg g, `#s5-cam`). Info only. Note: the check did **not** flag the end-card overlap (F1); it is a layout the tool does not catch. |
| Snapshots | 19 frames at the requested times, plus 3 contact sheets. |
| Scene labels (HUD) | Draußen, Schlafzimmer, Hof, Haustür, Schloss, Treppenhaus, Decke, Umfrage. Visible in the frames. |
| Banned patterns (code) | No `Math.random`, `Date`, `fetch`, CDN, gradients or `✓` glyph in the checked files. GSAP local. Fonts bundled. |

---

## 1. Requested visual checks

| Check | Verdict | Evidence |
|---|---|---|
| Title alone, one line, at 0–2 s | **PASS** (with F2 note) | 0.5 / 1.0 / 1.9 s: only moon, houses, snow, HUD and title. „FUSSSPUREN“ on one line, „IM SCHNEE“ below. No narration before 2.00 s. Horizontal extent is too wide for the 80 % title-safe rule, see F2. |
| Arm hand on the glass at 4.3 s | **PASS** | Crop `/tmp/hf/c5_arm43.png`: the hand ends at about (460, 958), inside the lower edge of the glass pane (glass bottom y 974). Mirrored angles, documented deviation (a). |
| 9 visible hallway treads near 11 s | **PASS** | Crop of 11.5 s (`/tmp/hf/c5_stairs115.png`): nine tread tops visible on the right, down to the floor. Code: `s4-flur` treads j = 0…8. |
| 6 hallway flakes | **NOT VERIFIED** (count) | Code: `#s4-flk` holds 18 flakes (SPEC §0.3, Änderungen F-S2). They are 2–4 px dots, and only about 6–8 are clearly countable in the 11.5 s crop. Exact visible count is not confirmed. |
| 10 yard prints on snow only | **PASS** | 8.5 s contact sheet: a trail of 10 dark prints on the light snow of the yard, growing toward the door. None on the glass. |
| 6 ceiling prints | **PASS** (count) with F4 | 22.5 s: six prints on the ceiling. Print p6 is partly hidden under the caption scrim, see F4. |
| Check mark complete at 16.5 s | **PASS** | 16.5 s: „VERRIEGELT“ badge with the full SVG check mark. |
| End card readable, no overlaps at 26–29 s | **FAIL** | Question, both buttons, hint and folge tag are legible at 26, 27.5, 29 s. The folge tag overlaps the watermark pill at 27.6–30 s, see F1. |
| Audio: every cue 3–6 dB above bed | **PASS** | 38 cues measured (see §2). All margins 4.25–4.73 dB. |
| Audio: silence 18.45–19.60 s | **FAIL** (minor), see F5 | Bed is silent from 18.50 to 19.60 s. A fade tail of about -48.5 dBFS remains in 18.45–18.50 s. Hits are silent (-240 dBFS). |

---

## 2. Audio measurements

Margin = peak of `hits.wav` in the 66 ms window starting at cue + 33 ms, minus the peak of `sfx-bed.wav` × 0.45 in the same window (dB).

| Cue group | Cues (s) | Margin (dB) |
|---|---|---|
| Snow crunch ×10 | 6.40 … 10.18 | 4.50 each |
| Stair step ×8 | 10.74 … 12.07 | 4.50 each |
| Floor step ×3 | 12.26, 12.42, 12.58 | 4.49–4.50 |
| Door thump | 12.90 | 4.50 |
| Lock click ×7 | 13.70 … 14.30 | 4.50 each |
| Deadbolt blip | 15.50 | 4.50 |
| Crack | 16.95 | 4.50 |
| Rumble | 17.10 | 4.73 |
| Ceiling thump ×6 | 20.62 … 22.02 | 4.25–4.39 |

All 38 cues are within 3–6 dB. This matches the Änderungen claim (4.25–4.73 dB). Measured on the same window the builder used, so the 66 ms window is the documented deviation (b): accepted.

---

## 3. BRIEF.md criteria 1–8

| # | Criterion | Verdict | Evidence |
|---|---|---|---|
| 1 | 0–2 s title only, no narration | **PASS** | §1 above. |
| 2 | Footprints on snow, gate to door, never on glass, pointing to door | **PASS** | 10 prints at 8.5 s on the yard snow, rotated 180° so toes point to the door. |
| 3 | Stairs ≥ 12 steps, banister, landing | **PASS** | S5 `s6-treppenhaus`: 13 treads, rails, landing, sign „2. OG“ (17.5, 18.5 s). |
| 4 | ≥ 8 identifiable objects per scene | **PASS** | All eight scenes in the frames. |
| 5 | HUD present throughout; location label changes per scene | **FAIL** | HUD and labels are present in every frame. But at 10.60–10.93 s the stick-figure head covers the „HAUSTÜR“ label, see F3. |
| 6 | Captions in sync ±0.15 s, never two groups at once | **PASS** | Single caption group in every checked frame. Timing per SPEC §5.1. |
| 7 | `check --json` clean (no errors, no contrast/layout warnings) | **PASS** | 0 errors, 0 warnings. 5 info only. |
| 8 | End card: poll visible, each text ≥ 2 s | **PASS** | Question 25.50; red button 26.10; green 26.30; hint 26.80; folge tag 27.60 to 30.00 (2.4 s). The overlap is tracked as F1. |

BRIEF result: **6 PASS, 1 FAIL (criterion 5, F3), 0 NOT VERIFIED**. Criterion 8 passes on timing and text. The tag/watermark overlap is F1.

Technical requirement from BRIEF „Technische Vorgaben“ (80 % title safe): **FAIL**, see F2.

---

## 4. SPEC.md checklist (§11, items 1–22)

| # | Item | Verdict | Evidence / note |
|---|---|---|---|
| 1 | 0–2 s title only; C1 at 2.00 | **PASS** | §1. |
| 2 | 10 prints on snow, gate to door, toward door, growing | **PASS** | 8.5 s. |
| 3 | S5 13 treads; S3 9 treads plus floor | **PASS** | Code: 13 and 9 treads. Visual at 11.5 s and 17.5 s. |
| 4 | ≥ 8 objects per scene | **PASS** | §3 above. |
| 5 | HUD on every frame; label per scene | **PASS** | HUD present. Its legibility is F3 (BRIEF 5). |
| 6 | Captions per §5.1 | **PASS** | Groups match the table; C11 and C16 are one word. |
| 7 | `check --json` clean | **PASS** | §0. |
| 8 | End card elements, each ≥ 2 s | **FAIL** | Elements and timing pass. The folge tag overlaps the watermark, see F1. |
| 9 | All text German | **PASS** | All on-screen text in German. |
| 10 | Figure motion by rotated limbs; stair run | **PASS** | Limb rigs in S1, S3, S5, S6. Cadence 0.19 s. Sync per Änderungen F-S3 option (a). |
| 11 | S1 arm to glass 3.40–5.20, hand on glass | **PASS** | §1; deviation (a) documented. |
| 12 | S2 prints at §3.2 times | **PASS** | 6.40 … 10.18 in 0.42 s steps (code). |
| 13 | S3 stair run, door, escutcheon, knob; rattle 13.70–14.30 | **PASS** | 13.2 s shows door, escutcheon, knob and figure. The rattle beats are in S4 (13.60–16.70) per §6.2. The item text places them in S3; that wording is off, and the rattle itself is correct. |
| 14 | S4 deadbolt 15.20–15.45, snap 15.50 | **PASS** | Bolt unmoved at 14.5 s, moved into the jamb at 16.5 s. Snap cue at 15.50 (-19.8 dBFS peak). |
| 15 | S5 crack 16.95, flash, shake, flinch | **PASS** | Crack visible at 17.5 s. |
| 16 | S6 ceiling prints 20.62…22.02, pulses, thumps, pendant, figure looks up | **PASS** | Six prints at 22.5 s. p6 partly hidden under the caption, see F4. |
| 17 | Light and colour, no glow or gradients | **PASS** | Flat fills. Only the required S6 red pulse. |
| 18 | Captions scrim, one yellow keyword | **PASS** | Scrim visible in frames 4.3, 8.5, 11.5, 14.5, 20.6, 22.5. |
| 19 | Sound: bed edited, hits deterministic, cues, bed silent after 25.90 | **FAIL** | Hit margins PASS (§2). Bed silent after 25.90 PASS. Silence 18.45–19.60 has a -48.5 dBFS tail in 18.45–18.50 s, see F5. |
| 20 | No Math.random, Date, fetch, CDN; GSAP local; fonts bundled | **PASS** | §0. |
| 21 | ✓ as SVG | **PASS** | Crop of 16.5 s. |
| 22 | Handle `@deinhandle` | **PASS** | Watermark in every frame. |

SPEC checklist: **19 PASS, 2 FAIL (items 8 and 19), 1 linked to the HUD item (5) with F3 noted as a visual issue, 0 NOT VERIFIED from 1–22.** Count as **2 FAIL** items at checklist level; the FAIL list below is 5.

---

## 5. Änderungen (SPEC) and REVIEW4 items

Accepted deviations:

| Item | Verdict | Note |
|---|---|---|
| Deviation (a) S1 near-arm mirrored (uaR −70, faR +35) | **PASS (accept)** | Documented in SPEC §2.2 and Änderungen F-S4. Visible result: hand on the lower glass edge at 4.3 s (`/tmp/hf/c5_arm43.png`). |
| Deviation (b) hit window 66 ms at +4.5 dB | **PASS (accept)** | Documented in SPEC §7 and Änderungen F-S1. All 38 cues measured 4.25–4.73 dB, within 3–6 dB. |
| REVIEW4 F-S1 hit levels | **PASS** | §2. |
| REVIEW4 F-S2 S3 snowflakes 18 | **PASS** (code) | `s4-flur.html` `#s4-flk`: 18 circles, formula values correct. Visible count not confirmed, see §1. |
| REVIEW4 F-S3 stair sync, option (a) | **PASS** (code) | Tween landings at 10.74 + 0.19k (k = 0…7), matching the 8 stair hits. First tween starts at 10.55, before the scene's 10.60 start, hidden by the dip cut; accepted as documented. |
| REVIEW4 F-S4 arm angles | **PASS** | Code: `s2-fig-uaR` −70, `s2-fig-faR` +35 (lines 25–26). |
| REVIEW4 F-S7a end-card flakes (6) | **PASS** | `compositions/s8-abspann.html`: six `.s8-flk` circles, `#dfe8f5`, opacity 0.85. |
| REVIEW4 F-S7b end-card layout | **PASS** (code) | Question top 600, red 920, green 1110, hint 1300, folge 140/1440 700×84 44 px, door-frame rects #161a24 added, zigzag removed, background #0d0f16. The folge tag position itself causes F1. |

---

## 6. FAIL items

### F1. 27.60–30.00 s, end card, folge tag vs watermark pill: FAIL

- **Element:** `#s8-folge` („FOLGE FÜR TEIL 2“, `compositions/s8-abspann.html`) and `#watermark` („@deinhandle“, HUD, track 2).
- **What is wrong:** measured on the 29 s frame: folge tag box x 140–839, y 1440–1523. Watermark pill box x 758–1010, y 1507–1561. Overlap box x 758–839, y 1507–1523 (about 82 × 17 px). SPEC §10.1 says the tag stays „away from the watermark (x 900–1010)“. That is an arithmetic error: the pill is about 252 px wide, so its left edge is at x 758, not 900.
- **Exact fix:** in `compositions/s8-abspann.html`, change `#s8-folge` from `top: 1440px` to `top: 1400px`. The tag then spans y 1400–1484, which clears the pill top at y 1507 by 23 px. Keep width 700 and height 84. Add to SPEC `## Änderungen`: „Fix-Runde 6, F1: Folge-Marke top 1400 (statt 1440); Wasserzeichen-Pille reicht bis x 758, daher vertikal getrennt.“ Re-snapshot at 29 s and confirm no overlap.

### F2. 0.00–2.00 s, title „FUSSSPUREN“ (S0), 80 % title-safe rule: FAIL

- **Element:** `#s1-t1` line 1, 150 px Archivo Black.
- **What is wrong:** the title's white pixels at 1.9 s span x 30–1058, so the margins are 30 px left and 22 px right. BRIEF „Technische Vorgaben“ requires content within 80 % title-safe, which is a 108 px margin on each side at 1080 px width. SPEC §1 mandates 150 px and does not mention horizontal safe area, so the two documents conflict.
- **Exact fix:** set `#s1-t1` font-size to 124 px (width scales to about 850 px, margins about 115 px each side). Keep the letter-spacing, timing and blur. Record in SPEC `## Änderungen`: „Fix-Runde 6, F2: Titel 124 px statt 150 px, damit die Zeile in der 80-%-Titelsicherheit liegt (BRIEF, Technische Vorgaben).“ Re-check one line at 0.5, 1.0 and 1.9 s.

### F3. 10.60–10.93 s, S3 Haustür, HUD label „HAUSTÜR“ covered by the stair figure's head: FAIL

- **Element:** HUD `#loc` („HAUSTÜR“, right 70, top 120, Inter 900 34 px) and the stick figure's head in `compositions/s4-flur.html` (`#s3-fig-hd`).
- **What is wrong:** at 10.7 s the figure starts on tread 0 (feet y 520, height 400), so its head top is at about y 120–170. It sits over the label's right letters (x about 895–1010, y 120–154). The HUD is on top and remains readable, but the figure head blocks part of the label. The brief says the HUD stays as it is.
- **Exact fix:** change the run so the head top is at or below y 170 during 10.60–10.93 s. Concretely, start the figure on tread 1 (feet y 610, head top 210) and add +90 px to each absolute `y` target of `#s3-fig-pos` from line 22 onward, then re-derive the landing y values for treads 2–8 (the `y` targets are absolute). Alternatively reduce the figure to H 340 (u 0.65) for S3 only. Record in SPEC §4.3 and `## Änderungen`. Re-snapshot 10.7 s and confirm the label is clear of the head.

### F4. 22.02–23.30 s, S6 Decke, ceiling print p6 hidden under caption C17 scrim: FAIL

- **Element:** `#s7-p6` (ceiling print, centre (430, 1120), W 80) in `compositions/s7-decke.html`, behind caption C17 „GENAU ÜBER“ (scrim top about y 1130).
- **What is wrong:** at 22.5 s the lower part of print p6 is under the caption scrim (`/tmp/hf/c5_p6_225.png`). The print looks dim and partly cut. Its lower edge (about 1187) is below the scrim top (about 1130).
- **Exact fix:** move p6 to centre (430, 1040) in `compositions/s7-decke.html` (its lower edge then lies at about 1107). Keep W, timing and colour. Record in SPEC §9.2 `## Änderungen`: „Fix-Runde 6, F4: p6 Mitte y 1040 (statt 1120), damit der Abdruck nicht unter der Untertitel-Lasche liegt.“ Re-snapshot 22.5 s.

### F5. 18.45–18.50 s, bed tail in `assets/sfx-bed.wav` vs SPEC §7 silence window: FAIL (minor, inaudible)

- **Element:** `assets/sfx-bed.wav`, fade-out and silence edit.
- **What is wrong:** SPEC §7 requires silence 18.45–19.60 s. Measured peaks: 18.40–18.45 s -35.0 dBFS, 18.45–18.50 s -48.5 dBFS (fade tail not reaching zero), 18.50–19.60 s -240 dBFS (true silence). The residual is about 50 ms at -48.5 dBFS. Hits are silent in the whole window.
- **Exact fix:** in the bed edit step, set all samples from 18.45 s to 19.60 s to zero (or fade 18.40–18.45 s to zero at 18.45 s). Re-run the peak check: 18.45–19.60 s must read -240 dBFS. The bed is an asset, so regenerate it with the bed-edit script, not by hand. No SPEC change needed.

---

## 7. NOT VERIFIED

| Item | Why |
|---|---|
| Visible count of 6 hallway flakes (BRIEF/user note) | Code defines 18 (`#s4-flk`). Flakes are 2–4 px and not reliably countable in the crop. |
| Voice loudness (−16 LUFS, true peak ≤ −1 dBTP) | Needs a render. Not run (per instructions). |
| Stair sync at 10.8 s and 11.0 s frames | Code-verified (landings 10.74 + 0.19k). Not snapshotted in this round. |
| Voice identity "Vincent Crowe" | Not checkable from the WAV. |

---

## 8. Summary

- **Check:** 0 errors, 0 warnings, 5 info (`container_overflow`). Clean per the tool, but the tool does not catch F1.
- **BRIEF criteria 1–8:** 6 PASS, 1 FAIL (criterion 5, via F3), 0 NOT VERIFIED. Technical 80 % title-safe rule: FAIL (F2).
- **SPEC checklist 1–22:** 19 PASS, 2 FAIL (items 8 and 19), 0 NOT VERIFIED.
- **Accepted deviations:** (a) S1 mirrored arm angles (hand on glass, verified); (b) 66 ms hit window at +4.5 dB (all 38 cues 4.25–4.73 dB, verified).
- **Audio:** all 38 cues in 3–6 dB. Silence 18.45–19.60 s has a 50 ms tail at -48.5 dBFS (F5).
- **FAIL items: 5.** F1 end-card overlap (29 s), F2 title width vs 80 % safe area (0–2 s), F3 HUD label covered by stair figure (10.6–10.9 s), F4 ceiling print p6 under caption (22.0–23.3 s), F5 bed tail (18.45–18.50 s).

**Recommendation:** NOT READY. Apply F1–F5 with the exact fixes above, record the changes in SPEC `## Änderungen`, then re-run `check --json`, the 19-time snapshot set, and the audio measurements. Do not render until the checks pass.
