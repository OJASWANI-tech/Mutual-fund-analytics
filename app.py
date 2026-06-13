import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Bluestock MF Analytics",
    layout="wide"
)

# Load data first
perf_df = pd.read_csv("data/processed/07_scheme_performance_cleaned.csv")

st.title("Bluestock Mutual Fund Analytics Platform")

# KPI Cards
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Funds", len(perf_df))

with col2:
    st.metric(
        "Top Sharpe",
        round(perf_df["sharpe_ratio"].max(), 2)
    )

with col3:
    st.metric(
        "Avg 3Y Return",
        round(perf_df["return_3yr_pct"].mean(), 2)
    )

# Overview
st.subheader("Project Overview")
st.write("""
This platform analyzes:
- Mutual Fund NAV trends
- SIP inflows
- Fund performance
- Risk metrics
- Investor demographics
""")

# Top Funds
st.subheader("Top 10 Funds by Sharpe Ratio")

top10 = perf_df.sort_values(
    "sharpe_ratio",
    ascending=False
).head(10)

st.dataframe(top10)

# Scatter Plot
st.subheader("Risk vs Return Analysis")

fig = px.scatter(
    perf_df,
    x="return_3yr_pct",
    y="std_dev_ann_pct",
    size="aum_crore",
    color="category",
    hover_name="scheme_name"
)

st.plotly_chart(fig)

# Recommender
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

# Category Explorer
st.subheader("Explore Funds by Category")

category = st.selectbox(
    "Select Category",
    perf_df["category"].unique()
)

filtered_cat = perf_df[
    perf_df["category"] == category
]

st.dataframe(filtered_cat)