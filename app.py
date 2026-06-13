import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Bluestock MF Analytics",
    layout="wide"
)

st.title("Bluestock Mutual Fund Analytics Platform")

st.subheader("Project Overview")
st.write("""
This platform analyzes:
- Mutual Fund NAV trends
- SIP inflows
- Fund performance
- Risk metrics
- Investor demographics
""")

# Load sample file
perf_df = pd.read_csv("data/processed/07_scheme_performance_cleaned.csv")

st.subheader("Top 10 Funds by Sharpe Ratio")

top10 = perf_df.sort_values(
    "sharpe_ratio",
    ascending=False
).head(10)

st.dataframe(top10)

st.subheader("Risk Appetite Recommender")

risk = st.selectbox(
    "Choose Risk Appetite",
    ["Low", "Moderate", "High"]
)

filtered = perf_df[
    perf_df["risk_grade"].str.lower() == risk.lower()
]

st.write("Top Recommended Funds")

st.dataframe(
    filtered.sort_values(
        "sharpe_ratio",
        ascending=False
    ).head(3)
)