CREATE TABLE dim_fund (
amfi_code INTEGER PRIMARY KEY,
scheme_name TEXT,
fund_house TEXT,
category TEXT
);

CREATE TABLE dim_date (
date_id INTEGER PRIMARY KEY,
full_date DATE
);

CREATE TABLE fact_nav (
nav_id INTEGER PRIMARY KEY AUTOINCREMENT,
amfi_code INTEGER,
date DATE,
nav REAL,
FOREIGN KEY(amfi_code) REFERENCES dim_fund(amfi_code)
);

CREATE TABLE fact_transactions (
txn_id INTEGER PRIMARY KEY AUTOINCREMENT,
investor_id TEXT,
amfi_code INTEGER,
transaction_date DATE,
transaction_type TEXT,
amount_inr REAL,
FOREIGN KEY(amfi_code) REFERENCES dim_fund(amfi_code)
);

CREATE TABLE fact_performance (
perf_id INTEGER PRIMARY KEY AUTOINCREMENT,
amfi_code INTEGER,
return_1yr_pct REAL,
return_3yr_pct REAL,
sharpe_ratio REAL,
expense_ratio_pct REAL,
FOREIGN KEY(amfi_code) REFERENCES dim_fund(amfi_code)
);

CREATE TABLE fact_aum (
aum_id INTEGER PRIMARY KEY AUTOINCREMENT,
fund_house TEXT,
aum_crore REAL
);
