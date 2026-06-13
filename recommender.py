import pandas as pd

perf_df = pd.read_csv("07_scheme_performance.csv")

risk_input = input("Enter risk appetite (Low/Moderate/High): ")

filtered = perf_df[perf_df["risk_grade"] == risk_input]

top3 = filtered.sort_values(
    "sharpe_ratio",
    ascending=False
).head(3)

print(top3[["scheme_name", "sharpe_ratio", "risk_grade"]])