import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Page Configuration
st.set_page_config(
    page_title="Bluestock MF Analytics",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Advanced Professional Styling (Dark Glassmorphic UI)
st.markdown("""
<style>
    /* Main Background & Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    html, body, [data-testid="stAppViewContainer"] {
        background-color: #0d1117 !important;
        font-family: 'Inter', sans-serif !important;
        color: #c9d1d9 !important;
    }
    
    /* Header Customization */
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Inter', sans-serif !important;
        font-weight: 700 !important;
        color: #ffffff !important;
        letter-spacing: -0.5px;
    }
    
    /* Main container padding */
    .block-container {
        padding-top: 2rem !important;
        padding-bottom: 3rem !important;
        max-width: 1200px;
    }

    /* Premium Metric Card Styling */
    [data-testid="stMetric"] {
        background: rgba(22, 27, 34, 0.8) !important;
        border: 1px solid rgba(48, 54, 61, 0.8) !important;
        border-radius: 14px !important;
        padding: 20px 24px !important;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2) !important;
        transition: transform 0.2s ease, border-color 0.2s ease;
    }
    [data-testid="stMetric"]:hover {
        transform: translateY(-2px);
        border-color: #58a6ff !important;
    }
    [data-testid="stMetricLabel"] {
        color: #8b949e !important;
        font-weight: 500 !important;
        font-size: 0.85rem !important;
        text-transform: uppercase !important;
        letter-spacing: 0.5px !important;
    }
    [data-testid="stMetricValue"] {
        color: #f0f6fc !important;
        font-size: 1.8rem !important;
        font-weight: 700 !important;
    }

    /* Sidebar Customization */
    section[data-testid="stSidebar"] {
        background-color: #161b22 !important;
        border-right: 1px solid #30363d !important;
    }
    section[data-testid="stSidebar"] .stRadio > label {
        color: #8b949e !important;
        font-weight: 600;
    }
    
    /* Tabs Customization */
    button[data-baseweb="tab"] {
        color: #8b949e !important;
        font-size: 1rem !important;
        font-weight: 500 !important;
    }
    button[data-baseweb="tab"][aria-selected="true"] {
        color: #58a6ff !important;
        border-bottom-color: #58a6ff !important;
    }

    /* Clean Dividers */
    hr {
        border-color: rgba(48, 54, 61, 0.6) !important;
    }
</style>
""", unsafe_allow_html=True)

# 3. Load Data
@st.cache_data
def load_data():
    return pd.read_csv("data/processed/07_scheme_performance_cleaned.csv")

perf_df = load_data()

# 4. Sidebar Layout
st.sidebar.markdown("<h2 style='margin-bottom:0;'>📊 Bluestock</h2>", unsafe_allow_html=True)
st.sidebar.markdown("<p style='color:#8b949e; font-size:0.9rem; margin-top:0;'>Smart Mutual Fund Dashboard</p>", unsafe_allow_html=True)
st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Navigation",
    ["📈 Dashboard", "🎯 Fund Recommender", "🔍 Category Explorer"]
)

st.sidebar.markdown("---")
st.sidebar.markdown(
    "<div style='background-color:#21262d; padding:12px; border-radius:8px; border: 1px solid #30363d; color:#8b949e; font-size:0.85rem; text-align:center;'>"
    "Built for <b>Bluestock Capstone Project</b>"
    "</div>", 
    unsafe_allow_html=True
)

# 5. Main Header
st.title("Bluestock Mutual Fund Analytics Platform")
st.markdown("<p style='color:#8b949e; font-size:1.1rem; margin-top:-10px;'>End-to-End Mutual Fund Intelligence Dashboard</p>", unsafe_allow_html=True)
st.markdown("---")

# 6. Global KPI Row
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Funds Tracker", len(perf_df))

with col2:
    st.metric("Top Sharpe Ratio", round(perf_df["sharpe_ratio"].max(), 2))

with col3:
    st.metric("Avg 3Y Return", f"{round(perf_df['return_3yr_pct'].mean(), 2)}%")

with col4:
    st.metric("Total Assets Under Management", f"₹{round(perf_df['aum_crore'].sum()/1000, 2)}K Cr")

st.markdown("---")

# Plotly Theme Defaults Configuration
plotly_layout_args = {
    'paper_bgcolor': 'rgba(0,0,0,0)',
    'plot_bgcolor': 'rgba(0,0,0,0)',
    'font_color': '#c9d1d9',
    'font_family': 'Inter'
}

# 7. Dynamic Navigation Pages
if "Dashboard" in page:
    tab1, tab2 = st.tabs(["📊 Performance Overview", "🔬 Deep-Dive Analytics"])

    with tab1:
        col1, col2 = st.columns([1.3, 1])

        with col1:
            st.markdown("### Top 10 Funds by Risk-Adjusted Return (Sharpe)")
            top10 = perf_df.sort_values("sharpe_ratio", ascending=False).head(10)
            st.dataframe(top10, use_container_width=True)

        with col2:
            st.markdown("### Asset Allocation by Category")
            pie_fig = px.pie(
                perf_df,
                names="category",
                hole=0.5,
                template="plotly_dark",
                color_discrete_sequence=px.colors.qualitative.Safe
            )
            pie_fig.update_layout(**plotly_layout_args)
            pie_fig.update_traces(textposition='inside', textinfo='percent+label')
            st.plotly_chart(pie_fig, use_container_width=True, config={'displayModeBar': False})

    with tab2:
        st.markdown("### Risk vs Return Analysis (3-Year Horizon)")
        scatter_fig = px.scatter(
            perf_df,
            x="return_3yr_pct",
            y="std_dev_ann_pct",
            size="aum_crore",
            color="category",
            hover_name="scheme_name",
            labels={"return_3yr_pct": "3-Year Annual Return (%)", "std_dev_ann_pct": "Volatility / Standard Deviation (%)"},
            template="plotly_dark",
            color_discrete_sequence=px.colors.qualitative.Safe
        )
        scatter_fig.update_layout(**plotly_layout_args)
        scatter_fig.update_xaxes(showgrid=True, gridcolor='#30363d')
        scatter_fig.update_yaxes(showgrid=True, gridcolor='#30363d')
        st.plotly_chart(scatter_fig, use_container_width=True)

elif "Recommender" in page:
    st.markdown("### 🎯 Fund Recommendation Engine")
    st.markdown("<p style='color:#8b949e;'>Filter schemes optimized by highest Sharpe Ratio matching your risk tier.</p>", unsafe_allow_html=True)

    risk = st.selectbox(
        "Select Your Risk Profile Target:",
        ["Low", "Moderate", "High"]
    )

    filtered = perf_df[perf_df["risk_grade"].str.lower() == risk.lower()]
    top_recommend = filtered.sort_values("sharpe_ratio", ascending=False).head(3)

    st.markdown(f"#### Top 3 Best Performing {risk}-Risk Mutual Funds")
    st.dataframe(top_recommend, use_container_width=True)

elif "Category Explorer" in page:
    st.markdown("### 🔍 Category Sector Explorer")

    category = st.selectbox(
        "Choose Macro Asset Class Category:",
        perf_df["category"].unique()
    )

    filtered_cat = perf_df[perf_df["category"] == category]
    
    st.markdown(f"#### Registered Schemes under {category}")
    st.dataframe(filtered_cat, use_container_width=True)

    st.markdown("#### 3-Year Return Comparison across Schemes")
    bar_fig = px.bar(
        filtered_cat,
        x="scheme_name",
        y="return_3yr_pct",
        color="sharpe_ratio",
        labels={"scheme_name": "Scheme Title", "return_3yr_pct": "3Y Annualized Return (%)", "sharpe_ratio": "Sharpe Metric"},
        template="plotly_dark",
        color_continuous_scale="Viridis"
    )
    bar_fig.update_layout(**plotly_layout_args)
    bar_fig.update_xaxes(showgrid=False)
    bar_fig.update_yaxes(showgrid=True, gridcolor='#30363d')
    st.plotly_chart(bar_fig, use_container_width=True)

# 8. Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #8b949e; font-size: 0.85rem; padding: 10px 0;'>"
    "Built by <b>Ojaswani</b> • Powered by Bluestock Mutual Fund Analytics Capstone Engine"
    "</div>",
    unsafe_allow_html=True
)