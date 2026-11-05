---
name: schau-nicht-hoch-video
description: Make a new German vertical TikTok story episode (30–70 s, 1080×1920) in the "Nacht 1" / "Schau nicht hoch" style, built in code with HyperFrames and narrated with the ElevenLabs voice Vincent Crowe. Use when the user asks for a new Teil/Folge of the series, a scary or suspense story short, or a German vertical video in this style.
---

# Schau nicht hoch: Story-Episode bauen

Ziel: eine Folge, die optisch und im Ablauf zur Vorlage passt (Titel-Karte, Erzählung mit Untertiteln, Handy-Einblendungen, Cliffhanger-Umfrage, Folge-Tag). Alles wird im Code gebaut (HyperFrames), nicht im Schnittprogramm.

## Feste Vorgaben

- **Sprache:** immer Deutsch. Untertitel, Texte, Umfragen, Labels auf Deutsch.
- **Stimme:** ElevenLabs „Vincent Crowe – Dark & Haunting Tales“, `voice_id` `18X2yBovneA0q06wd8E9`, Modell `eleven_v4`. Die Stimme nicht durch eine andere ersetzen, ohne dass der Nutzer es verlangt.
- **Format:** 1080×1920, 30 fps, Länge 30–70 s (die erste Folge ist 30 s).
- **Engine:** HyperFrames `0.9.17` (`npx hyperframes@0.9.17 …`). Vor dem Bauen die Hyperframes-Skill (`/hyperframes`) lesen, besonders `references/types/vertical.md` und `references/captions.md`.
- **Keine fremden Marken:** Das Handle ist ein Platzhalter (`@deinhandle`), bis der Nutzer seins nennt. Titel und Logo der Vorlage-Creator nicht übernehmen; nur den Stil.

## Ablauf einer Folge

1. **Story schreiben** (Deutsch, kurze Sätze). Struktur: Hook in den ersten 2 s, Steigerung, Stopp kurz vor der Auflösung, dann Cliffhanger-Umfrage. Vorlage: Teil 1 unter `videos/schau-nicht-hoch/teil-01-fussspuren/`.
2. **Erzählung als Text planen**: Phrasen mit geschätzten Start-/Endzeiten (Untertitel-Gruppen von 2–4 Wörtern).
3. **Stimme erzeugen** mit `creative_generate_speech` (ElevenLabs-MCP): `voice_id` wie oben, `model_id` `eleven_v4`. Nie denselben Aufruf wiederholen, weil er Credits kostet; bei „busy“ den Nutzer informieren und später erneut versuchen.
4. **Projekt anlegen** unter `videos/schau-nicht-hoch/teil-NN-<thema>/` mit `index.html`, `hyperframes.json`, `package.json`, `assets/` (Stimme als `voice.mp3`, Tonspur als `sfx.wav`).
5. **Szenen bauen:** pro Szene ein Hintergrund-Host mit `class="clip"`, `data-start`, `data-duration`. Schrift: `Archivo Black` für Titel, `Inter` 900 für Untertitel. Farben: Nacht-Blau/Schwarz, Rot für Alarm, Grün für Entwarnung und Umfrage (`#1b8a4b` für Kontrast), Gelb `#ffe14d` für Schlüsselwörter.
6. **Untertitel:** eine Gruppe pro Phrase, Schlüsselwort gelb (`span.k`), Ein- und Ausblenden wie in `references/captions.md`. Die Zeiten nach dem Erzeugen der Stimme am Audio ausrichten.
7. **Tonspur:** Wind, Schläge und Knacken mit ffmpeg erzeugen (siehe Teil 1). Die Stimme kommt als zweites `<audio>`-Element dazu.
8. **Prüfen:** `npx hyperframes@0.9.17 check --json` muss ohne Fehler sein, Kontrast- und Layoutwarnungen beheben. Danach `snapshot --at …` und die Bilder ansehen.
9. **Rendern:** `npx hyperframes@0.9.17 render --output out/<name>.mp4`. Die MP4 nach dem Rendern nicht ins Repo committen, wenn sie groß ist; nur Quelle und Skill einchecken, außer der Nutzer will das Video.

## Erzählstil

- Anrede „du“ oder Ich-Form, Ein-Satz-Absätze, Pausen durch Punkte.
- Jede Folge endet offen. Auf die letzte Zeile folgt eine Umfrage mit zwei Buttons (rot und grün) und „Stimm in den Kommentaren ab“, dann „Folge für Teil X“.
- Wiederkehrende Elemente: Handy-Einblendung mit Alarm, Ortslabel oben rechts, Uhrzeit oben links („NACHT 1 · 03:12 UHR“).

## Was nicht gemacht wird

- Keine echten Personen, keine Marken, keine Musik ohne Lizenz.
- Keine Ausgabe in anderen Sprachen, außer der Nutzer verlangt es ausdrücklich.
- Keine Veröffentlichung oder Upload auf TikTok; das macht der Nutzer selbst.
