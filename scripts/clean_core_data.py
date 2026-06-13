import pandas as pd


# -----------------------------
# 1. CLEAN NAV HISTORY
# -----------------------------
nav = pd.read_csv("data/raw/02_nav_history.csv")

# Convert date
nav["date"] = pd.to_datetime(nav["date"])

# Sort
nav = nav.sort_values(
    ["amfi_code", "date"]
)

# Forward fill missing NAV
nav["nav"] = nav.groupby(
    "amfi_code"
)["nav"].ffill()

# Remove duplicates
nav = nav.drop_duplicates()

# Validate NAV > 0
nav = nav[nav["nav"] > 0]

# Save
nav.to_csv(
    "data/processed/02_nav_history_cleaned.csv",
    index=False
)


# -----------------------------
# 2. CLEAN INVESTOR TRANSACTIONS
# -----------------------------
txn = pd.read_csv(
    "data/raw/08_investor_transactions.csv"
)

# Fix dates
txn["transaction_date"] = pd.to_datetime(
    txn["transaction_date"]
)

# Standardize transaction types
txn["transaction_type"] = txn[
    "transaction_type"
].str.strip().str.title()

txn["transaction_type"] = txn[
    "transaction_type"
].replace({
    "Sip": "SIP",
    "Lumpsum": "Lumpsum",
    "Redemption": "Redemption"
})

# Amount validation
txn = txn[
    txn["amount_inr"] > 0
]

# Valid KYC values
valid_kyc = [
    "Verified",
    "Pending",
    "Rejected"
]

txn = txn[
    txn["kyc_status"].isin(valid_kyc)
]

txn = txn.drop_duplicates()

txn.to_csv(
    "data/processed/08_investor_transactions_cleaned.csv",
    index=False
)


# -----------------------------
# 3. CLEAN SCHEME PERFORMANCE
# -----------------------------
perf = pd.read_csv(
    "data/raw/07_scheme_performance.csv"
)

return_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct"
]

# Convert returns to numeric
for col in return_cols:
    perf[col] = pd.to_numeric(
        perf[col],
        errors="coerce"
    )

# Flag anomalies
perf["is_anomaly"] = (
    (perf["return_3yr_pct"] > 100)
    |
    (perf["return_3yr_pct"] < -50)
)

# Expense ratio validation
perf["expense_valid"] = perf[
    "expense_ratio_pct"
].between(0.1, 2.5)

perf = perf.drop_duplicates()

perf.to_csv(
    "data/processed/07_scheme_performance_cleaned.csv",
    index=False
)

print("Core cleaning completed successfully.")