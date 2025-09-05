# src/btcvol/config.py
from dataclasses import dataclass

@dataclass
class Config:
    start: str = "2018-01-01"
    end: str   = "2024-12-31"
    tickers: tuple[str, ...] = ("BTC-USD", "ETH-USD")
    dist: str = "t"                  # 'normal' | 't' | 'skewt'
    outdir: str = "results"
    figures_dir: str = "results/figures"
    tables_dir: str = "results/tables"
    models_dir: str = "results/models"
