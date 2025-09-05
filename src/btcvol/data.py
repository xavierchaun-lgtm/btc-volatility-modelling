# src/btcvol/data.py
from __future__ import annotations
import pandas as pd
import numpy as np
import yfinance as yf

def load_prices(ticker: str, start: str, end: str) -> pd.Series:
    df = yf.download(ticker, start=start, end=end, auto_adjust=True, progress=False)
    if df.empty:
        raise ValueError(f"No data returned by yfinance for {ticker} in [{start}, {end}]")
    px = df["Close"].rename(ticker).sort_index()
    return px

def to_log_returns(price: pd.Series) -> pd.Series:
    """Return log returns in decimal (not %)."""
    price = price.ffill().dropna().astype(float)
    r = np.log(price).diff().dropna()
    r.name = f"{price.name}_logret"
    return r

def load_returns_panel(tickers: list[str], start: str, end: str) -> pd.DataFrame:
    series = [to_log_returns(load_prices(tk, start, end)) for tk in tickers]
    df = pd.concat(series, axis=1).dropna(how="all")
    return df
