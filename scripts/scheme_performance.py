perf = pd.read_csv("data/raw/07_scheme_performance.csv")

return_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct"
]

for col in return_cols:
    perf[col] = pd.to_numeric(perf[col], errors="coerce")

# anomaly flag
perf["is_anomaly"] = (
    (perf["return_3yr_pct"] > 100) |
    (perf["return_3yr_pct"] < -50)
)

# expense ratio validation
perf["expense_valid"] = perf["expense_ratio_pct"].between(0.1, 2.5)

perf.to_csv("data/processed/07_scheme_performance_cleaned.csv", index=False)