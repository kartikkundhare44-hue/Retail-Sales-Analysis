import pandas as pd

data = pd.read_csv("dataset/retail_sales.csv")

print("Original shape:")
print(data.shape)

# Missing values
print("\nMissing values:")
print(data.isnull().sum())

# Duplicate records
print("\nDuplicate rows:")
print(data.duplicated().sum())

# Remove duplicates
data = data.drop_duplicates()

# Convert date
data["Order_Date"] = pd.to_datetime(data["Order_Date"])

# Fill missing values
data["Customer_Name"] = data["Customer_Name"].fillna("Unknown")
data["City"] = data["City"].fillna("Unknown")
data["Discount"] = data["Discount"].fillna(data["Discount"].median())

print("\nAfter cleaning:")
print(data.isnull().sum())

# Save cleaned dataset
data.to_csv("dataset/retail_sales_cleaned.csv", index=False)

print("\nCleaned dataset saved successfully.")