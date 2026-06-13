txn = pd.read_csv("data/raw/08_investor_transactions.csv")

# date fix
txn["transaction_date"] = pd.to_datetime(txn["transaction_date"])

# standardize transaction type
txn["transaction_type"] = txn["transaction_type"].str.strip().str.title()

txn["transaction_type"] = txn["transaction_type"].replace({
    "Sip": "SIP",
    "Lumpsum": "Lumpsum",
    "Redemption": "Redemption"
})

# amount validation
txn = txn[txn["amount_inr"] > 0]

# KYC check
valid_kyc = ["Verified", "Pending", "Rejected"]
txn = txn[txn["kyc_status"].isin(valid_kyc)]

txn.to_csv("data/processed/08_investor_transactions_cleaned.csv", index=False)