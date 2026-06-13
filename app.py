import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(
    page_title="Bluestock MF Analytics",
    page_icon="📈",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
.main {
    background-color: #F8FAFC;
}
.big-title {
    font-size: 42px;
    font-weight: 700;
    color: #1E293B;
}
.sub-text {
    font-size: 18px;
    color: #64748B;
}
.metric-card {
    background: linear-gradient(135deg, #6C4CF1, #3B2C9E);
    padding: 20px;
    border-radius: 15px;
    color: white;
    box-shadow: 0px 8px 20px rgba(0,0,0,0.1);
}
.section {
    padding-top: 20px;
    padding-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

# Load Data
perf_df = pd.read_csv("data/processed/07_scheme_performance_cleaned.csv")

# Sidebar
st.sidebar.image(
    "https://cdn-icons-png.flaticon.com/512/2830/2830284.png",
    width=120
)

st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Go to",
    ["Dashboard", "Fund Recommender", "Category Explorer"]
)

# Header
st.markdown('<p class="big-title">Bluestock Mutual Fund Analytics Platform</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-text">Advanced Mutual Fund Intelligence Dashboard</p>', unsafe_allow_html=True)

st.divider()

# KPI Section
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Funds", len(perf_df))

with col2:
    st.metric("Top Sharpe", round(perf_df["sharpe_ratio"].max(), 2))

with col3:
    st.metric("Avg 3Y Return", round(perf_df["return_3yr_pct"].mean(), 2))

with col4:
    st.metric("Total AUM", f"₹{round(perf_df['aum_crore'].sum()/1000,2)}K Cr")

st.divider()

if page == "Dashboard":

    col1, col2 = st.columns(2)

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
        st.subheader("Fund Category Distribution")

        cat_fig = px.pie(
            perf_df,
            names="category",
            title="Category Split"
        )

        st.plotly_chart(cat_fig, use_container_width=True)

    st.subheader("Risk vs Return Analysis")

    fig = px.scatter(
        perf_df,
        x="return_3yr_pct",
        y="std_dev_ann_pct",
        size="aum_crore",
        color="category",
        hover_name="scheme_name",
        template="plotly_dark"
    )

    st.plotly_chart(fig, use_container_width=True)

if page == "Fund Recommender":

    st.subheader("Smart Fund Recommender")

    risk = st.selectbox(
        "Choose Your Risk Appetite",
        ["Low", "Moderate", "High"]
    )

    filtered = perf_df[
        perf_df["risk_grade"].str.lower() == risk.lower()
    ]

    top_recommend = filtered.sort_values(
        "sharpe_ratio",
        ascending=False
    ).head(3)

    st.success(f"Top 3 {risk} Risk Funds")

    st.dataframe(
        top_recommend,
        use_container_width=True
    )

if page == "Category Explorer":

    st.subheader("Explore by Category")

    category = st.selectbox(
        "Select Category",
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
        color="sharpe_ratio",
        title=f"{category} Fund Performance"
    )

    st.plotly_chart(
        bar_fig,
        use_container_width=True
    )

st.divider()

st.caption("Built by Harshita | Bluestock Mutual Fund Analytics Capstone")