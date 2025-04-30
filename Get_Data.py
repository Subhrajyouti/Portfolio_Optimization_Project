# fetch_data.py

import yfinance as yf
import pandas as pd
from datetime import datetime

# 1) List of all NSE/BSE tickers
tickers = [
   "ASHOKLEY.NS",    # Ashok Leyland Ltd
    "BAJAJHFL.NS",    # Bajaj Housing Finance Ltd
    "BANKBARODA.NS",  # Bank of Baroda
    "CENTRALBK.NS",   # Central Bank of India
    "DLF.NS",         # DLF Limited
    "EASEMYTRIP.NS",  # Easy Trip Planners Ltd
    "HINDALCO.NS",    # Hindalco Industries Ltd
    "IDFCFIRSTB.NS",  # IDFC First Bank Ltd
    "IOB.NS",         # Indian Overseas Bank
    "IRFC.NS",        # Indian Railway Finance Corp Ltd
    "ITC.NS",         # ITC Ltd
    "JIOFIN.NS",      # Jio Financial Services Ltd
    "NBCC.NS",        # NBCC (India) Ltd
    "NHPC.NS",        # NHPC Ltd
    "OLAELEC.NS",     # Ola Electric Mobility Ltd
    "OMINFRAL.NS",    # Om Infra Limited
    "PNB.NS",         # Punjab National Bank
    "RVNL.NS",        # Rail Vikas Nigam Ltd
    "RAMASTEEL.NS",   # Rama Steel Tubes Ltd
    "RTNINDIA.NS",    # RattanIndia Enterprises Ltd
    "RECLTD.NS",      # REC Ltd
    "RPOWER.NS",      # Reliance Power Ltd
    "SBISENSEX.BO",   # SBI ETF – Sensex (BSE)
    "SETFNIF50.NS",   # SBI ETF – Nifty 50 (NSE)
    "SJVN.NS",        # SJVN Ltd
    "SUZLON.NS",      # Suzlon Energy Ltd
    "TATACHEM.NS",    # Tata Chemicals Ltd
    "TATAMOTORS.NS",  # Tata Motors Ltd
    "TATAPOWER.NS",   # Tata Power Co. Ltd
    "TATASTEEL.NS",   # Tata Steel Ltd
    "UCOBANK.NS",     # UCO Bank
    "IDEA.NS"  
]

# 2) Date range
start_date = "2020-01-01"
end_date   = datetime.today().strftime("%Y-%m-%d")

# 3) Download auto-adjusted OHLCV data
data = yf.download(
    tickers,
    start=start_date,
    end=end_date,
    interval="1d",
    group_by="ticker",
    auto_adjust=True,
    threads=True
)

# 4) Write each ticker’s DataFrame to CSV
import os
os.makedirs("data", exist_ok=True)

for t in tickers:
    df = data[t].copy()
    df.to_csv(f"data/{t}.csv")
    print(f"→ data/{t}.csv [{len(df)} rows]")

# 5) (Optional) Combine all Close prices
adj_close = pd.DataFrame({t: data[t]["Close"] for t in tickers})
adj_close.to_csv("data/all_adj_close.csv")
print("→ data/all_adj_close.csv")
