# Projektregeln: Schwarzfahrer im Schweizer ÖV (ZHAW Scripting)

- Die Aufgabenstellung verlangt vier Notebooks: `01_daten_laden`, `02_analyse`, `03_darstellung` (je ein Haupttask) und `04_bericht` (Business Case). Jedes Notebook liest die Ergebnisse des vorherigen aus `data/processed/`.
- Jeder Vorverarbeitungsschritt wird in Code-Kommentaren kurz beschrieben und begründet. Pandas DataFrames sind Pflicht, dazu mindestens ein Überblicksdiagramm und eine Heatmap-Karte.
- Einfach halten: Wir haben erst Grundkenntnisse in Python. Keine komplexen Konstrukte, kurze Kommentare, keine Gedankenstriche in Texten, Anführungszeichen als "..." (nie «»).
- Notebooks werden ohne Outputs committet (Filter `nbstripout` via `.gitattributes`). Nach einem frischen Klon einmal `scripts/setup.ps1` bzw. `scripts/setup.sh` ausführen.
- Die Kontrolldaten (`ASP_*.XLSX`) enthalten Geburtsdaten und kommen nie ins Repo. Ebenfalls nicht committen: `data/processed/`, ZIP-Dateien und alles über 100 MB.
- Vor einem Commit prüfen: `git diff --cached --stat` darf keine Daten oder Outputs enthalten.
- Texte auf Deutsch, Code und Bezeichner auf Englisch.
