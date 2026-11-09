# Einmalig nach dem Klonen ausfuehren: venv, Abhaengigkeiten, Output-Filter fuer Notebooks
python -m venv .venv
.\.venv\Scripts\python -m pip install -r requirements.txt
.\.venv\Scripts\nbstripout --install
Write-Host "Fertig. Aktivieren mit: .\.venv\Scripts\Activate.ps1"
