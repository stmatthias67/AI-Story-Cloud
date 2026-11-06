# Briefing: Teil 1 „Fußspuren im Schnee“ (Serie „Nacht 1“)

Dies ist die verbindliche Grundlage für Planer, Bauer und Prüfer. Wer etwas ändert, schreibt es in SPEC.md bzw. REVIEW.md.

## Was der Nutzer ausdrücklich verlangt (Kritik der letzten Version)

1. **Mehr Detail.** Die Vorlage-Videos haben viele Bilder pro Sekunde, viele Objekte, Figuren, Licht- und Kamerawechsel. Die letzte Version war zu grob. Jede Szene braucht mehrere sichtbare Objekte und Bewegungen, keine Ein-Objekt-Bilder.
2. **Titel allein zuerst.** Die ersten 2 Sekunden zeigen nur die Titel-Karte. Kein Erzähltext auf dem Titelbild. Die Erzählung beginnt bei 2,02 s (die Stimme ist bereits um 2 s verschoben).
3. **Fußspuren im Schnee, nicht auf dem Fenster.** Die Spuren liegen auf dem Schnee im Hof, auf dem Boden, nicht auf der Glasscheibe. Sie sind über die Strecke verteilt (vom Tor bzw. Gehweg bis zur Haustür), nicht an einer Stelle gehäuft. Sie zeigen auf die Haustür zu, nicht vom Haus weg.
4. **Treppe mit vielen Stufen.** Die Treppe hat mindestens 12 Stufen, perspektivisch nach oben laufend, mit Geländer und Absatz. Nicht vier Kästchen.
5. **HUD beibehalten.** Die Elemente oben links („NACHT 1“ mit rotem Balken, Uhrzeit „03:12 UHR“), oben rechts das Ortslabel und das Wasserzeichen unten rechts bleiben so, wie sie sind. Nur das Video selbst wird überarbeitet.
6. **Deutsch.** Alle Texte und Labels auf Deutsch. Die Stimme ist ElevenLabs „Vincent Crowe“, bereits erzeugt.

## Story (Erzähltext, deutsche Stimme, bereits aufgenommen)

„Mitten in der Nacht schaue ich aus dem Fenster. Im frischen Schnee: Fußspuren. Sie führen nicht vom Haus weg. Sie führen direkt auf meine Tür zu. Ich laufe runter. Ich prüfe das Schloss. Verriegelt. Alles zu. Dann knackt es. Im zweiten Stock. Und dann … Schritte. Genau über meinem Kopf.“

## Zeitanker aus der Stimme (Stille-Erkennung, Stimme ab 2,0 s verschoben)

Sprechsegmente (Start–Ende in Sekunden, aus der Stille-Erkennung, ±0,1 s):

| Segment | Text | Start | Ende |
|---|---|---|---|
| 1 | Mitten in der Nacht schaue ich aus dem Fenster. | 2,02 | 4,65 |
| 2 | Im frischen Schnee: Fußspuren. | 5,27 | 6,28 |
| 3 | Sie führen nicht vom Haus weg. | 6,75 | 7,68 |
| 4 | Sie führen direkt auf meine Tür zu. | 8,32 | 10,03 |
| 5 | Ich laufe runter. Ich prüfe das Schloss. | 10,52 | 12,91 |
| 6 | Verriegelt. | 13,58 | 14,51 |
| 7 | Alles zu. | 15,02 | 16,17 |
| 8 | Dann knackt es. | 16,72 | 17,40 |
| 9 | Im zweiten Stock. | 17,77 | 18,45 |
| 10 | Und dann … | 19,14 | 20,19 |
| 11 | Schritte. | 20,56 | 21,52 |
| 12 | Genau über meinem Kopf. | 21,93 | 25,40 |

Stille bis zum Ende ab 25,40 s: der Abspann (Umfrage) läuft dort.

## Ablauf in Sekunden (Richtwert, Planer verfeinert)

- **0,0–2,0 Titel-Karte.** Dunkelblauer Nachthimmel, Schneeflocken, Titel „FUSSSPUREN“ und „IM SCHNEE“, Serientag „NACHT 1“. Kein Erzähltext.
- **2,0–6,3 Schlafzimmer am Fenster.** Innen, Figur (Strichfigur) steht am Fenster. Draußen: Hof mit Schnee, Laterne, Nachbarhäuser mit Fenstern, geparkte Autos unter Schnee, Zaun. Untertitel Segment 1, dann 2.
- **6,3–10,6 Blick aus dem Fenster nach unten.** Fußspuren erscheinen nacheinander im Schnee des Hofes, vom Gartentor zur Haustür, jede Spur mit der Perspektive kleiner oder größer. Die Spuren sind dunkel in den Schnee gedrückt, nicht auf der Scheibe. Untertitel Segment 3–4.
- **10,5–13,0 Haustür von innen.** Figur läuft die Treppe hinunter (sichtbare Bewegung, Beine und Arme wechseln), Ankunft an der Tür. Schloss in Nahaufnahme, Riegel wird geprüft, rüttelt. Am Türfenster sieht man draußen die Spuren im Schnee zur Tür. Untertitel 5–6.
- **13,6–16,2 Schloss verriegelt.** Badge „VERRIEGELT ✓“ bleibt mindestens 0,8 s stehen. Untertitel 7.
- **16,7–18,5 Treppenhaus.** Treppe mit mindestens 12 Stufen, Geländer, Absatz, Schild „2. OG“ erscheint. Riss an der Wand, roter Lichtblitz, Erschütterung. Untertitel 8–9.
- **19,1–22,0 Decke.** Schritte auf der Decke: Spuren von oben, auf dem Kopf stehend, jede mit Stoß, rotes Pulsieren. Untertitel 10–12.
- **25,5–30,0 Abspann.** Umfrage „Gehst du nach oben?“, Buttons „NACHSCHAUEN“ (rot) und „LIEBER NICHT“ (grün), Hinweis „STIMM IN DEN KOMMENTAREN AB“, Tag „FOLGE FÜR TEIL 2“.

## Technische Vorgaben

- Format 1080×1920, 30 fps, Dauer 30 s. Gültigkeitsbereich: Inhalt innerhalb 80 % Titel-Sicherheit, Untertitel im unteren Bereich über 1080 px.
- Engine: HyperFrames 0.9.17. Referenzen: `/tmp/hf/node_modules/hyperframes/dist/skills/hyperframes/references/` (zuerst `format.md`, `captions.md`, `types/vertical.md`, `motion.md`, `sound.md`).
- GSAP lokal: `assets/gsap.min.js` (nicht CDN, der ist blockiert).
- Schriften nur gebündelt: „Archivo Black“ für Titel, „Inter“ für Untertitel und Labels.
- Stimme: `assets/voice-timed.wav` (30 s, Erzählung ab 2,02 s). Tonspur: `assets/sfx.wav` (Wind, Schläge, Knacken), Lautstärke der Tonspur unter der Stimme.
- Untertitel: eine Gruppe pro Phrase, Schlüsselwort gelb, Fade ein 0,12 s, Fade aus 0,12 s, harte Abschaltung am Ende (siehe `captions.md`).
- Figuren: Strichfigur im Stil der Vorlage (weißer runder Kopf, weiße Linien für Arme und Beine). Bewegung mit Rotationen der Gliedmaßen, nicht eine Figur, die gleitet.
- Kein Zufall im Code (`Math.random`), keine Netzwerkaufrufe. Schneeflocken als feste Elemente mit festen Positionen.
- Handle bleibt Platzhalter `@deinhandle`.

## Qualitätskriterien (Prüfer prüft jede Zeile)

1. 0–2 s: nur Titel, kein Erzähltext sichtbar.
2. Fußspuren im Schnee, auf dem Boden, nie auf der Scheibe; Spuren laufen zur Tür und sind über die Strecke verteilt.
3. Treppe hat ≥ 12 Stufen.
4. Mindestens 8 erkennbare Objekte pro Szene (Figur, Laterne, Autos, Fenster, Zaun, Schild, Flocken, Spuren usw.).
5. HUD (Tag, Uhrzeit, Ortslabel, Wasserzeichen) durchgängig vorhanden, Ortslabel wechselt pro Szene.
6. Untertitel stimmen mit den Sprechsegmenten überein (±0,15 s) und sind nie gleichzeitig mehrere Gruppen.
7. `npx hyperframes@0.9.17 check --json`: keine Fehler, keine Kontrast- oder Layoutwarnungen.
8. Abspann mit Umfrage: Text jeweils ≥ 2 s sichtbar.
