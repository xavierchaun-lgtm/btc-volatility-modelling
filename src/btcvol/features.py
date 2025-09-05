# src/btcvol/features.py
from __future__ import annotations
import pandas as pd

def standardize(s: pd.Series) -> pd.Series:
    z = (s - s.mean()) / s.std(ddof=0)
    z.name = f"{s.name}_z"
    return z
