from sqlalchemy import create_engine
import pandas as pd

engine = create_engine(
    "sqlite:///bluestock_mf.db"
)

datasets = {
    "dim_fund":
    "data/processed/01_fund_master_cleaned.csv",

    "fact_nav":
    "data/processed/02_nav_history_cleaned.csv",

    "fact_transactions":
    "data/processed/08_investor_transactions_cleaned.csv",

    "fact_performance":
    "data/processed/07_scheme_performance_cleaned.csv"
}

for table, path in datasets.items():

    df = pd.read_csv(path)

    df.to_sql(
        table,
        engine,
        if_exists="replace",
        index=False
    )

    print(
        f"{table} loaded: {len(df)} rows"
    )

print("Database Loaded Successfully")