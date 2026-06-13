import pandas as pd

# NAV HISTORY
nav = pd.read_csv("data/raw/02_nav_history.csv")
nav["date"] = pd.to_datetime(nav["date"])
nav = nav.sort_values(["amfi_code", "date"])
nav["nav"] = nav.groupby("amfi_code")["nav"].ffill()
nav = nav.drop_duplicates()
nav = nav[nav["nav"] > 0]
nav.to_csv("data/processed/02_nav_history_cleaned.csv", index=False)

# INVESTOR TRANSACTIONS
txn = pd.read_csv("data/raw/08_investor_transactions.csv")
txn["transaction_date"] = pd.to_datetime(txn["transaction_date"])
txn["transaction_type"] = txn["transaction_type"].str.strip().str.title()
txn = txn[txn["amount_inr"] > 0]

valid_kyc = ["Verified", "Pending", "Rejected"]
txn = txn[txn["kyc_status"].isin(valid_kyc)]

txn.to_csv("data/processed/08_investor_transactions_cleaned.csv", index=False)

# SCHEME PERFORMANCE
perf = pd.read_csv("data/raw/07_scheme_performance.csv")

returns = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct"
]

for col in returns:
    perf[col] = pd.to_numeric(perf[col], errors="coerce")

perf["is_anomaly"] = (
    (perf["return_3yr_pct"] > 100) |
    (perf["return_3yr_pct"] < -50)
)

perf["expense_valid"] = perf["expense_ratio_pct"].between(0.1, 2.5)

perf.to_csv("data/processed/07_scheme_performance_cleaned.csv", index=False)

print("Cleaning done.")