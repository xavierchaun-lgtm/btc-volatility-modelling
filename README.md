# 🧠 BTC Volatility Modelling with GARCH-type Models

This project explores the volatility of Bitcoin using various GARCH-type models including:
- GARCH
- EGARCH
- GJR-GARCH

The goal is to assess the effectiveness of each model on historical BTC price data and identify volatility clustering patterns and forecasting performance.

## 🧪 Models & Methodology
- **GARCH(1,1)**: Standard volatility modelling
- **EGARCH**: Captures asymmetric volatility effects
- **GJR-GARCH**: Models leverage effect

## 🛠 Technologies
- Python (NumPy, pandas, arch, matplotlib, seaborn)
- Jupyter Notebook
- Git/GitHub

## 📊 Dataset
Bitcoin daily price data from [Yahoo Finance](https://finance.yahoo.com/)

## 📈 Results
- Visualisation of fitted volatilities
- Comparison of AIC/BIC
- Forecast accuracy metrics


## Quickstart

```bash
pip install -r requirements.txt
# 运行 BTC & ETH，t 分布：
python -m src.btcvol.cli --tickers BTC-USD ETH-USD --dist t --start 2018-01-01 --end 2024-12-31
# 仅展示图像（不阻塞执行可去掉 --show）：
python -m src.btcvol.cli --tickers BTC-USD --dist normal --show
