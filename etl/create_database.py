import sqlite3

conn = sqlite3.connect("database/mutual_fund.db")

with open("database/schema.sql", "r") as f:
    schema = f.read()

conn.executescript(schema)

conn.commit()
conn.close()

print("Database Created Successfully!")