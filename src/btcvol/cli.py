# src/btcvol/cli.py
from __future__ import annotations
import argparse, os
from pathlib import Path
import pandas as pd

from .config import Config
from .data import load_prices, to_log_returns
from .models import fit_garch11
from .diagnostics import ljung_box, jb_test
from .plotting import plot_volatility

def _ensure_dirs(cfg: Config):
    for d in (cfg.outdir, cfg.figures_dir, cfg.tables_dir, cfg.models_dir):
        Path(d).mkdir(parents=True, exist_ok=True)

def run_one_ticker(ticker: str, cfg: Config, show: bool = False, dist: str | None = None):
    dist = dist or cfg.dist
    px = load_prices(ticker, cfg.start, cfg.end)
    r = to_log_returns(px)                         # decimal
    res = fit_garch11(r, dist=dist)

    # Conditional volatility (%)
    sigma = res.conditional_volatility.rename(f"{ticker}_sigma_%")
    vol_path = f"{cfg.figures_dir}/{ticker}_garch11_{dist}_vol.png"
    plot_volatility(sigma, f"{ticker} GARCH(1,1) – {dist}", vol_path, show=show)

    # Save tables
    params_df = res.params.to_frame("estimate")
    params_df["std_err"] = res.std_err
    params_df.to_csv(f"{cfg.tables_dir}/{ticker}_garch11_{dist}_params.csv")

    # Residual diagnostics
    lb = ljung_box(res.std_resid, lags=20)
    jb = jb_test(res.std_resid.rename(f"{ticker}_std_resid"))
    pd.concat([lb, jb], axis=1).to_csv(f"{cfg.tables_dir}/{ticker}_garch11_{dist}_diag.csv")

    # Save textual summary
    with open(f"{cfg.tables_dir}/{ticker}_garch11_{dist}_summary.txt", "w") as f:
        f.write(res.summary().as_text())

    # Optional: export volatility series
    sigma.to_csv(f"{cfg.tables_dir}/{ticker}_garch11_{dist}_vol_series.csv")

def main():
    ap = argparse.ArgumentParser(description="BTC/ETH GARCH(1,1) runner")
    ap.add_argument("--start", default=Config.start)
    ap.add_argument("--end", default=Config.end)
    ap.add_argument("--tickers", nargs="+", default=list(Config.tickers))
    ap.add_argument("--dist", default=Config.dist, choices=["normal", "t", "skewt"])
    ap.add_argument("--outdir", default=Config.outdir)
    ap.add_argument("--show", action="store_true")
    args = ap.parse_args()

    cfg = Config(
        start=args.start, end=args.end,
        tickers=tuple(args.tickers),
        dist=args.dist,
        outdir=args.outdir,
        figures_dir=os.path.join(args.outdir, "figures"),
        tables_dir=os.path.join(args.outdir, "tables"),
        models_dir=os.path.join(args.outdir, "models"),
    )
    _ensure_dirs(cfg)

    for tk in cfg.tickers:
        run_one_ticker(tk, cfg, show=args.show, dist=cfg.dist)

if __name__ == "__main__":
    main()
