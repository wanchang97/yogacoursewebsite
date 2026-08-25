#!/usr/bin/env python3
"""Generiert die SRT-Untertitel (Pose-Namen) fuer die EasySit-Sequenz.
Anpassen:  PACE = Sekunden pro Atemzug, INTRO = Sekunden Begruessung vor Pose 1.
Bei bekannter Videolaenge: setze TOTAL = Videolaenge in Sek. -> PACE wird berechnet.
"""
PACE  = 5.0   # Sekunden pro Atemzug (Standard, ruhiges Tempo)
INTRO = 15.0  # Begruessung vor der ersten Haltung
TOTAL = None  # z.B. 414  -> ueberschreibt PACE automatisch

# (Untertitel, Atemzuege)
SEG = [
 ("Sitzende Aufwärmsequenz\nNa Yoga", None),          # Intro-Titel = INTRO Sek.
 ("Schneidersitz\nSukhasana", 4),
 ("Katze-Kuh im Sitzen\nMarjaryasana - Bitilasana", 32),
 ("Seitbeuge im Sitzen\nParsva Sukhasana", 10),
 ("Vorbeuge im Sitzen\nPaschimottanasana", 10),
 ("Zurück zur Mitte", 4),
 ("Drehung im Sitzen - rechts\nParivrtta Sukhasana", 8),
 ("Zurück zur Mitte", 4),
 ("Drehung im Sitzen - links\nParivrtta Sukhasana", 8),
 ("Zurück zur Mitte", 4),
 ("Stellung des Kindes\nBalasana", 4),
 ("Vierfüßlerstand\nBharmanasana", 6),
]

breaths = sum(b for _,b in SEG if b)
if TOTAL:
    PACE = (TOTAL - INTRO) / breaths

def ts(s):
    h=int(s//3600); m=int(s%3600//60); sec=int(s%60); ms=int(round((s-int(s))*1000))
    return f"{h:02d}:{m:02d}:{sec:02d},{ms:03d}"

out=[]; t=0.0; i=1
for text,b in SEG:
    dur = INTRO if b is None else b*PACE
    out.append(f"{i}\n{ts(t)} --> {ts(t+dur)}\n{text}\n")
    t+=dur; i+=1

open("EasySit_PoseNames_de.srt","w",encoding="utf-8").write("\n".join(out))
print(f"Atemzuege gesamt: {breaths} | PACE={PACE:.2f}s | Gesamtlaenge={ts(t)}")
