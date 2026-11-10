# Projektregeln: Schwarzfahrer im Schweizer ÖV (ZHAW Scripting)

- Das Notebook ist der Leistungsnachweis: Jeder Schritt (Einlesen, Bereinigen, Matching, Statistik, Darstellung) steht mit Code und kurzer Begründung direkt im Notebook. Nur kleine Hilfsfunktionen gehören nach `src/schwarzfahrer/`.
- Notebooks werden ohne Outputs committet (Filter `nbstripout` via `.gitattributes`). Nach einem frischen Klon einmal `scripts/setup.ps1` bzw. `scripts/setup.sh` ausführen.
- Rohdaten in `data/raw/` gehören ins Repo (anonymisiert, Notebook muss reproduzierbar laufen). Nicht committen: `data/processed/`, ZIP-Dateien und alles über 100 MB (GitHub-Limit).
- Vor einem Commit prüfen: `git diff --cached --stat` darf keine Daten oder Outputs enthalten.
- Texte auf Deutsch, Code und Bezeichner auf Englisch.
