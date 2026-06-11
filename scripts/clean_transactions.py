import pandas as pd

df = pd.read_csv("data/raw/08_investor_transactions.csv")

# Standardize transaction types
df["transaction_type"] = (
    df["transaction_type"]
    .str.strip()
    .str.upper()
)

# Fix dates
df["transaction_date"] = pd.to_datetime(
    df["transaction_date"]
)

# Amount validation
df = df[df["amount_inr"] > 0]

# KYC validation
valid_kyc = ["COMPLETED", "PENDING", "REJECTED"]

df["kyc_status"] = (
    df["kyc_status"]
    .str.strip()
    .str.upper()
)

invalid_kyc = df[
    ~df["kyc_status"].isin(valid_kyc)
]

print("Invalid KYC Records:", len(invalid_kyc))

# Remove duplicates
df = df.drop_duplicates()

df.to_csv(
    "data/processed/08_investor_transactions_cleaned.csv",
    index=False
)

print("Transactions cleaned successfully")
print(df.shape)