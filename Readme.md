# Mutual Fund Analytics Capstone Project

## Overview

The **Mutual Fund Analytics Capstone Project** is an end-to-end data analytics solution built to analyze mutual fund performance, investor behavior, and risk metrics using Python, SQL, and Power BI.

The project covers the full analytics lifecycle:

* Data Ingestion (ETL)
* Data Cleaning
* SQL Database Design
* Exploratory Data Analysis (EDA)
* Performance Analytics
* Advanced Risk Metrics
* Dashboard Development
* Final Reporting

This project was developed as part of the **Bluestock Fintech Internship Program**.

---

# Project Objectives

The key objectives of this project are:

* Build a structured ETL pipeline for mutual fund datasets
* Design a relational database schema using SQLite
* Perform data cleaning and transformation
* Conduct exploratory data analysis
* Evaluate mutual fund performance using advanced financial metrics
* Analyze investor cohorts and SIP continuity
* Develop a simple fund recommender system
* Build an interactive Power BI dashboard

---

# Tech Stack

## Programming

* Python 3.x
* SQL (SQLite)

## Libraries Used

* Pandas
* NumPy
* Matplotlib
* Seaborn
* Plotly
* SciPy

## Visualization

* Power BI

## Version Control

* Git
* GitHub

---

# Project Structure

```bash
bluestock_mf_capstone/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── 01_data_ingestion.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_eda_analysis.ipynb
│   ├── 04_performance_analytics.ipynb
│   └── 06_advanced_analytics.ipynb
│
├── sql/
│   ├── schema.sql
│   └── queries.sql
│
├── scripts/
│   ├── recommender.py
│   └── run_pipeline.py
│
├── reports/
│   ├── Final_Report.pdf
│   ├── Bluestock_MF_Presentation.pptx
│   └── rolling_sharpe_chart.png
│
├── dashboard/
│   └── Mutual_Fund_Dashboard.pbix
│
├── bluestock_mf.db
├── requirements.txt
└── README.md
```

---

# Data Sources

The project uses the following datasets:

| Dataset               | Description                            |
| --------------------- | -------------------------------------- |
| NAV History           | Daily mutual fund NAV values           |
| AUM Data              | Assets Under Management by fund houses |
| SIP Data              | Monthly SIP inflow trends              |
| Category Inflows      | Net inflow by fund category            |
| Investor Transactions | Investor-level transaction records     |
| Portfolio Holdings    | Stock allocation across sectors        |
| Benchmark Indices     | NIFTY50 and NIFTY100 historical data   |

---

# ETL Pipeline

The ETL pipeline consists of:

## Extract

Loading raw CSV files into Python.

## Transform

Data cleaning:

* Null handling
* Date formatting
* Duplicate removal
* Standardization

## Load

Loading cleaned data into SQLite database.

Database tables:

* dim_fund
* fact_nav
* fact_aum
* fact_sip
* fact_category_inflows
* fact_folio
* fact_transactions
* fact_holdings
* fact_benchmark

---

# Exploratory Data Analysis (EDA)

The project includes:

* NAV Trend Analysis
* AUM Growth Analysis
* SIP Inflow Analysis
* Category Inflow Heatmaps
* Investor Demographics
* Geographic Distribution
* Folio Growth
* Correlation Matrix
* Sector Allocation

---

# Performance Analytics

Computed metrics:

* CAGR
* Sharpe Ratio
* Sortino Ratio
* Alpha
* Beta
* Maximum Drawdown
* Fund Scorecard Ranking

Outputs:

```bash
returns_computed.csv
cagr_report.csv
sharpe_values.csv
sortino_values.csv
alpha_beta.csv
max_drawdown.csv
fund_scorecard.csv
```

---

# Advanced Risk Analytics

Implemented:

* Historical VaR (95%)
* Conditional VaR (CVaR)
* Rolling 90-Day Sharpe
* Investor Cohort Analysis
* SIP Continuity Analysis
* Sector HHI Concentration
* Fund Recommendation Engine

Outputs:

```bash
var_cvar_report.csv
cohort_analysis.csv
sip_risk_flags.csv
recommender.py
rolling_sharpe_chart.png
```

---

# Power BI Dashboard

The dashboard provides:

* Fund NAV Trends
* AUM Comparison
* SIP Inflow Trends
* Investor Demographics
* Risk Metrics
* Benchmark Comparison
* Top Fund Rankings

Dashboard file:

```bash
dashboard/Mutual_Fund_Dashboard.pbix
```

---

# Installation

Clone repository:

```bash
git clone <your_repo_url>
cd bluestock_mf_capstone
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# How to Run

Run ETL:

```bash
python scripts/run_pipeline.py
```

Run recommender:

```bash
python scripts/recommender.py
```

Open notebooks:

```bash
jupyter notebook
```

---

# Key Insights

* SBI Mutual Fund dominates AUM share
* Equity funds attracted the highest inflows
* SIP inflows reached all-time highs in 2025
* Younger investors drive mutual fund participation
* T30 cities contribute the largest investments
* Top funds consistently outperform benchmarks
* High Sharpe funds provide better risk-adjusted returns

---

# Future Improvements

* Live NAV API integration
* Machine Learning-based recommendation system
* Real-time dashboard refresh
* Investor personalization engine
* Cloud deployment

---

# Author

**Prateek Yadav**
B.Tech CSE
Bluestock Fintech Intern

---

# Version

**v1.0**
Final submission of Bluestock Mutual Fund Analytics Capstone.
