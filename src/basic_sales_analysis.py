import pandas as pd
from pathlib import Path

# Find project folder
project_root = Path(__file__).resolve().parents[1]

# Load dataset
data_path = project_root / "data" / "restaurant_sales_sample.csv"
df = pd.read_csv(data_path)

# Create total sales column
df["total_sales"] = df["quantity"] * df["unit_price"]

# Basic analysis
print("Restaurant Sales Analysis")
print("-------------------------")

print("\nFirst 5 rows:")
print(df.head())

print("\nTotal Revenue:")
print(df["total_sales"].sum())

print("\nTotal Orders:")
print(df["order_id"].nunique())

print("\nSales by Category:")
print(df.groupby("category")["total_sales"].sum())

print("\nTop Selling Items:")
print(df.groupby("item")["quantity"].sum().sort_values(ascending=False))

print("\nPayment Method Analysis:")
print(df.groupby("payment_method")["total_sales"].sum())
