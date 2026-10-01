import pandas as pd

data = pd.read_csv("dataset/retail_sales_cleaned.csv")

# Total Sales
print("Total Sales:", data["Sales"].sum())

# Total Profit
print("Total Profit:", data["Profit"].sum())

# Total Quantity
print("Total Quantity:", data["Quantity"].sum())

# Average Sales
print("Average Sales:", data["Sales"].mean())

# Average Profit
print("Average Profit:", data["Profit"].mean())

# Sales by Category
print("\nSales by Category:")
print(
    data.groupby("Category")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

# Profit by Category
print("\nProfit by Category:")
print(
    data.groupby("Category")["Profit"]
    .sum()
    .sort_values(ascending=False)
)

# Sales by Region
print("\nSales by Region:")
print(
    data.groupby("Region")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

# Top 10 Products
print("\nTop 10 Products:")
print(
    data.groupby("Product")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)