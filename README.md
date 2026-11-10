# Schwarzfahrer im Schweizer ÖV

**ZHAW, CAS Information Engineering, Scripting: Gruppe 05 (SC02_Gruppe_05)**

## Team

- Dominik Erbsland
- Joel Liechti

## Background

Schwarzfahren verursacht den Schweizer ÖV-Unternehmen jedes Jahr Einnahmeverluste. Kontrollen sind aufwändig, und das Personal kann nicht überall gleichzeitig sein. PostAuto hat Schwarzfahrer erfasst. Diese Fälle sind bisher nicht systematisch auf konkrete Linien, Haltestellen und Fahrten abgebildet.

## Business Case

Ziel der Analyse ist es, die erfassten Schwarzfahrer auf Zug- und Busverbindungen zu mappen. Daraus entstehen Statistiken, die zeigen, auf welchen Linien, Strecken, Haltestellen und zu welchen Zeiten Schwarzfahren besonders häufig vorkommt.

Diese Auswertung kann Kontrollen gezielter planen und die Einsatzplanung des Kontrollpersonals unterstützen.

Zusätzlich sollen verschiedene Metriken berechnet werden:

- Linien und Verbindungen mit den meisten Schwarzfahrern
- Verteilung nach Wochentag und Tageszeit
- Vergleich von Bus und Zug

## Datasets

- Schwarzfahrerdaten von PostAuto (eigener Datensatz)
- [Haltestelle / Haltekante](https://opendata.swiss/en/dataset/haltestelle-haltekante)
- [Fahrplan 2026 (GTFS)](https://ckan.opendata.swiss/de/dataset/fahrplan-2026-gtfs2020/resource/78c47ea6-2da7-4be2-9f7c-8409db436e81)

**Alternative Quelle (noch offen, ob wir sie statt GTFS verwenden):**

- [Swiss Public Transport API](https://transport.opendata.ch) (`transport.opendata.ch`): kostenlose JSON-API ohne Schlüssel für Haltestellen (`/locations`), Verbindungen (`/connections`) und Abfahrten (`/stationboard`). Sie ist einfacher einzurichten als GTFS, liefert aber nur den aktuellen Fahrplan und hat ein Fair-Use-Limit.

Die PostAuto-Rohdaten gehören nur ins Repository, wenn sie anonymisiert sind und die Weitergabe mit der Datenquelle geklärt ist.

## Daten lokal bereitstellen

Die Kontrolldaten (`ASP_202509.XLSX`) enthalten Geburtsdaten und sind deshalb **nicht im Repository**. Wer das Notebook ausführen will, legt die Datei selbst unter `data/raw/ASP_202509.XLSX` ab. Ohne sie bricht das Notebook mit einer Fehlermeldung ab.

## Notebook ausführen

1. `scripts\setup.ps1` ausführen (virtuelle Umgebung, Pakete, Output-Filter).
2. Die Excel-Datei wie oben ablegen.
3. `notebooks/01_analyse.ipynb` in VS Code öffnen, Kernel `.venv` wählen und «Run All».

## Vorgehen

1. **Daten einlesen:** PostAuto-Daten, Haltestellen und Fahrplan laden und bereinigen.
2. **Mapping:** Die erfassten Fälle auf Zug- und Busverbindungen abbilden.
3. **Auswertung:** Statistiken pro Verbindung, Linie und Zeitraum berechnen.
4. **Darstellung:** Die Ergebnisse als Tabellen und Grafiken aufbereiten.

## Projektstruktur und Nutzung

Wird ergänzt, sobald der Code im Repository liegt (Python 3, Abhängigkeiten, Startbefehl).
