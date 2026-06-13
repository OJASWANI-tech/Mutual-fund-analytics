import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Bluestock MF Analytics",
    page_icon="📊",
    layout="wide"
)

# Auto Light/Dark Theme CSS
st.markdown("""
<style>
:root {
    --radius: 16px;
}

[data-testid="stMetric"] {
    border-radius: var(--radius);
    padding: 18px;
    border: 1px solid rgba(128,128,128,0.2);
    box-shadow: 0px 6px 16px rgba(0,0,0,0.05);
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

h1, h2, h3 {
    font-weight: 700 !important;
}

section[data-testid="stSidebar"] {
    border-right: 1px solid rgba(128,128,128,0.2);
}

.stDataFrame {
    border-radius: 12px;
}
</style>
""", unsafe_allow_html=True)

# Load Data
perf_df = pd.read_csv("data/processed/07_scheme_performance_cleaned.csv")

# Sidebar
st.sidebar.title("📊 Bluestock Analytics")
st.sidebar.markdown("Smart Mutual Fund Dashboard")

page = st.sidebar.radio(
    "Navigation",
    ["Dashboard", "Fund Recommender", "Category Explorer"]
)

st.sidebar.markdown("---")
st.sidebar.info(
    "Built for Bluestock Capstone Project"
)

# Main Header
st.title("Bluestock Mutual Fund Analytics Platform")
st.caption("End-to-End Mutual Fund Intelligence Dashboard")

st.divider()

# KPI Row
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Funds",
        len(perf_df)
    )

with col2:
    st.metric(
        "Top Sharpe Ratio",
        round(perf_df["sharpe_ratio"].max(), 2)
    )

with col3:
    st.metric(
        "Avg 3Y Return",
        f"{round(perf_df['return_3yr_pct'].mean(), 2)}%"
    )

with col4:
    st.metric(
        "Total AUM",
        f"₹{round(perf_df['aum_crore'].sum()/1000, 2)}K Cr"
    )

st.divider()

# Dashboard
if page == "Dashboard":

    tab1, tab2 = st.tabs(["Overview", "Analytics"])

    with tab1:

        col1, col2 = st.columns([1.3, 1])

        with col1:
            st.subheader("Top 10 Funds by Sharpe Ratio")

            top10 = perf_df.sort_values(
                "sharpe_ratio",
                ascending=False
            ).head(10)

            st.dataframe(
                top10,
                use_container_width=True
            )

        with col2:
            st.subheader("Category Distribution")

            pie_fig = px.pie(
                perf_df,
                names="category",
                hole=0.45
            )

            st.plotly_chart(
                pie_fig,
                use_container_width=True
            )

    with tab2:

        st.subheader("Risk vs Return Analysis")

        scatter_fig = px.scatter(
            perf_df,
            x="return_3yr_pct",
            y="std_dev_ann_pct",
            size="aum_crore",
            color="category",
            hover_name="scheme_name"
        )

        st.plotly_chart(
            scatter_fig,
            use_container_width=True
        )

# Recommender
if page == "Fund Recommender":

    st.subheader("Fund Recommendation Engine")

    risk = st.selectbox(
        "Select Risk Appetite",
        ["Low", "Moderate", "High"]
    )

    filtered = perf_df[
        perf_df["risk_grade"].str.lower() == risk.lower()
    ]

    top_recommend = filtered.sort_values(
        "sharpe_ratio",
        ascending=False
    ).head(3)

    st.success(
        f"Top 3 {risk} Risk Funds"
    )

    st.dataframe(
        top_recommend,
        use_container_width=True
    )

# Explorer
if page == "Category Explorer":

    st.subheader("Explore Funds by Category")

    category = st.selectbox(
        "Choose Category",
        perf_df["category"].unique()
    )

    filtered_cat = perf_df[
        perf_df["category"] == category
    ]

    st.dataframe(
        filtered_cat,
        use_container_width=True
    )

    bar_fig = px.bar(
        filtered_cat,
        x="scheme_name",
        y="return_3yr_pct",
        color="sharpe_ratio"
    )

    st.plotly_chart(
        bar_fig,
        use_container_width=True
    )

# Footer
st.divider()
st.caption(
    "Built by Ojaswani https://github.com/OJASWANI-tech/Mutual-fund-analytics • Bluestock Mutual Fund Analytics Capstone"
)