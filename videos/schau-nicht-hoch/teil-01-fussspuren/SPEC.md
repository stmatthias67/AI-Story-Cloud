# SPEC: Teil 1 „Fußspuren im Schnee“ (Serie „Nacht 1“)

Blueprint for the builder. Every number here is binding unless a REVIEW.md entry changes it.
On-screen text is German. Technical notes are English. Source of truth for story and criticism: `BRIEF.md`.

## 0. Global

```text
GOAL:    the viewer sees footprints lead to their own door, hears the lock rattle, the crack, then
         footsteps above their head, and ends on a poll that asks whether to go upstairs.
OUTPUT:  HyperFrames 0.9.17, 1080 x 1920 px, 30 fps, 30.00 s = 900 frames.
TIME:    all times are absolute seconds on the root timeline (data-start / data-duration of scene hosts).
ENGINE:  GSAP from assets/gsap.min.js (local). No CDN. No Math.random. No fetch. No Date.
FONTS:   "Archivo Black" (titles, sign, badge, buttons); "Inter" weight 900 (HUD, captions, labels,
         hint, folge tag), Inter 700 (watermark). Both bundled. Do not use the glyph "✓" (U+2713):
         draw the check as an inline SVG polyline (stroke #ffffff, width 14, round caps).
COLOURS: ground #070b14 · ink #ffffff · accent #ffe14d (captions keyword, sign, folge tag) ·
         alert #ff3b3b (HUD bar, red button) · ok #1b8a4b (green button, badge) · snow #dfe8f5 ·
         print (footprint) #2f3d54 · night sky #0a1730 · wall #0c1424 · door #3b2a20.
         Defined as :root tokens; body background explicit.
SAFE:    text and product inside y 168–1330. Captions in y 1060–1300. HUD (existing, kept) sits at
         top 96–246 and bottom right 1514–1560 by design (see §0.1).
CAMERA:  one wrapper per scene named #cam-<scene>; camera moves are tweens on that wrapper only.
MOTION:  eases by role: arrival power3.out / expo.out; camera move power1.inOut; impact power4.out;
         hard shake steps linear; exit power2.in, 40–50 % shorter than the entrance.
```

### 0.1 HUD (kept from the current index.html, positions unchanged)

| Element | Position (px) | Style | Content |
|---|---|---|---|
| `#hud-tag` | left 70, top 96 | Inter 900 34 px, tracking 0.12 em, uppercase; red bar 8 x 42 #ff3b3b left of text | „NACHT 1“ |
| `#hud-clock` | left 70, top 150 | Inter 900 96 px, tracking -0.02 em; „UHR“ 34 px, opacity 0.7, margin-left 16 px | „03:12“ + „UHR“ |
| `#loc` | right 70, top 120 | Inter 900 34 px, tracking 0.12 em, uppercase, white, text-shadow 0 3px 14px rgba(0,0,0,0.9) | scene label (table §0.2) |
| `#watermark` | right 70, bottom 360 (box ends y 1560) | Inter 700 34 px, bg rgba(7,11,20,0.7), radius 10, padding 6 px 16 px | „@deinhandle“ |

HUD is on track 2 (top of every scene, z-index 900 to 903). It never fades. Clock never changes.

### 0.2 Scene list (absolute seconds)

| Scene | Start | End | HUD label (#loc) | Captions in scene | Hard-cut / transition in |
|---|---|---|---|---|---|
| S0 Titel | 0.00 | 2.00 | „Draußen“ | none | film start |
| S1 Schlafzimmer | 2.00 | 6.30 | „Schlafzimmer“ | C1–C5 region: C1, C2, C3, C4 starts 5.25 (see §5) | cut from title (0.00–0.20 s fade of title only) |
| S2 Hof | 6.30 | 10.60 | „Hof“ | C5–C8 | window zoom-through 6.30–6.80 (§2.6) |
| S3 Haustür | 10.60 | 13.60 | „Haustür“ | C9, C10 | dip cut at 10.60 (§3.1) |
| S4 Schloss | 13.60 | 16.70 | „Schloss“ | C11, C12 | hard cut at 13.60 on the knob’s rattle peak |
| S5 Treppenhaus | 16.70 | 19.10 | „Treppenhaus“ | C13, C14 | hard cut at 16.70 |
| S6 Decke | 19.10 | 25.50 | „Decke“ | C15–C18 | hard cut at 19.10 |
| S7 Abspann | 25.50 | 30.00 | „Umfrage“ | none | dip cut at 25.50 (3 frames at 40 %) |

Layer order inside every scene (bottom to top, CSS z-index):
1 background (sky / wall / floor) · 2 far architecture (houses, fence, stairs, door) · 3 ground props (cars, lamp, sill) · 4 snow prints · 5 stick figure · 6 foreground props (curtain, pendant lamp, lock plate) · 7 effects (crack, flash, vignette) · 8 snowflakes (fixed) · 9 scene text (title, sign, badge, poll) · 10 captions (scrim + text) · 11 HUD · 12 watermark.

### 0.3 Snowflakes (all scenes except S4, fixed positions, deterministic)

`for i in 0..17: x = (i*397 + 61) % 1080; y = (i*613 + 97) % 1920; r = 2 + (i % 3)` px, fill #dfe8f5, opacity 0.85.
Each scene moves them down: y += 220 px linear over the scene's duration (no loop, no random).

### 0.4 Stick figure rig (used in S1, S3, S5, S6)

Unit u = H / 520, where H is the figure's height from feet to top of head.
Parts (white #ffffff, limbs stroke-width 10u, round caps; head = filled circle, no face):

| Part | Length (px at u = 1) | Pivot | Notes |
|---|---|---|---|
| head | r 40 | neck top | centre sits 14 u + 40 u above shoulder |
| torso | 180 | hip → shoulder (neck base) | pivot at hip |
| upper arm | 110 | shoulder | near arm drawn in front |
| forearm | 100 | elbow | |
| thigh | 140 | hip | |
| shin | 140 | knee | |
| foot | 20 | ankle | horizontal stroke pointing toward the figure’s facing direction |

Facing: right for S1, S3, S5 (toward the window / door / stairs); facing up for S6 (figure looks at the ceiling).
Poses are given as rotations in degrees (positive = clockwise in screen space), relative to the parent part.

---

## 1. S0 Titel (0.00–2.00)

Only the title card. No narrative text on screen.

**Objects (9):** night sky (flat #0a1730 full frame, top 0–1240), moon (disc #dfe8f5 centre (830, 300), r 70, flat, no glow), six house silhouettes (#05080f) at y 1100–1240 with widths 120, 150, 110, 170, 130, 160 starting at x 0, 130, 290, 410, 590, 730 (roofs flat), snow ground (#1b2a44 y 1240–1920), 18 snowflakes (§0.3), title line 1, title line 2.

**Text:**
- Line 1 „FUSSSPUREN“: Archivo Black 150 px, white, centre x 540, y 720–880 (7.8 % of height). Letter entrance: per letter 0.10 s apart, opacity 0.3 → 1 and blur 4 px → 0, 0.13 s each, power2.out, starts at 0.00. Letters land by 0.90 s, then hold dead still until 2.00.
- Line 2 „IM SCHNEE“: Archivo Black 96 px, accent #ffe14d, centre x 540, y 900–990. Entrance: whole line blur 8 px → 0 and opacity 0 → 1 in 0.20 s, start 0.60 s.

**Motion:** only the snowflakes fall (§0.3). No camera move. No caption. HUD visible from 0.00.
**Light/colour:** cold night blue; no light source.
**Sound:** wind bed only (see §7).
**Frame 0:** title already at ≥ 30 % opacity (not black).

---

## 2. S1 Schlafzimmer (2.00–6.30)

Interior bedroom, figure stands at the window and looks out at the yard.

**Camera:** #cam-S1 scale 1.00 → 1.04 from 2.00 to 6.30, power1.inOut (slow push in, early in the scene, ends at the window zoom).

### 2.1 Objects with coordinates (1080 x 1920 space)

| # | Object | Coordinates (x, y, w, h in px) | Style |
|---|---|---|---|
| 1 | wall | 0,0 1080x1180 | #0c1424 |
| 2 | floor | 0,1180 1080x740 | #2b1f19 with planks: lines at y 1320, 1480, 1660 (stroke 4, #22170f) |
| 3 | window frame (outer) | 360,300 580x700 | #1b2538, border 26 px |
| 4 | window glass | 386,326 528x648 (x 386–914, y 326–974) | sky #0a1224 0–60 %, #1a2740 at 60 % |
| 5 | yard in glass | 386,860 528x114 | snow #c9d6ea |
| 6 | mullion | 642,326 16x648 | #1b2538 |
| 7 | transom | 386,640 528x14 | #1b2538 |
| 8 | neighbour house A | 420,400 180x210 | #131f35; lit windows #e8b84a at 80 %: (440,430,40,40), (500,430,40,40), (440,500,40,40), (500,500,40,40) |
| 9 | neighbour house B | 700,380 220x180 | #101a2c; lit windows (760,420,44,44), (840,470,44,44) |
| 10 | street lamp | pole 820,520 10x380; head 806,500 38x20 | pole #0b1424; head #ffe14d |
| 11 | parked car 1 under snow | 430,830 190x50 | snow mound #dfe8f5, radius 24 on top |
| 12 | parked car 2 under snow | 700,840 200x50 | snow mound #dfe8f5 |
| 13 | fence | 386,820 528x50; 8 posts 10x56 at x 400, 460, 520, 580, 640, 700, 760, 820 | #0b1424 |
| 14 | window sill | 340,1000 600x40 | #1b2538, shadow strip 1040–1048 at 40 % black |
| 15 | curtain (right) | 960,260 90x920 | #3a2a3f, three folds: rects 960–978, 1000–1018, 1030–1048 at 35 % black |
| 16 | bed edge (left) | 0,1080 240x220 | blanket #2b2140; pillow #dfe8f5 at 20 % opacity (40,1080,160,60) |
| 17 | stick figure | see §2.2 | white |
| 18 | snowflakes | §0.3 | |

Object count: 18 (requirement ≥ 8).

### 2.2 Stick figure (H = 520, u = 1, facing right)

Feet (300, 1300). Hip (300, 1020). Shoulder (300, 840). Neck top 826. Head centre (300, 786), r 40.

Beats (times absolute):
- 2.00–3.00: idle, torso rotates ±1.5° about hip, sine.inOut, period 2.0 s. Arms hang (upper arm 0°, forearm 0°).
- 3.00–3.40: head turns toward the window: neck rotation 0° → -12° (power2.out, 0.40 s). Body stays still.
- 3.40–4.20: near arm (left arm, the one nearer the window) raises to the glass: upper arm 0° → 70° (toward window), forearm 0° → -35° (expo.out, 0.80 s). Hand ends at (460, 960), touching the glass at its lower edge.
- 4.20–5.20: hold, hand flat on glass; head tilts to -18° (stays).
- 5.20–6.30: slow breathing only (torso ±1°, 2.0 s period). Right arm remains hanging.
- Legs: straight throughout (thigh 0°, shin 0°, foot horizontal).

### 2.3 Light and colour

Cold blue ambient (#0c1424 to #1a2740). The only warm light: three lit neighbour windows (#e8b84a at 80 %) and the lamp head (#ffe14d). No glow, no bloom.

### 2.4 Captions in S1

C1 2.00–3.28, C2 3.30–3.95, C3 4.00–4.67 (see §5).

### 2.5 Titles / prints

No footprints in S1. The window glass shows no prints (checklist item 2).

### 2.6 Transition to S2 (6.30–6.80)

Window zoom-through. The window frame group (objects 3–7) scales 1.00 → 3.20 about (650, 650), power3.in, 0.50 s, from 6.30 to 6.80. At 6.30 the S2 layer is already underneath, so the glass opening reveals the yard. Frame is fully off-frame at 6.80.

---

## 3. S2 Hof, Blick aus dem Fenster nach unten (6.30–10.60)

The camera is now outside, above the yard, looking down toward the viewer’s front door at the bottom of the frame. Footprints run from the gate (far, top) to the door (near, bottom). Prints get bigger toward the viewer.

**Camera:** the yard layer #yard translates y 0 → -60 px from 6.80 to 10.60, power1.inOut (slow down-pan). Scene-wide layers stay in place.

### 3.1 Objects with coordinates

| # | Object | Coordinates (x, y, w, h) | Style |
|---|---|---|---|
| 1 | neighbour house facade | 0,0 1080x600 | #101a2c |
| 2 | neighbour windows lit | (120,200,70,60), (300,200,70,60), (520,240,70,60), (760,200,70,60), (900,260,60,60) | #e8b84a at 80 % |
| 3 | lamp pole | 900,470 12x530 | #0b1424 |
| 4 | lamp head | 884,450 46x22 | #ffe14d |
| 5 | fence (far) | 0,600 1080x60; 12 posts 10x90 at x 30, 120, 210, 390, 480, 570, 660, 750, 840, 930, 1020 (skip 300–380 gate gap) | #0b1424 |
| 6 | gate posts | 296,590 10x110 and 384,590 10x110 | #0b1424 |
| 7 | snow yard | 0,660 1080x510 | #c9d6ea, with lighter patches #dfe8f5 (rects 60,700 220x40; 700,760 260x60) |
| 8 | parked car 1 (snow) | 40,760 260x120 | body #3a4660; snow mound #dfe8f5 over top half |
| 9 | parked car 2 (snow) | 760,900 280x120 | body #3a4660; snow mound #dfe8f5 |
| 10 | house front wall | 0,1170 1080x750 | #1a1820 |
| 11 | front door | 480,1200 120x360 | #2a1d17, panels 500–580 at y 1230–1400 and 1420–1540 (#22170f), peephole circle (540,1260) r 8 #e8b84a |
| 12 | stoop | 440,1170 200x30 | #6f7f96 |
| 13 | footprints 0–9 | §3.2 | #2f3d54 at opacity 0.9 |
| 14 | stick figure | none in S2 | |
| 15 | snowflakes | §0.3 | |

Object count: 12 categories plus 10 prints (≥ 8).

### 3.2 Footprint layout (exact)

Symbol: the `fp` symbol (viewBox 60 x 100: ball ellipse at (30,34), heel ellipse at (30,74), five toe circles at top). Each print is drawn at width W with height H = 1.67 W, rotated 180° so the toes point to the door. Put the SVG `left = x - W/2`, `top = y - 0.835 W`, `width = W`, `height = 1.67 W`. Alternate rotation 174° / 186° for stride splay (left foot 174°, right foot 186°).

| k | centre x | centre y | W (px) | Foot | Appears at (s) |
|---|---|---|---|---|---|
| 0 | 312 | 700 | 25 | left | 6.40 |
| 1 | 371 | 750 | 28 | right | 6.82 |
| 2 | 359 | 800 | 32 | left | 7.24 |
| 3 | 418 | 850 | 35 | right | 7.66 |
| 4 | 405 | 900 | 39 | left | 8.08 |
| 5 | 465 | 950 | 42 | right | 8.50 |
| 6 | 452 | 1000 | 46 | left | 8.92 |
| 7 | 511 | 1050 | 49 | right | 9.34 |
| 8 | 499 | 1100 | 53 | left | 9.76 |
| 9 | 558 | 1150 | 56 | right | 10.18 |

Rules: all prints are on the snow (y 700–1150, inside #yard), all between the gate posts and the door, path runs from the gate (x 296–384, y 590–700) to the door threshold (stoop at y 1170). None on the window glass (window is not in S2 and S1 has no prints). Prints increase in size as they approach the viewer.

Print entrance (each k): scaleY 0.6 → 1.0 and opacity 0 → 0.9 in 0.12 s, power2.out, at the listed time. The print does not move afterward. Pressed-in look: fill #2f3d54, plus a 2 px lighter rim stroke #6f7f96 on the lower edge.

### 3.3 Figure in S2

None. The viewer is above the yard; the prints carry the scene.

### 3.4 Light and colour

Cold blue ambient, snow #c9d6ea. Lamp head #ffe14d (flat). Captions over snow need the scrim (§5.2).

---

## 4. S3 Haustür von innen (10.60–13.60)

The hall, inside the front door. Door in the middle, staircase at the right, figure runs down the stairs then walks to the door and checks the lock.

**Camera:** #cam-S3 scale 1.00 → 1.05 from 10.60 to 13.60, power1.in (slow push). Each step adds a 2 px hit shake (§7).

**Entrance:** dip cut at 10.60: the outgoing frame darkens to 60 % brightness over 3 frames (0.10 s), then hard cut to S3.

### 4.1 Objects with coordinates

| # | Object | Coordinates (x, y, w, h) | Style |
|---|---|---|---|
| 1 | hall wall | 0,0 1080x1340 | #17120e |
| 2 | floor | 0,1340 1080x580 | #2a1d17; planks at y 1500, 1680 (stroke 4 #22170f) |
| 3 | door frame | 232,242 616x1116 | #140d0a (border 18 inside) |
| 4 | door leaf | 250,260 580x1080 | #3b2a20 |
| 5 | upper panel | 300,330 480x400 | #2c1f18 |
| 6 | lower panel | 300,770 480x480 | #2c1f18 |
| 7 | pane (sidelight) | 340,350 100x100 | glass #1b2a44; snow in lower third (y 430–450, #c9d6ea) with three prints (see 4.2) |
| 8 | lock escutcheon | 640,840 100x130 | #c9ced8, radius 10 |
| 9 | knob | circle (690,880) r 34 | #e2e6ee; highlight arc white 30 % |
| 10 | stair treads | 9 treads j = 0–8: x from 1080 - 22.2·j to 1080, y from 520 + 90·j to y + 14 | #1a2232, top edge #2c3a52 (6 px) |
| 11 | stair risers | under each tread: 90 - 14 = 76 px tall, same x span, #120e18 | |
| 12 | stair rail | polyline from (1040, 480) to (1040, 1310) with posts every 90 px | #2c3a52, 6 px |
| 13 | stick figure | §4.2 | white |
| 14 | door frame light (wall lamp) | 40,640 50x90 | #ffe14d at 70 % (flat) |

Object count: 14 (≥ 8).

Stair geometry: tread j has left edge x_j = 1080 - 22.2·j, top y_j = 520 + 90·j. j = 8: x 902, y 1240. Floor at y 1340 (figure reaches floor at (880, 1340)).

### 4.2 Pane prints (inside the sidelight, on snow, not on glass)

Three prints at (366, 436, W 14), (392, 442, W 16), (418, 438, W 18), fill #2f3d54, toes down. Visible only inside the pane.

### 4.3 Stick figure (H = 400, u = 400/520 = 0.769, facing right)

Feet on tread j: feet x = x_j - 40, y = y_j (the figure stands on the tread’s top edge). Floor feet (880, 1340) then (760, 1340).
Thigh 108 px, shin 108 px, torso 138 px, head r 31, upper arm 85 px, forearm 77 px.

Beats (absolute):
- 10.60–12.07: run down the stairs, 9 steps, one step every 0.19 s (feet touch at 10.55 + 0.19 j, j = 0…8; see §7). Per step: torso lean forward 12° (constant), hip rotates ±28° alternating (thigh from +28° to -28°), knee bends 0 → 40° at mid-air (shin rotation), arms swing ±35° at the shoulder, opposite to the legs. Figure translates diagonally down-left by the tread offset; the drawing lands on the tread every 0.19 s.
- 12.07–12.60: at the floor, walk-run to the left: thigh ±20°, shin ±12°, torso 6° lean. Feet at (880, 1340) → (760, 1340), power2.out, duration 0.53 s.
- 12.60–12.90: slow to stop: torso rotates back to 0° (0.30 s, power2.out), feet at x 760.
- 12.90–13.60: right arm (near arm) raises to the lock: upper arm 0° → -60° (toward the door), forearm 0° → -65° (expo.out, 0.50 s). Hand reaches the knob at (690, 880). Head turns to face the door: neck rotation -15°.
- 13.70–14.30: hand rattles the knob: knob rotation ±10° at 6 Hz (sine); figure torso bobs ±1.5°.
- 14.30–14.60: arm returns down (reverse of 12.90–13.60 at power2.in). Not visible after 13.60 (S4 starts), so the arm goes to S4 instead.

### 4.4 Light and colour

Warm interior: door panels #3b2a20, wall #17120e; wall lamp #ffe14d at 70 % (flat). No glow.

---

## 5. Captions

### 5.1 Caption table (complete)

Group rules: 2–4 words per group. Exceptions allowed only for single-word segments (C11, C16): one word. One group visible at a time (no overlap, minimum gap 0.02 s). Yellow keyword is one word per group (class `.k`, #ffe14d). All text uppercase, German. Anchor times from BRIEF.md (±0.15 s). Words inside a segment are split by proportional time, so each group is within its segment.

| # | Start | End | Text | Yellow | Segment (BRIEF) |
|---|---|---|---|---|---|
| C1 | 2.00 | 3.28 | MITTEN IN DER NACHT | NACHT | 1 (2.02–4.65) |
| C2 | 3.30 | 3.95 | SCHAUE ICH AUS | AUS | 1 |
| C3 | 4.00 | 4.67 | DEM FENSTER. | FENSTER | 1 |
| C4 | 5.25 | 6.30 | IM FRISCHEN SCHNEE: FUSSSPUREN | FUSSSPUREN | 2 (5.27–6.28) |
| C5 | 6.72 | 7.22 | SIE FÜHREN NICHT | NICHT | 3 (6.75–7.68) |
| C6 | 7.25 | 7.72 | VOM HAUS WEG. | WEG | 3 |
| C7 | 8.30 | 8.95 | SIE FÜHREN DIREKT | DIREKT | 4 (8.32–10.03) |
| C8 | 9.00 | 10.07 | AUF MEINE TÜR ZU. | TÜR | 4 |
| C9 | 10.50 | 11.25 | ICH LAUFE RUNTER. | RUNTER | 5 (10.52–12.91) |
| C10 | 11.30 | 12.95 | ICH PRÜFE DAS SCHLOSS. | SCHLOSS | 5 |
| C11 | 13.55 | 14.52 | VERRIEGELT. | VERRIEGELT | 6 (13.58–14.51), one-word exception |
| C12 | 15.00 | 16.20 | ALLES ZU. | ZU | 7 (15.02–16.17) |
| C13 | 16.70 | 17.42 | DANN KNACKT ES. | KNACKT | 8 (16.72–17.40) |
| C14 | 17.75 | 18.47 | IM ZWEITEN STOCK. | STOCK | 9 (17.77–18.45) |
| C15 | 19.10 | 20.20 | UND DANN… | DANN | 10 (19.14–20.19) |
| C16 | 20.54 | 21.54 | SCHRITTE. | SCHRITTE | 11 (20.56–21.52), one-word exception |
| C17 | 21.91 | 23.30 | GENAU ÜBER | ÜBER | 12 (21.93–25.40), part 1 |
| C18 | 23.35 | 25.42 | MEINEM KOPF. | KOPF | 12, part 2 |

Gaps between consecutive groups: C1→C2 0.02, C2→C3 0.05, C3→C4 0.00 (not adjacent in time, C4 is at 5.25), C5→C6 0.03, C6→C7 0.58, C7→C8 0.05, C8→C9 0.43, C9→C10 0.05, C10→C11 0.60, C11→C12 0.48, C12→C13 0.50, C13→C14 0.33, C14→C15 0.63, C15→C16 0.34, C16→C17 0.37, C17→C18 0.05. No overlaps.

### 5.2 Caption build

- One host `#captions` with `data-track-kind="captions"`, full-frame absolute, z-index 10.
- Each group `.cap` absolute, left 50 px, width 980 px, text-align center, container bottom at y 1300 (top set so the text baseline ends at 1300). Font Inter 900, uppercase, `fitTextFontSize(text, { fontFamily: "Inter", fontWeight: 900, maxWidth: 960 })`, minimum 72 px, base 98 px, max 2 lines.
- Scrim: inline-block span behind the text, background rgba(7,11,20,0.55), padding 6 px 22 px, radius 6 px. Required on S2 (snow yard), S5 (light wall), S6 (ceiling). Optional elsewhere but apply everywhere for consistency. No full-width bar.
- Fade in 0.12 s from group start (opacity 0 → 1), fade out 0.12 s before group end (1 → 0), then hard kill `tl.set(group, {opacity: 0, visibility: "hidden"}, end)`.
- No text-shadow on the caption text itself beyond 0 6 px 24 px rgba(0,0,0,0.85) (not a glow; a shadow).

---

## 6. S4 Schloss (13.60–16.70)

Close-up of the lock. Hard cut in at 13.60. Figure’s arm enters from the left edge.

**Camera:** fixed. During the rattle (13.70–14.30) the whole scene shakes ±3 px at 6 Hz (sine, not random).

### 6.1 Objects with coordinates

| # | Object | Coordinates (x, y, w, h) | Style |
|---|---|---|---|
| 1 | door background | full frame #3b2a20 | |
| 2 | planks | vertical lines at x 216, 432, 648, 864 (stroke 6, #2a1d17) | |
| 3 | lock plate | 340,620 400x400, radius 24 | #3a3f48 |
| 4 | rivets | circles r 8 at (370,650), (710,650), (370,990), (710,990) | #22262d |
| 5 | knob | circle (540,820) r 92 | #c9ced8; inner circle r 60 #9aa1ad; highlight arc |
| 6 | deadbolt | 340,1080 400x80, radius 12 | #8a909c; slot 540–560 x 1100–1140 #22262d |
| 7 | jamb | 760,1080 40x160 | #05070c |
| 8 | badge | 60,300 960x140, radius 14, bg #1b8a4b | text „VERRIEGELT“ Archivo Black 84 px white + SVG check (white stroke 14, points (900,335)(920,360)(960,320)? see 6.3) |
| 9 | figure arm + hand | shoulder off-screen at (-60, 1000); upper arm 0° → ends at (240, 860); forearm ends at (440, 820) | white, stroke 22 px |
| 10 | door planks shadow | 0,0 1080x1920 gradient-free: #000 at 25 % where planks meet | |

Object count: 9 (≥ 8). Badge sits at y 300–440, inside the safe band and above the captions.

### 6.2 Motion beats

- 13.60–13.70: camera at rest, lock still.
- 13.70–14.30: knob rotates ±10° at 6 Hz (sine); arm follows, forearm rotates ±4°; whole frame shakes ±3 px.
- 14.52: C11 ends. Badge enters at 14.55: scale 1.20 → 1.00 and opacity 0 → 1 in 0.20 s, power3.out. Check mark draws on (stroke-dashoffset 40 → 0 in 0.20 s, starts 14.70).
- 15.00: C12 starts.
- 15.20–15.45: deadbolt slides right 0 → 60 px into the jamb (power3.out, 0.25 s). Ends blocked by the jamb.
- 15.50: lock snap: a 3 px flash on the deadbolt slot (opacity 0 → 1 → 0 in 0.10 s). Sound cue §7.
- 15.50–16.70: hold still. Badge stays until 16.70 (1.15 s after entry, satisfies ≥ 0.8 s).

### 6.3 Check mark

Inline SVG 64 x 64 at (900, 320): polyline points 12,34 26,48 52,16 (stroke #ffffff, stroke-width 14, round caps, fill none).

---

## 7. Sound (clock = voice; bed and hits)

Audio assets:
- Voice: `assets/voice-timed.wav` (narration starts 2.02 s; voice gain 1.00).
- Bed: `assets/sfx.wav` (wind, 30 s stereo 48 kHz). Required edit before mixing: silence 18.45–19.60 s (fade out 18.40–18.45, silent until 19.60, fade in 19.60–19.65). That removes the existing big impact that does not match the picture. Bed gain 0.45 (about -7 dB) during 0–18.4 and 19.6–25.4. Fade bed to 0 from 25.40 to 25.90. Silent after 25.90.
- Hits: `assets/hits.wav`, generated by a stdlib-only Python script (no `random` module; noise from a fixed LFSR, seed 0xACE1). The script must write 48 kHz stereo, 30 s, same length as the bed. Hits are described below.

Hit types (synthesis, all deterministic):
- snow crunch: 60 ms burst of band-passed noise 1.5–4 kHz, decay 0.08 s, gain -16 dB.
- stair step: 40 ms noise transient + sine 110 Hz decaying 0.12 s, gain -10 dB.
- door thump: sine 70 Hz decaying 0.30 s + noise 0.04 s, gain -6 dB.
- lock rattle click: 25 ms noise transient + sine 1800 Hz decaying 0.02 s, gain -12 dB.
- crack: 250 ms broadband noise, decay 0.20 s, with a 10 ms attack, gain -3 dB.
- rumble: sine 45 Hz decaying 0.80 s, gain -6 dB.
- ceiling thump: sine 70 Hz decaying 0.35 s + noise 0.03 s, gain -4 dB.

Cue list (times in seconds; hits.wav unless noted):

| Time | Sound | Matches picture |
|---|---|---|
| 0.00–2.00 | bed only (wind, gain 0.45) | title card |
| 2.02–25.40 | voice-timed.wav (narration) | S1 to S6 captions |
| 6.40, 6.82, 7.24, 7.66, 8.08, 8.50, 8.92, 9.34, 9.76, 10.18 | snow crunch ×10 | prints k 0–9 |
| 10.55, 10.74, 10.93, 11.12, 11.31, 11.50, 11.69, 11.88, 12.07 | stair step ×9 | figure feet touch treads j 0–8 |
| 12.26, 12.42, 12.58 | floor step ×3 (lighter, gain -13 dB) | walk to the door |
| 12.90 | door thump (heavy) | arrival at the door |
| 13.70, 13.80, 13.90, 14.00, 14.10, 14.20, 14.30 | lock rattle click ×7 | rattle beats §6.2 |
| 15.50 | sfx.wav original blip (keep, gain 0.9) | deadbolt snap |
| 16.95 | crack | crack in wall, red flash |
| 17.10 | rumble | ground shake, S5 |
| 20.62, 20.90, 21.18, 21.46, 21.74, 22.02 | ceiling thump ×6 | ceiling prints p1–p6 |

Hit peaks: each hit lands on its picture start, peaks one frame later (33 ms) per the sound reference. Every hit is 3–6 dB above the bed at its time.
Levels: voice -16 LUFS integrated target; bed and hits below voice. True peak ≤ -1 dBTP. Run `npx hyperframes audio <video> --json` after render to check hits and loudness.

---

## 8. S5 Treppenhaus (16.70–19.10)

Staircase going up, seen from the bottom. Thirteen treads. Landing with sign „2. OG“. A crack appears in the right wall, red flash, shake, figure flinches.

**Camera:** shake starts at 16.95 and decays over 0.35 s. Keyframes (x, y in px, each 0.05 s): (+8,-5), (-8,+4), (+6,-3), (-4,+2), (+2,-1), (0,0). Shake is a fixed table, not random.

### 8.1 Stair geometry (exact)

Vanishing point (540, 700). Tread i (i = 0 … 12): half width hw_i = 380 / (1 + 0.2 i); tread top y = 700 + 1000 / (1 + 0.2(i+1)); tread bottom y = 700 + 1000 / (1 + 0.2 i).

| i | x left | x right | top y | bottom y | height |
|---|---|---|---|---|---|
| 0 | 160 | 920 | 1533 | 1700 | 167 |
| 1 | 223 | 857 | 1414 | 1533 | 119 |
| 2 | 269 | 811 | 1325 | 1414 | 89 |
| 3 | 303 | 777 | 1256 | 1325 | 69 |
| 4 | 329 | 751 | 1200 | 1256 | 56 |
| 5 | 350 | 730 | 1155 | 1200 | 45 |
| 6 | 367 | 713 | 1117 | 1155 | 38 |
| 7 | 382 | 698 | 1085 | 1117 | 32 |
| 8 | 394 | 686 | 1057 | 1085 | 28 |
| 9 | 404 | 676 | 1033 | 1057 | 24 |
| 10 | 413 | 667 | 1012 | 1033 | 21 |
| 11 | 421 | 659 | 994 | 1012 | 18 |
| 12 | 428 | 652 | 978 | 994 | 16 |

Each tread: rect (x left, top y) to (x right, bottom y), fill #1a2232, top edge 6 px #2c3a52. Risers: the 2 px line at the bottom of each tread, #05070c.

Landing: rect 310,880 460x98 (y 880–978), #1f2838. Behind it the upper hall: rect 360,740 360x140 (y 740–880), #05070c.
Sign „2. OG“: rect 380,640 320x80, bg #ffe14d, radius 12, Archivo Black 72 px, #111111, centred. Sign sits above the upper hall.

Railings: left rail = polyline through the tops of posts at (160, 1550), (329, 1100), (394, 990), (428, 950) (post height 150 · scale, scale = 1/(1+0.2i)). Right rail mirrors: (920, 1550), (751, 1100), (686, 990), (652, 950). Posts at each tread's outer x, 5 px wide.

Walls: left wall polygon (0,0) (160,700) (160,1700) (0,1920) fill #0e1220. Right wall polygon (1080,0) (920,700) (920,1700) (1080,1920) fill #0e1220.
Left wall lamp: 40,1140 50x60, #ffe14d at 70 %.
Crack (right wall, appears 16.95): polyline (960,1040) (985,1120) (950,1200) (1000,1290) (975,1400), stroke #000000 4 px; branches (985,1120)→(1030,1080) and (950,1200)→(915,1240) stroke 3 px. Draw-on: stroke-dashoffset from full length to 0 in 0.12 s, power2.out, starts 16.95.

Flash: full-frame rect #ff3b3b, opacity 0.55 → 0 over 16.95–17.30 (power2.in). Second flash none.

### 8.2 Stick figure (H = 390, u = 0.75, facing up the stairs, body facing right)

Feet (540, 1690). Hip (540, 1480). Shoulder (540, 1345). Neck top 1334. Head centre (540, 1293), r 30.
Thigh 105, shin 105, torso 135, upper arm 83, forearm 75.

Beats:
- 16.70–16.90: still; head rotates 0° → +14° (look up toward the landing), power2.out 0.2 s.
- 16.95–17.05: flinch: torso leans back 8° (power4.out, 0.10 s).
- 17.05–17.60: sway, damped: torso rotates +3°, -3°, +2°, -1° at 0.13 s half-periods (sine decaying).
- 17.60–17.80: returns to rest (torso 0°, head 0°).
- 17.77–18.20: head turns up toward the landing: neck -20°, power2.out.
- 18.20–19.10: hold, slow breathing (torso ±1°, 2.0 s period).
- Arms: hang, then 17.05 both arms rise slightly (upper arm -18°) and return at 17.60.

### 8.3 Light and colour

Dark stairwell #0e1220 walls, #1a2232 treads, one warm light: the sign (#ffe14d) and the left wall lamp at 70 %. Red flash only at 16.95–17.30.

### 8.4 Objects count (≥ 8)

13 treads, 2 rails, sign, landing, upper hall, crack, two walls, left wall lamp, figure = 22 objects.

---

## 9. S6 Decke (19.10–25.50)

Ceiling view. The figure stands at the bottom-left and looks up. Footprints appear on the ceiling, upside down, one thump at a time. The pendant lamp swings. Red pulse with each thump.

**Camera:** none. Pendant lamp swings with a decaying sine (amplitude 4° at 20.62, adds 2° per thump, decays with time constant 1.2 s).

### 9.1 Objects with coordinates

| # | Object | Coordinates (x, y, w, h) | Style |
|---|---|---|---|
| 1 | ceiling | full frame | #14101a |
| 2 | beam A | 0,280 1080x60 | #0e0a14, top edge #2a2036 (4 px) |
| 3 | beam B | 0,1400 1080x60 | #0e0a14, top edge #2a2036 |
| 4 | pendant cord | 536,0 8x420 | #2a2036 |
| 5 | pendant shade | polygon (470,420) (610,420) (580,470) (500,470) | #3a2f22 |
| 6 | pendant bulb | circle (540,490) r 20 | #ffe14d, flat |
| 7 | ceiling prints p1–p6 | §9.2 | #05070c at 85 %, upside down (rot 0°) |
| 8 | red pulse | full-frame inset box-shadow overlay `inset 0 0 260px 120px rgba(255,59,59,0.45)` | opacity 0 → 0.8 → 0 per thump, 0.25 s |
| 9 | stick figure | §9.3 | white |
| 10 | snowflakes | §0.3 (none fall in S6 except as set; keep them static, drift 220 px) | |
| 11 | wall corner | 0,1500 120x420 | #0e0a14 (the house wall in shadow) |

Object count: 11 (≥ 8).

### 9.2 Ceiling prints (exact)

Printed as ceiling marks: same symbol, rot 0° (toes point up = upside down relative to floor prints), colour #05070c at 85 %. Size W and centre:

| p | centre x | centre y | W | appears at |
|---|---|---|---|---|
| p1 | 260 | 600 | 40 | 20.62 |
| p2 | 330 | 700 | 46 | 20.90 |
| p3 | 300 | 800 | 54 | 21.18 |
| p4 | 380 | 900 | 62 | 21.46 |
| p5 | 350 | 1010 | 70 | 21.74 |
| p6 | 430 | 1120 | 80 | 22.02 |

Entrance per print: scale 1.25 → 1.00 (power4.out, 0.10 s) and opacity 0 → 0.85 in 0.08 s. Each entrance is paired with a red pulse (§9.4) and a ceiling thump (§7).

### 9.3 Stick figure (H = 380, u = 0.73, looking up)

Feet (200, 1760). Hip (200, 1556). Shoulder (200, 1425). Neck top 1415. Head centre (200, 1386), r 29. Thigh 102, shin 102, torso 131, upper arm 80, forearm 73. Figure faces the ceiling: neck -20° (head turned up) at rest.

Beats:
- 19.10–19.80: head tilts up 0° → -20° (power2.out 0.7 s).
- 19.80–20.50: hold, breathing ±1° on torso (2.0 s period).
- 20.62–21.80: at each thump (20.62, 20.90, 21.18, 21.46, 21.74): knee dip (both shins rotate +6°, power4.out 0.08 s, then return 0.15 s) and shoulders shake ±2 px. Arms hang.
- 22.02–25.50: head holds at -20°, shoulders still. No further motion (the figure is the one thing that does not move in the last 3.5 s).

### 9.4 Red pulse timing

Pulse at each thump: 20.62, 20.90, 21.18, 21.46, 21.74, 22.02, each 0.25 s, opacity 0 → 0.8 (power2.out 0.08 s) → 0 (power2.in 0.17 s). Overlap-free.

### 9.5 Light and colour

Cold dark ceiling #14101a, beams #0e0a14, pendant bulb warm flat (#ffe14d), red pulses only. Captions C15–C18 with scrim.

---

## 10. S7 Abspann (25.50–30.00)

Poll and end card. Silence (no voice, no hits; bed fades out by 25.90).

**Camera:** none. Dip cut in at 25.50 (3 frames at 40 %).

### 10.1 Objects with coordinates

| # | Object | Coordinates (x, y, w, h) | Style |
|---|---|---|---|
| 1 | background | full frame #0d0f16 | |
| 2 | door-frame left | 0,0 36x1920 | #161a24 |
| 3 | door-frame right | 1044,0 36x1920 | #161a24 |
| 4 | question line 1 „GEHST DU“ | centre x 540, y 600–720 | Archivo Black 112 px, white, uppercase |
| 5 | question line 2 „NACH OBEN?“ | centre x 540, y 720–840 | same |
| 6 | red button „NACHSCHAUEN“ | 130,920 820x150, radius 16 | bg #ff3b3b, Archivo Black 72 px, white, centred |
| 7 | green button „LIEBER NICHT“ | 130,1110 820x150, radius 16 | bg #1b8a4b, same text style |
| 8 | hint „STIMM IN DEN KOMMENTAREN AB“ | left 60, width 960, y 1300–1340 | Inter 900 40 px, tracking 0.04 em, #dfe8f5, centred |
| 9 | folge tag „FOLGE FÜR TEIL 2“ | 140,1440 700x84, radius 10 | bg #ffe14d, text #111111, Inter 900 44 px, tracking 0.06 em |
| 10–15 | six snowflakes | §0.3 for i = 0…5, r 2–4 | #dfe8f5 |

Object count: 15 (≥ 8). The folge tag stays within x 140–840, away from the watermark (x 900–1010, y 1514–1560).

### 10.2 Timing (absolute)

| Element | In | Out | Visible at least |
|---|---|---|---|
| question (both lines) | 25.50 | 30.00 | 4.50 s |
| red button | 26.10 | 30.00 | 3.90 s |
| green button | 26.30 | 30.00 | 3.70 s |
| hint | 26.80 | 30.00 | 3.20 s |
| folge tag | 27.60 | 30.00 | 2.40 s |

Entrances: question words per word, blur 6 px → 0 and opacity 0 → 1 in 0.13 s, 0.067 s apart (power2.out). Buttons: blur 8 px → 0 and opacity 0 → 1 in 0.15 s, no position change. Hint and folge: opacity 0 → 1 in 0.20 s (power2.out), no movement. Nothing moves after it lands (the poll stays dead still until 30.00).

### 10.3 Light and colour

Dark card. Red and green buttons are the only saturated surfaces. Folge tag is the only yellow.

---

## 11. Checklist (numbered; the checker ticks each line)

Copied from BRIEF.md (1–8) and added spec-specific items (9–22).

1. 0.00–2.00 s shows only the title card (FUSSSPUREN, IM SCHNEE, HUD). No narrative text or caption before 2.00 s. First caption C1 at 2.00.
2. Footprints (10 prints, §3.2) lie on the snow of the yard (y 700–1150), are spread from gate to door, point toward the door, and grow in size toward the viewer. None on the window glass or on any window.
3. The staircase in S5 has 13 treads (≥ 12), with railings (both sides), a landing and the sign „2. OG“. The stairs in S3 have 9 treads plus the floor.
4. Every scene has at least 8 identifiable objects: S0 9, S1 18, S2 12 + 10 prints, S3 14, S4 9, S5 22, S6 11, S7 15.
5. The HUD (NACHT 1 with red bar, 03:12 UHR, watermark @deinhandle) is present in every frame 0.00–30.00. The top-right label changes per scene (§0.2).
6. Captions match the table (§5.1) within ±0.15 s of the BRIEF segments; no two caption groups are visible at the same time; each group is 2–4 words except C11 and C16 (one word each).
7. `npx hyperframes@0.9.17 check --json` shows no errors, no contrast warnings, no layout warnings.
8. The end card (§10) shows the question „GEHST DU NACH OBEN?“, two buttons („NACHSCHAUEN“ red, „LIEBER NICHT“ green), the hint „STIMM IN DEN KOMMENTAREN AB“, and the folge tag „FOLGE FÜR TEIL 2“; each text is visible at least 2 s (table §10.2).
9. All on-screen text is German. No English labels in the video.
10. Figure motion is by rotated limbs (§2.2, §4.3, §6.2, §8.2, §9.3), not a sliding figure. Run-down-stairs beats are §4.3 (9 treads, 0.19 s each).
11. S1 figure raises its arm to the glass (3.40–4.20) and holds it there until 5.20. The hand is on the glass, not beside it.
12. S2 footprints appear one by one at the times in §3.2 (6.40 to 10.18, step 0.42 s), each with a scale-in and opacity entrance.
13. S3 includes the stair run, the door, the lock escutcheon and knob, and the rattle at 13.70–14.30.
14. S4 deadbolt slides at 15.20–15.45 and the lock snap sound is at 15.50.
15. S5 crack appears at 16.95, red flash 16.95–17.30, shake table in §8, and the figure flinch at 16.95–17.05.
16. S6 ceiling prints appear at 20.62, 20.90, 21.18, 21.46, 21.74, 22.02 with red pulses and ceiling thumps; pendant lamp swings; the figure looks up and holds still from 22.02.
17. Light and colour: cold night base, one warm accent per scene (lit windows, lamp, sign, bulb). No glow, no bloom, no neon, no gradients on the ground.
18. Captions have a text-sized scrim (rgba(7,11,20,0.55)); none is a full-width bar. Yellow keyword per group is the word given in §5.1.
19. Sound: bed edited (18.45–19.60 silenced), hits generated deterministically (no Math.random, no `random` module), cues per §7 table; bed silent after 25.90.
20. No Math.random, no Date, no fetch, no network, no CDN. GSAP from `assets/gsap.min.js`. Fonts Archivo Black and Inter only.
21. The ✓ mark is drawn as SVG (§6.3), not a text glyph.
22. Handle stays the placeholder `@deinhandle`.

### BANNED (in addition to the defaults in spec.md)

- Radial-gradient ground behind scenes (the current S1 and S5 gradients). Use flat fills.
- Glow, bloom, lens flares, floating particles beyond the fixed snowflakes.
- Every element fading and sliding up. Titles stay still after landing.
- A slow push late in a scene (the S3 push is early in its scene and ends before the cut; the S6 has no camera move).
- The old footprint placement on the window glass (S2 in the current index.html).
- Text on the window glass.
- Caption groups over more than one group at a time.
