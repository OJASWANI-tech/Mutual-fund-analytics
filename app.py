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

# 2. Executive Soft-Theme Styling (Clean Light/Medium Corporate Palette)
st.markdown("""
<style>
    /* Professional Google/Stripe-like Modern Typography & Neutral Canvas */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    html, body, [data-testid="stAppViewContainer"] {
        background-color: #f8fafc !important; /* Soft cool-grey background */
        font-family: 'Inter', sans-serif !important;
        color: #1e293b !important;
    }
    
    /* Clean Sidebar Separation */
    section[data-testid="stSidebar"] {
        background-color: #ffffff !important;
        border-right: 1px solid #e2e8f0 !important;
    }

    /* Elegant Structural Title & Headers */
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Inter', sans-serif !important;
        font-weight: 700 !important;
        color: #0f172a !important;
        letter-spacing: -0.02em;
    }
    
    /* Spacious App View Padding */
    .block-container {
        padding-top: 2.5rem !important;
        padding-bottom: 3rem !important;
    }

    /* Premium SaaS-style White KPI Blocks */
    [data-testid="stMetric"] {
        background: #ffffff !important;
        border: 1px solid #e2e8f0 !important;
        border-radius: 12px !important;
        padding: 20px 22px !important;
        box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.05), 0 1px 2px -1px rgba(0, 0, 0, 0.05) !important;
    }
    [data-testid="stMetricLabel"] {
        color: #64748b !important;
        font-weight: 600 !important;
        font-size: 0.8rem !important;
        text-transform: uppercase !important;
        letter-spacing: 0.05em !important;
    }
    [data-testid="stMetricValue"] {
        color: #0f172a !important;
        font-size: 1.75rem !important;
        font-weight: 700 !important;
    }

    /* Custom Input and Typography Layout Refinements */
    .stRadio > label, .stSelectbox > label {
        color: #334155 !important;
        font-weight: 600 !important;
    }
    
    /* Dividers Line Color */
    hr {
        border-color: #e2e8f0 !important;
    }
</style>
""", unsafe_allow_html=True)

# 3. Load Data Safely
@st.cache_data
def load_data():
    return pd.read_csv("data/processed/07_scheme_performance_cleaned.csv")

perf_df = load_data()

# 4. Professional Corporate Sidebar
st.sidebar.markdown("<h2 style='margin-bottom:0; color:#0f172a;'>📊 Bluestock</h2>", unsafe_allow_html=True)
st.sidebar.markdown("<p style='color:#64748b; font-size:0.85rem; margin-top:0;'>Smart Mutual Fund Dashboard</p>", unsafe_allow_html=True)
st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Navigation System",
    ["📈 Performance Dashboard", "🎯 Fund Recommender", "🔍 Category Explorer"]
)

st.sidebar.markdown("---")
st.sidebar.markdown(
    "<div style='background-color:#f1f5f9; padding:12px; border-radius:8px; border: 1px solid #e2e8f0; color:#475569; font-size:0.8rem; text-align:center; font-weight:500;'>"
    "Built for <b>Bluestock Capstone Project</b>"
    "</div>", 
    unsafe_allow_html=True
)

# 5. Main Screen Frame Header
st.title("Bluestock Mutual Fund Analytics Platform")
st.markdown("<p style='color:#64748b; font-size:1.05rem; margin-top:-10px;'>End-to-End Mutual Fund Intelligence Dashboard</p>", unsafe_allow_html=True)
st.markdown("---")

# 6. Global Operational KPI Metrics
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Active Funds", len(perf_df))

with col2:
    st.metric("Peak Sharpe Ratio", round(perf_df["sharpe_ratio"].max(), 2))

with col3:
    st.metric("Average 3Y Return", f"{round(perf_df['return_3yr_pct'].mean(), 2)}%")

with col4:
    st.metric("Total Consolidated AUM", f"₹{round(perf_df['aum_crore'].sum()/1000, 2)}K Cr")

st.markdown("---")

# Neutral Clean Plotly Layout Standards
plotly_clean_args = {
    'paper_bgcolor': 'rgba(0,0,0,0)',
    'plot_bgcolor': 'rgba(0,0,0,0)',
    'font_color': '#334155',
    'font_family': 'Inter'
}

# 7. Navigation Engine Route Rules
if "Dashboard" in page:
    tab1, tab2 = st.tabs(["📊 Performance Overview", "🔬 Deep-Dive Analysis"])

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
                hole=0.4,
                template="plotly_white",
                color_discrete_sequence=px.colors.qualitative.Prism
            )
            pie_fig.update_layout(**plotly_clean_args)
            pie_fig.update_traces(textposition='inside', textinfo='percent')
            st.plotly_chart(pie_fig, use_container_width=True, config={'displayModeBar': False})

    with tab2:
        st.markdown("### Risk vs Return Matrix (3-Year Horizon)")
        scatter_fig = px.scatter(
            perf_df,
            x="return_3yr_pct",
            y="std_dev_ann_pct",
            size="aum_crore",
            color="category",
            hover_name="scheme_name",
            labels={"return_3yr_pct": "3-Year Return (%)", "std_dev_ann_pct": "Volatility / Std Dev (%)"},
            template="plotly_white",
            color_discrete_sequence=px.colors.qualitative.Prism
        )
        scatter_fig.update_layout(**plotly_clean_args)
        scatter_fig.update_xaxes(showgrid=True, gridcolor='#e2e8f0')
        scatter_fig.update_yaxes(showgrid=True, gridcolor='#e2e8f0')
        st.plotly_chart(scatter_fig, use_container_width=True)

elif "Recommender" in page:
    st.markdown("### 🎯 Fund Recommendation Engine")
    st.markdown("<p style='color:#64748b;'>Optimized model sorting schemes by alpha generation and risk tier limits.</p>", unsafe_allow_html=True)

    risk = st.selectbox(
        "Select Client Target Risk Profile:",
        ["Low", "Moderate", "High"]
    )

    filtered = perf_df[perf_df["risk_grade"].str.lower() == risk.lower()]
    top_recommend = filtered.sort_values("sharpe_ratio", ascending=False).head(3)

    st.markdown(f"#### Top 3 Recommended Schemes — {risk} Risk Tier")
    st.dataframe(top_recommend, use_container_width=True)

elif "Category Explorer" in page:
    st.markdown("### 🔍 Category Asset Class Explorer")

    category = st.selectbox(
        "Choose Macro Industry Portfolio Category:",
        perf_df["category"].unique()
    )

    filtered_cat = perf_df[perf_df["category"] == category]
    
    st.markdown(f"#### Active Funds under {category}")
    st.dataframe(filtered_cat, use_container_width=True)

    st.markdown("#### 3-Year Annual Return Performance Yield Comparison")
    bar_fig = px.bar(
        filtered_cat,
        x="scheme_name",
        y="return_3yr_pct",
        color="sharpe_ratio",
        labels={"scheme_name": "Scheme Name", "return_3yr_pct": "3Y Return (%)", "sharpe_ratio": "Sharpe Metric"},
        template="plotly_white",
        color_continuous_scale="Cividis"
    )
    bar_fig.update_layout(**plotly_clean_args)
    bar_fig.update_xaxes(showgrid=False)
    bar_fig.update_yaxes(showgrid=True, gridcolor='#e2e8f0')
    st.plotly_chart(bar_fig, use_container_width=True)

# 8. Clean Universal Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #64748b; font-size: 0.85rem; padding: 10px 0; font-weight: 500;'>"
    "Built by <b>Ojaswani</b> • Powered by Bluestock Mutual Fund Analytics Capstone Engine"
    "</div>",
    unsafe_allow_html=True
)