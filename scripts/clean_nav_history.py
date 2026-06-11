import pandas as pd

df = pd.read_csv("data/raw/02_nav_history.csv")

# Date conversion
df["date"] = pd.to_datetime(df["date"])

# Sort
df = df.sort_values(["amfi_code", "date"])

# Remove duplicates
df = df.drop_duplicates()

# Forward fill NAV
df["nav"] = df.groupby("amfi_code")["nav"].ffill()

# NAV validation
df = df[df["nav"] > 0]

df.to_csv(
    "data/processed/02_nav_history_cleaned.csv",
    index=False
)

print(df.shape)