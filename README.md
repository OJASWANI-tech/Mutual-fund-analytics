# Bluestock Mutual Fund Analytics Platform

## Project Overview

The **Bluestock Mutual Fund Analytics Platform** is an end-to-end financial analytics project designed to analyze mutual fund performance, investor behavior, and market trends using structured datasets.

This project integrates **ETL pipelines, exploratory data analysis (EDA), advanced performance analytics, risk measurement, and interactive Power BI dashboards** to provide meaningful investment insights.

 live website-https://bluestock-mf.streamlit.app/

The platform helps evaluate:

* Fund performance across multiple categories
* NAV trends over time
* SIP growth patterns
* Investor demographics and behavior
* Risk-adjusted returns
* Portfolio concentration
* Benchmark comparisons

This capstone simulates a real-world fintech analytics workflow.

---

# Objectives

* Build a complete ETL pipeline for mutual fund datasets
* Perform data cleaning and transformation
* Analyze NAV, AUM, SIP, and folio trends
* Compute advanced performance metrics
* Measure downside risk using VaR and CVaR
* Build an interactive Power BI dashboard
* Create a simple fund recommendation engine
* Generate final reports and insights

---

# Tech Stack

## Programming

* Python
* Pandas
* NumPy
* SciPy

## Data Visualization

* Matplotlib
* Seaborn
* Plotly
* Power BI

## Database

* SQLite

## Tools

* Jupyter Notebook
* VS Code
* Git
* GitHub

---

# Project Structure

```text
Mutual-Fund-Analytics/
│
├── data/
│   ├── raw/
│   ├── processed/
│
├── notebooks/
│   ├── EDA_Analysis.ipynb
│   ├── Performance_Analytics.ipynb
│   ├── Advanced_Analytics.ipynb
│
├── scripts/
│   ├── run_pipeline.py
│   ├── recommender.py
│
├── dashboard/
│   └── bluestock_mf_dashboard.pbix
│
├── reports/
│   ├── Dashboard.pdf
│   ├── Final_Report.pdf
│   ├── Bluestock_MF_Presentation.pptx
│   ├── var_cvar_report.csv
│   └── rolling_sharpe_chart.png
│
└── README.md
```

---

# Setup Instructions

## Step 1 — Clone Repository

```bash
git clone <repository_link>
cd Mutual-Fund-Analytics
```

---

## Step 2 — Install Dependencies

```bash
pip install pandas numpy matplotlib seaborn plotly scipy jupyter
```

---

# How to Run the ETL Pipeline

Run:

```bash
python scripts/run_pipeline.py
```

This pipeline:

* Reads raw datasets
* Cleans missing values
* Standardizes formats
* Creates processed datasets

---

# How to Run Analysis

## EDA Notebook

```bash
jupyter notebook notebooks/EDA_Analysis.ipynb
```

---

## Performance Analytics Notebook

```bash
jupyter notebook notebooks/Performance_Analytics.ipynb
```

---

## Advanced Analytics Notebook

```bash
jupyter notebook notebooks/Advanced_Analytics.ipynb
```

---

# Fund Recommender

Run:

```bash
python scripts/recommender.py
```

Input options:

* Low
* Moderate
* High

Output:

Top 3 recommended funds based on risk-adjusted performance.

---

# How to Open the Dashboard

Open the Power BI dashboard file:

```text
dashboard/bluestock_mf_dashboard.pbix
```

Dashboard pages include:

### Page 1 — Industry Overview

* Total AUM
* SIP Inflows
* Total Folios
* Total Schemes

---

### Page 2 — Fund Performance

* Risk vs Return Scatter Plot
* Fund Scorecard Table
* NAV vs Benchmark Comparison

---

### Page 3 — Investor Analytics

* State-wise transaction analysis
* Age-group investment behavior
* Transaction type split

---

### Page 4 — SIP & Market Trends

* SIP trend analysis
* Category inflow heatmap
* Top inflow categories

---

# Dataset Descriptions

| Dataset            | Description                        |
| ------------------ | ---------------------------------- |
| Fund Master        | Basic scheme metadata              |
| NAV History        | Daily NAV records for schemes      |
| AUM Data           | Assets under management by AMC     |
| SIP Inflows        | Monthly SIP contribution data      |
| Category Inflows   | Category-wise net inflows          |
| Folio Count        | Industry folio growth trends       |
| Scheme Performance | CAGR, Sharpe, Alpha, Beta          |
| Transactions       | Investor transaction records       |
| Portfolio Holdings | Fund stock allocation              |
| Benchmarks         | Nifty and market benchmark indices |

---

# Key Insights

* Equity funds outperformed during the 2023 bull market
* SIP inflows showed consistent growth
* Younger investors contributed strongly to SIP growth
* Mid-cap funds generated higher long-term CAGR
* Large-cap funds showed better stability
* Some portfolios had high concentration risk

---

# Future Scope

* Live NAV API integration
* Machine learning forecasting
* Portfolio optimization
* Real-time investor alerts
* Automated dashboard refresh

---

# Final Deliverables

* ETL Pipeline Scripts
* EDA Analysis Notebook
* Performance Analytics Notebook
* Advanced Analytics Notebook
* Power BI Dashboard
* Final Report
* Presentation Deck
* GitHub Repository

---

# Author

**Ojaswani**
Data Analyst Intern
Bluestock Mutual Fund Analytics Capstone Project
