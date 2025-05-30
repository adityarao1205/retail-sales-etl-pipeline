# Retail Sales ETL Pipeline with Python and SQL

This project demonstrates a complete ETL (Extract, Transform, Load) pipeline using Python and SQLite. The goal is to simulate a multi-store retail business, clean and transform the data, load it into a SQL database, and analyze key metrics through SQL queries and visualizations.

## 🔧 Technologies Used

- Python (Pandas, SQLite3)
- SQL (via SQLite)
- Matplotlib (for visualization)
- Google Colab

## 📊 Dataset

Synthetic sales data for 100 orders across 3 stores and 5 products. Each row includes:

- OrderID
- Product Name
- Category
- Store
- Quantity
- Price
- Date

## 🚀 Process Overview

### 1. Extract

Load raw CSV data using Pandas.

### 2. Transform

Clean the data and calculate `TotalRevenue` using:

TotalRevenue = Quantity \* Price

### 3. Load

Store the transformed data into a SQLite database using `sqlite3`.

## 🧠 SQL Insights

- Total revenue per store
- Top 5 products by revenue
- Daily revenue trend over time

## 📈 Visualization

Used Matplotlib to plot daily revenue trend.

## 📁 Files

- `retail_sales.csv` – generated dataset
- `etl_pipeline.py` – main Python script
- `retail_sales.db` – SQLite database (auto-created)
- `README.md` – project overview
