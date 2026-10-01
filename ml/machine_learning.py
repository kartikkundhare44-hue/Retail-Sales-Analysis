import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.cluster import KMeans

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score,
    accuracy_score,
    classification_report,
    silhouette_score
)

from sklearn.preprocessing import StandardScaler


# =========================================================
# LOAD DATA
# =========================================================

data = pd.read_csv("dataset/retail_sales_cleaned.csv")

print("=" * 60)
print("DATASET INFORMATION")
print("=" * 60)

print("Shape:", data.shape)
print("\nColumns:")
print(data.columns.tolist())


# =========================================================
# REGRESSION
# Predict Sales
# =========================================================

print("\n")
print("=" * 60)
print("1. REGRESSION - PREDICT SALES")
print("=" * 60)

# Select numeric columns
numeric_columns = data.select_dtypes(include=np.number).columns.tolist()

print("\nNumeric columns:")
print(numeric_columns)

# We need Sales as target
if "Sales" not in data.columns:
    raise ValueError("Sales column not found in dataset.")

# Use numeric columns except Sales as features
regression_features = [
    col for col in numeric_columns
    if col != "Sales"
]

if len(regression_features) == 0:
    raise ValueError("No numeric features available for Sales prediction.")

X = data[regression_features].copy()
y = data["Sales"].copy()

# Fill missing values
X = X.fillna(X.median())
y = y.fillna(y.median())

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create model
regression_model = LinearRegression()

# Train model
regression_model.fit(X_train, y_train)

# Prediction
y_pred = regression_model.predict(X_test)

# Evaluation
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print("\nFeatures used:")
print(regression_features)

print("\nRegression Evaluation:")
print("MAE :", mae)
print("MSE :", mse)
print("RMSE:", rmse)
print("R²  :", r2)


# =========================================================
# CLASSIFICATION
# High Profit / Low Profit
# =========================================================

print("\n")
print("=" * 60)
print("2. CLASSIFICATION - HIGH PROFIT / LOW PROFIT")
print("=" * 60)

if "Profit" not in data.columns:
    raise ValueError("Profit column not found in dataset.")

# Create profit category using median profit
profit_median = data["Profit"].median()

data["Profit_Level"] = np.where(
    data["Profit"] >= profit_median,
    "High Profit",
    "Low Profit"
)

print("\nProfit threshold:", profit_median)

print("\nClass distribution:")
print(data["Profit_Level"].value_counts())

# Use numeric features except Profit
classification_features = [
    col for col in numeric_columns
    if col not in ["Profit"]
]

# Don't use the target itself
if len(classification_features) == 0:
    raise ValueError("No features available for classification.")

X = data[classification_features].copy()
y = data["Profit_Level"]

# Fill missing values
X = X.fillna(X.median())

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Create Random Forest model
classification_model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

# Train
classification_model.fit(X_train, y_train)

# Prediction
y_pred = classification_model.predict(X_test)

# Evaluation
accuracy = accuracy_score(y_test, y_pred)

print("\nFeatures used:")
print(classification_features)

print("\nClassification Accuracy:")
print(accuracy)

print("\nClassification Report:")
print(classification_report(y_test, y_pred))


# =========================================================
# CLUSTERING
# Customer Segmentation
# =========================================================

print("\n")
print("=" * 60)
print("3. CLUSTERING - CUSTOMER SEGMENTATION")
print("=" * 60)

if "Customer_Name" not in data.columns:
    raise ValueError(
        "Customer_Name column not found. "
        "Check the actual customer column name."
    )

# Create customer-level summary
customer_data = data.groupby("Customer_Name").agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum"),
    Number_of_Orders=("Customer_Name", "count")
).reset_index()

print("\nCustomer summary:")
print(customer_data.head())

# Features for clustering
cluster_features = [
    "Total_Sales",
    "Total_Profit",
    "Number_of_Orders"
]

X_cluster = customer_data[cluster_features].copy()

# Fill missing values
X_cluster = X_cluster.fillna(0)

# Standardize features
scaler = StandardScaler()

X_scaled = scaler.fit_transform(X_cluster)

# Create K-Means model
kmeans = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

# Fit clustering model
customer_data["Cluster"] = kmeans.fit_predict(X_scaled)

# Silhouette score
silhouette = silhouette_score(
    X_scaled,
    customer_data["Cluster"]
)

print("\nNumber of clusters: 3")

print("\nSilhouette Score:")
print(silhouette)

print("\nCustomer Segments:")
print(customer_data.head(10))

print("\nCluster counts:")
print(customer_data["Cluster"].value_counts())


# =========================================================
# SAVE CUSTOMER SEGMENTS
# =========================================================

customer_data.to_csv(
    "dataset/customer_segments.csv",
    index=False
)

print("\nCustomer segmentation saved successfully.")

print("\n")
print("=" * 60)
print("MACHINE LEARNING COMPLETED")
print("=" * 60)