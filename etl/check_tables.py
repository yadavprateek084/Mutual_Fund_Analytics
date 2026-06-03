import sqlite3
import pandas as pd

conn = sqlite3.connect("database/mutual_fund.db")

tables = [
    "dim_fund",
    "fact_nav",
    "fact_aum",
    "fact_sip",
    "fact_category_inflows",
    "fact_folio",
    "fact_performance",
    "fact_transactions",
    "fact_holdings",
    "fact_benchmark"
]

for table in tables:
    query = f"SELECT COUNT(*) as row_count FROM {table}"
    result = pd.read_sql(query, conn)

    print(f"\n{table}")
    print(result)

conn.close()