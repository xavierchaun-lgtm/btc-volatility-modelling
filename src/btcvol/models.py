# src/btcvol/models.py
from __future__ import annotations
import pandas as pd
from arch import arch_model

def fit_garch11(r: pd.Series, dist: str = "t"):
    """
    r: log returns in decimal. We multiply by 100 for arch (percent units).
    dist: 'normal' | 't' | 'skewt'
    """
    am = arch_model(r * 100, mean="Constant", vol="GARCH", p=1, q=1, dist=dist)
    res = am.fit(disp="off")
    return res
