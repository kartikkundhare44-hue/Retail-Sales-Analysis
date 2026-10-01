import pandas as pd
import matplotlib.pyplot as plt
import os

# Load cleaned dataset
data = pd.read_csv("dataset/retail_sales_cleaned.csv")

# Create images folder if it does not exist
os.makedirs("images", exist_ok=True)


# =========================================================
# Chart 1: Sales by Category
# =========================================================

sales_category = data.groupby("Category")["Sales"].sum()

plt.figure(figsize=(8, 5))
sales_category.plot(kind="bar")

plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("images/sales_by_category.png")
plt.show()
plt.close()


# =========================================================
# Chart 2: Profit by Category
# =========================================================

profit_category = data.groupby("Category")["Profit"].sum()

plt.figure(figsize=(8, 5))
profit_category.plot(kind="bar")

plt.title("Profit by Category")
plt.xlabel("Category")
plt.ylabel("Total Profit")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("images/profit_by_category.png")
plt.show()
plt.close()


# =========================================================
# Chart 3: Sales by Region
# =========================================================

sales_region = data.groupby("Region")["Sales"].sum()

plt.figure(figsize=(8, 5))
sales_region.plot(kind="bar")

plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("images/sales_by_region.png")
plt.show()
plt.close()


# =========================================================
# Chart 4: Monthly Sales Trend
# =========================================================

data["Order_Date"] = pd.to_datetime(data["Order_Date"])

monthly_sales = data.groupby(
    data["Order_Date"].dt.to_period("M")
)["Sales"].sum()

monthly_sales.index = monthly_sales.index.astype(str)

plt.figure(figsize=(10, 5))
monthly_sales.plot(kind="line", marker="o")

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()

plt.savefig("images/monthly_sales_trend.png")
plt.show()
plt.close()


# =========================================================
# Chart 5: Top 10 Products
# =========================================================

top_products = data.groupby("Product")["Sales"].sum().sort_values(
    ascending=False
).head(10)

plt.figure(figsize=(10, 6))
top_products.sort_values().plot(kind="barh")

plt.title("Top 10 Products by Sales")
plt.xlabel("Total Sales")
plt.ylabel("Product")
plt.tight_layout()

plt.savefig("images/top_10_products.png")
plt.show()
plt.close()


# =========================================================
# Chart 6: Discount vs Profit
# =========================================================

plt.figure(figsize=(8, 5))

plt.scatter(
    data["Discount"],
    data["Profit"],
    alpha=0.5
)

plt.title("Discount vs Profit")
plt.xlabel("Discount")
plt.ylabel("Profit")
plt.grid(True)
plt.tight_layout()

plt.savefig("images/discount_vs_profit.png")
plt.show()
plt.close()


print("\nAll 6 charts created successfully!")
print("Charts saved inside the images folder.")