CREATE TABLE dim_fund(
    amfi_code INTEGER PRIMARY KEY,
    scheme_name TEXT,
    fund_house TEXT,
    category TEXT,
    sub_category TEXT,
    risk_category TEXT
);

CREATE TABLE dim_date(
    date_id INTEGER PRIMARY KEY,
    date DATE
);

CREATE TABLE fact_nav(
    nav_id INTEGER PRIMARY KEY AUTOINCREMENT,
    amfi_code INTEGER,
    date DATE,
    nav REAL,
    FOREIGN KEY(amfi_code)
    REFERENCES dim_fund(amfi_code)
);

CREATE TABLE fact_transactions(
    txn_id INTEGER PRIMARY KEY,
    investor_id INTEGER,
    amfi_code INTEGER,
    amount REAL,
    transaction_type TEXT,
    txn_date DATE
);

CREATE TABLE fact_performance(
    perf_id INTEGER PRIMARY KEY AUTOINCREMENT,
    amfi_code INTEGER,
    sharpe_ratio REAL,
    sortino_ratio REAL,
    alpha REAL,
    beta REAL
);

CREATE TABLE fact_aum(
    aum_id INTEGER PRIMARY KEY AUTOINCREMENT,
    fund_house TEXT,
    quarter_date DATE,
    aum_crore REAL
);