import numpy as np
import pandas as pd

# 1. Your weights (from your last message)
weights = np.array([
    0.004809576017, 0.01587122025,  0.005340096822, 0.007117309801,
    0.1403797379,   0.008476068944, 0.02658524543,  0.07030616485,
    0.001599808852, 0.03495664806,  0.009066852176, 0.005453221027,
    0.03754285769,  0.04953761803,  0.003143161325, 0.002508397093,
    0.02808461691,  0.04582481818,  0.0004267002727,0.00185185381,
    0.009156717199, 0.004372726283, 0.09276607712,  0.2064831799,
    0.01036196574,  0.01832612122,  0.05319903622,  0.05651135524,
    0.01670855082,  0.03004029125,  0.001301668423,0.001890337184
])

# 2. Load your adjusted-close price data
stocks = pd.read_csv(
    r"E:\Portfolio_Optimization_Project\data\all_adj_close.csv",
    parse_dates=["Date"],
    index_col="Date"
)

# 3. Compute daily returns and annualize
returns = stocks.pct_change().dropna(how ='all')       # daily returns

mu      = returns.mean() * 252               # expected annual return per asset
Sigma   = returns.cov()  * 252               # annual covariance matrix

# 4. Portfolio metrics
risk_free_rate = 0.04    # e.g. 4% p.a.; adjust as needed

Rp     = weights.dot(mu)                     # portfolio expected return
sigma  = np.sqrt(weights.dot(Sigma).dot(weights))  # portfolio volatility
sharpe = (Rp - risk_free_rate) / sigma       # annualized Sharpe ratio

print(f"Expected Return:     {Rp:.6f}")
print(f"Expected Volatility: {sigma:.6f}")
print(f"Sharpe Ratio:        {sharpe:.6f}")
