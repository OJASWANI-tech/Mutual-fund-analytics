import sqlite3

conn = sqlite3.connect("bluestock_mf.db")
cursor = conn.cursor()

tables = [
    "dim_fund",
    "fact_nav",
    "fact_transactions",
    "fact_performance",
    "fact_aum"
]

for table in tables:
    cursor.execute(f"SELECT COUNT(*) FROM {table}")
    print(table, cursor.fetchone()[0])

conn.close()