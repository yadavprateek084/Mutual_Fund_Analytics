import pandas as pd
from sqlalchemy import create_engine

# SQLite Database Connection
engine = create_engine("sqlite:///database/mutual_fund.db")

# Load CSV Files

fund_master = pd.read_csv("data/raw/01_fund_master.csv")
nav_history = pd.read_csv("data/raw/02_nav_history.csv")
aum = pd.read_csv("data/raw/03_aum_by_fund_house.csv")
sip = pd.read_csv("data/raw/04_monthly_sip_inflows.csv")
category = pd.read_csv("data/raw/05_category_inflows.csv")
folio = pd.read_csv("data/raw/06_industry_folio_count.csv")
performance = pd.read_csv("data/raw/07_scheme_performance.csv")
transactions = pd.read_csv("data/raw/08_investor_transactions.csv")
holdings = pd.read_csv("data/raw/09_portfolio_holdings.csv")
benchmark = pd.read_csv("data/raw/10_benchmark_indices.csv")

# Load into SQLite

fund_master.to_sql("dim_fund", engine, if_exists="replace", index=False)
nav_history.to_sql("fact_nav", engine, if_exists="replace", index=False)
aum.to_sql("fact_aum", engine, if_exists="replace", index=False)
sip.to_sql("fact_sip", engine, if_exists="replace", index=False)
category.to_sql("fact_category_inflows", engine, if_exists="replace", index=False)
folio.to_sql("fact_folio", engine, if_exists="replace", index=False)
performance.to_sql("fact_performance", engine, if_exists="replace", index=False)
transactions.to_sql("fact_transactions", engine, if_exists="replace", index=False)
holdings.to_sql("fact_holdings", engine, if_exists="replace", index=False)
benchmark.to_sql("fact_benchmark", engine, if_exists="replace", index=False)

print("All datasets loaded successfully!")