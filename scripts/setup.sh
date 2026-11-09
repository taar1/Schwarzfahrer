#!/bin/sh
# Einmalig nach dem Klonen ausfuehren: venv, Abhaengigkeiten, Output-Filter fuer Notebooks
python -m venv .venv
. .venv/bin/activate 2>/dev/null || . .venv/Scripts/activate
pip install -r requirements.txt
nbstripout --install
echo "Fertig."
