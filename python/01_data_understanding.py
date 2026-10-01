import pandas as pd

# Load dataset
data = pd.read_csv("dataset/retail_sales.csv")

# Display first 5 rows
print("First 5 rows:")
print(data.head())

# Dataset shape
print("\nDataset Shape:")
print(data.shape)

# Column names
print("\nColumns:")
print(data.columns)

# Data types
print("\nData Types:")
print(data.dtypes)

# Dataset information
print("\nDataset Information:")
data.info()

# Statistical summary
print("\nStatistical Summary:")
print(data.describe())