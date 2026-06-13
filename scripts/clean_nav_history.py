# data_ingestion.py

import pandas as pd

nav = pd.read_csv("data/raw/02_nav_history.csv")

# convert date
nav["date"] = pd.to_datetime(nav["date"])

# sort
nav = nav.sort_values(["amfi_code", "date"])

# forward fill missing nav
nav["nav"] = nav.groupby("amfi_code")["nav"].ffill()

# remove duplicates
nav = nav.drop_duplicates()

# validate nav > 0
nav = nav[nav["nav"] > 0]

# save
nav.to_csv("data/processed/02_nav_history_cleaned.csv", index=False)