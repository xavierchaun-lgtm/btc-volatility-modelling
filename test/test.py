# test/test.py
from src.btcvol.data import load_prices, to_log_returns
from src.btcvol.models import fit_garch11

def test_garch_minimal():
    px = load_prices("BTC-USD", "2024-11-01", "2024-12-01")
    assert not px.empty and px.name == "BTC-USD"
    r = to_log_returns(px)
    assert r.size > 10
    res = fit_garch11(r, dist="t")
    # 至少要有 omega, alpha[1], beta[1]
    for k in ["omega", "alpha[1]", "beta[1]"]:
        assert k in res.params.index
