import streamlit as st
import pandas as pd
import plotly.express as px

# ------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------
st.set_page_config(
    page_title="Bluestock MF Analytics",
    page_icon="📊",
    layout="wide"
)

# ------------------------------------------------
# CUSTOM CSS
# ------------------------------------------------
st.markdown("""
<style>
body {
    font-family: 'Inter', sans-serif;
}
.block-container {
    padding-top: 2rem;
}
[data-testid="stMetric"] {
    background: white;
    border: 1px solid #E5E7EB;
    padding: 15px;
    border-radius: 12px;
}
</style>
""", unsafe_allow_html=True)

# ------------------------------------------------
# LOAD DATA
# ------------------------------------------------
@st.cache_data
def load_perf():
    return pd.read_csv(
        "data/processed/07_scheme_performance_cleaned.csv"
    )

@st.cache_data
def load_nav():
    nav = pd.read_csv(
        "data/processed/02_nav_history_cleaned.csv"
    )
    nav["date"] = pd.to_datetime(nav["date"])
    return nav

perf_df = load_perf()
nav_df = load_nav()

# ------------------------------------------------
# SIDEBAR
# ------------------------------------------------
st.sidebar.title("📊 Bluestock")
page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "NAV Trends",
        "Fund Recommender",
        "Category Explorer"
    ]
)

# ------------------------------------------------
# HEADER
# ------------------------------------------------
st.title("Bluestock Mutual Fund Analytics Platform")
st.caption("Professional Mutual Fund Intelligence Dashboard")

# ------------------------------------------------
# KPI SECTION
# ------------------------------------------------
col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Funds",
    len(perf_df)
)

col2.metric(
    "Top Sharpe Ratio",
    round(
        perf_df["sharpe_ratio"].max(), 2
    )
)

col3.metric(
    "Avg 3Y Return",
    f"{round(perf_df['return_3yr_pct'].mean(), 2)}%"
)

col4.metric(
    "Total AUM",
    f"₹{round(perf_df['aum_crore'].sum()/1000, 2)}K Cr"
)

st.divider()

# ------------------------------------------------
# DASHBOARD
# ------------------------------------------------
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

        fig = px.pie(
            perf_df,
            names="category",
            hole=0.4
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    st.subheader("Risk vs Return Analysis")

    fig2 = px.scatter(
        perf_df,
        x="return_3yr_pct",
        y="std_dev_ann_pct",
        size="aum_crore",
        color="category",
        hover_name="scheme_name"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

# ------------------------------------------------
# NAV TRENDS
# ------------------------------------------------
elif page == "NAV Trends":

    st.subheader("Daily NAV Trends")

    selected_scheme = st.selectbox(
        "Select AMFI Code",
        nav_df["amfi_code"].unique()
    )

    filtered_nav = nav_df[
        nav_df["amfi_code"] == selected_scheme
    ]

    fig3 = px.line(
        filtered_nav,
        x="date",
        y="nav",
        title=f"NAV Trend — {selected_scheme}"
    )

    st.plotly_chart(
        fig3,
        use_container_width=True
    )

# ------------------------------------------------
# FUND RECOMMENDER
# ------------------------------------------------
elif page == "Fund Recommender":

    st.subheader("Risk-Based Fund Recommendations")

    risk = st.selectbox(
        "Select Risk Appetite",
        ["Low", "Moderate", "High"]
    )

    filtered = perf_df[
        perf_df["risk_grade"].str.lower() == risk.lower()
    ]

    recommended = filtered.sort_values(
        "sharpe_ratio",
        ascending=False
    ).head(3)

    st.dataframe(
        recommended,
        use_container_width=True
    )

# ------------------------------------------------
# CATEGORY EXPLORER
# ------------------------------------------------
elif page == "Category Explorer":

    st.subheader("Explore by Category")

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

    fig4 = px.bar(
        filtered_cat,
        x="scheme_name",
        y="return_3yr_pct",
        color="sharpe_ratio"
    )

    st.plotly_chart(
        fig4,
        use_container_width=True
    )

# ------------------------------------------------
# DOWNLOAD BUTTON
# ------------------------------------------------
st.divider()

st.download_button(
    "📥 Download Performance Data",
    perf_df.to_csv(index=False),
    file_name="scheme_performance.csv",
    mime="text/csv"
)

# ------------------------------------------------
# FOOTER
# ------------------------------------------------
st.caption(
    "Built by Ojaswani • Bluestock Capstone Project"
)