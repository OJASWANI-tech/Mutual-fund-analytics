import pandas as pd


# -------------------------------
# 01 FUND MASTER
# -------------------------------
fund = pd.read_csv("data/raw/01_fund_master.csv")

fund = fund.drop_duplicates()
fund["launch_date"] = pd.to_datetime(fund["launch_date"])

fund.to_csv(
    "data/processed/01_fund_master_cleaned.csv",
    index=False
)


# -------------------------------
# 02 NAV HISTORY
# -------------------------------
nav = pd.read_csv("data/raw/02_nav_history.csv")

nav["date"] = pd.to_datetime(nav["date"])
nav = nav.sort_values(["amfi_code", "date"])
nav["nav"] = nav.groupby("amfi_code")["nav"].ffill()
nav = nav.drop_duplicates()
nav = nav[nav["nav"] > 0]

nav.to_csv(
    "data/processed/02_nav_history_cleaned.csv",
    index=False
)


# -------------------------------
# 03 AUM BY FUND HOUSE
# -------------------------------
aum = pd.read_csv("data/raw/03_aum_by_fund_house.csv")

aum = aum.drop_duplicates()
aum = aum[aum["aum_crore"] > 0]

aum.to_csv(
    "data/processed/03_aum_by_fund_house_cleaned.csv",
    index=False
)


# -------------------------------
# 04 MONTHLY SIP INFLOWS
# -------------------------------
sip = pd.read_csv("data/raw/04_monthly_sip_inflows.csv")

sip["month"] = pd.to_datetime(sip["month"])
sip = sip.drop_duplicates()
sip = sip[sip["sip_inflow_crore"] > 0]

sip.to_csv(
    "data/processed/04_monthly_sip_inflows_cleaned.csv",
    index=False
)


# -------------------------------
# 05 CATEGORY INFLOWS
# -------------------------------
cat = pd.read_csv("data/raw/05_category_inflows.csv")

cat["category"] = cat["category"].str.strip().str.title()
cat = cat.drop_duplicates()
cat = cat[cat["net_inflow_crore"] > 0]

cat.to_csv(
    "data/processed/05_category_inflows_cleaned.csv",
    index=False
)


# -------------------------------
# 06 INDUSTRY FOLIO COUNT
# -------------------------------
folio = pd.read_csv("data/raw/06_industry_folio_count.csv")

folio = folio.drop_duplicates()

# Fix based on available column
if "date" in folio.columns:
    folio["date"] = pd.to_datetime(folio["date"])
    folio["year"] = folio["date"].dt.year

elif "month" in folio.columns:
    folio["month"] = pd.to_datetime(folio["month"])
    folio["year"] = folio["month"].dt.year

folio = folio[folio["total_folios_crore"] > 0]

folio.to_csv(
    "data/processed/06_industry_folio_count_cleaned.csv",
    index=False
)


# -------------------------------
# 07 SCHEME PERFORMANCE
# -------------------------------
perf = pd.read_csv("data/raw/07_scheme_performance.csv")

return_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct"
]

for col in return_cols:
    perf[col] = pd.to_numeric(
        perf[col],
        errors="coerce"
    )

perf["is_anomaly"] = (
    (perf["return_3yr_pct"] > 100)
    | (perf["return_3yr_pct"] < -50)
)

perf["expense_valid"] = perf[
    "expense_ratio_pct"
].between(0.1, 2.5)

perf = perf.drop_duplicates()

perf.to_csv(
    "data/processed/07_scheme_performance_cleaned.csv",
    index=False
)


# -------------------------------
# 08 INVESTOR TRANSACTIONS
# -------------------------------
txn = pd.read_csv("data/raw/08_investor_transactions.csv")

txn["transaction_date"] = pd.to_datetime(
    txn["transaction_date"]
)

txn["transaction_type"] = txn[
    "transaction_type"
].str.strip().str.title()

txn = txn[txn["amount_inr"] > 0]

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


# -------------------------------
# 09 PORTFOLIO HOLDINGS
# -------------------------------
hold = pd.read_csv("data/raw/09_portfolio_holdings.csv")

hold = hold.drop_duplicates()

hold["weight_pct"] = pd.to_numeric(
    hold["weight_pct"],
    errors="coerce"
)

hold = hold[hold["weight_pct"] > 0]

hold.to_csv(
    "data/processed/09_portfolio_holdings_cleaned.csv",
    index=False
)


# -------------------------------
# 10 BENCHMARK INDICES
# -------------------------------
bench = pd.read_csv("data/raw/10_benchmark_indices.csv")

bench["date"] = pd.to_datetime(
    bench["date"]
)

bench = bench.drop_duplicates()

bench["return_pct"] = pd.to_numeric(
    bench["return_pct"],
    errors="coerce"
)

bench.to_csv(
    "data/processed/10_benchmark_indices_cleaned.csv",
    index=False
)


print("All 10 datasets cleaned successfully!")