
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

# Extract
df = pd.read_csv("retail_sales.csv")

# Transform
df["Revenue"] = df["Quantity"] * df["Price"]

# Load
conn = sqlite3.connect("retail_sales.db")
df.to_sql("retail_sales", conn, if_exists="replace", index=False)

# SQL Queries
query1 = """
SELECT Store, SUM(Revenue) as TotalRevenue
FROM retail_sales
GROUP BY Store
ORDER BY TotalRevenue DESC
"""

query2 = """
SELECT Product, SUM(Revenue) as TotalRevenue
FROM retail_sales
GROUP BY Product
ORDER BY TotalRevenue DESC
LIMIT 5
"""

query3 = """
SELECT Date, SUM(Revenue) as DailyRevenue
FROM retail_sales
GROUP BY Date
ORDER BY Date ASC
"""

result1 = pd.read_sql_query(query1, conn)
result2 = pd.read_sql_query(query2, conn)
result3 = pd.read_sql_query(query3, conn)

print("Total Revenue per Store:\n", result1)
print("\nTop 5 Products:\n", result2)
print("\nDaily Revenue Trend:\n", result3.head())

# Visualization
plt.figure(figsize=(10,5))
plt.plot(result3["Date"], result3["DailyRevenue"], marker='o')
plt.title("Daily Revenue Trend")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("daily_revenue_trend.png")
plt.show()

conn.close()
