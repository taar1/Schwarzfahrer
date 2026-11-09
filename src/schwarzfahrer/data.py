"""Einlesen der Rohdaten aus data/raw/."""
from pathlib import Path

import pandas as pd

RAW_DIR = Path(__file__).resolve().parents[2] / "data" / "raw"


def load_stops(path: Path = RAW_DIR / "haltestelle_haltekante.csv") -> pd.DataFrame:
    """Haltestellen (SBB Atlas) mit Koordinaten, eine Zeile pro Haltestelle.

    Spalten: sloid, name, lat, lon, canton, municipality, transport, operator
    """
    df = pd.read_csv(path, sep=";", encoding="utf-8-sig", low_memory=False)
    # Die Datei enthält ein zweites BOM mitten im Header
    df.columns = df.columns.str.replace("﻿", "", regex=False)

    coords = df["geopos_haltestelle"].str.split(",", expand=True).astype(float)
    stops = pd.DataFrame(
        {
            "sloid": df["Haltestelle SLOID"],
            "name": df["offizielle Haltestellen Bezeichnung"],
            "lat": coords[0],
            "lon": coords[1],
            "canton": df["cantonAbbreviation"],
            "municipality": df["municipalityName"],
            "transport": df["meansOfTransport"],
            "operator": df["businessOrganisationDescriptionDe"],
        }
    )
    # Mehrere Zeilen pro Haltestelle (Haltekanten): eine pro SLOID behalten
    return stops.dropna(subset=["lat", "lon"]).drop_duplicates("sloid").reset_index(drop=True)
