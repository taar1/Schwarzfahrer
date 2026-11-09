# Projektregeln: Schwarzfahrer im Schweizer ÖV (ZHAW Scripting)

- Wiederverwendbare Logik gehört nach `src/schwarzfahrer/`, Notebooks in `notebooks/` rufen sie nur auf und zeigen Ergebnisse.
- Notebooks werden ohne Outputs committet (Filter `nbstripout` via `.gitattributes`). Nach einem frischen Klon einmal `scripts/setup.ps1` bzw. `scripts/setup.sh` ausführen.
- Rohdaten in `data/raw/` gehören ins Repo (anonymisiert, Notebook muss reproduzierbar laufen). Nicht committen: `data/processed/`, ZIP-Dateien und alles über 100 MB (GitHub-Limit).
- Vor einem Commit prüfen: `git diff --cached --stat` darf keine Daten oder Outputs enthalten.
- Texte auf Deutsch, Code und Bezeichner auf Englisch.
