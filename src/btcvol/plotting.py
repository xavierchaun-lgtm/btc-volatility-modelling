# src/btcvol/plotting.py
from __future__ import annotations
import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path

def plot_volatility(sigma: pd.Series, title: str, outpath: str | None = None, show: bool = False):
    ax = sigma.plot()
    ax.set_title(title)
    ax.set_ylabel("Conditional volatility (%)")
    ax.set_xlabel("")
    fig = ax.get_figure()
    if outpath:
        Path(outpath).parent.mkdir(parents=True, exist_ok=True)
        fig.savefig(outpath, bbox_inches="tight", dpi=220)
    if show:
        plt.show()
    plt.close(fig)
