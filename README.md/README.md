
# Retail Sales Analysis

## Project Overview

The **Retail Sales Analysis** project focuses on analyzing retail sales data to understand sales performance, profitability, product categories, and regional trends. The project uses Python, SQL, and Power BI to clean data, perform analysis, create visualizations, and present business insights.

## Objectives

- Clean and prepare retail sales data for analysis.
- Identify sales and profit trends across product categories and regions.
- Analyze product performance and sales patterns.
- Explore the relationship between discounts and profit.
- Use SQL to work with retail sales data.
- Build an interactive Power BI dashboard for business reporting.
- Explore machine learning techniques for sales analysis.

## Tools and Technologies

| Tool | Purpose |
|---|---|
| Python | Data processing and analysis |
| Pandas | Data cleaning and manipulation |
| Matplotlib | Data visualization |
| SQL / MySQL | Querying and analyzing structured data |
| Power BI | Dashboard creation and reporting |
| Scikit-learn | Machine learning experiments |
| Git and GitHub | Version control and project sharing |

## Project Workflow

1. **Data Collection** — Load the original retail sales dataset.
2. **Data Understanding** — Examine the dataset structure, columns, and data quality.
3. **Data Cleaning** — Handle duplicate records, missing values, and date formats.
4. **Data Analysis** — Explore sales, profit, categories, regions, and products.
5. **SQL Analysis** — Store and query retail data using MySQL.
6. **Data Visualization** — Create charts to identify patterns and trends.
7. **Machine Learning** — Explore regression and classification techniques.
8. **Power BI Dashboard** — Present key metrics and business trends.
9. **Reporting** — Summarize findings to support business decisions.

## Dataset Information

The project uses a retail sales CSV dataset.

Key columns include:

- `Order_ID`
- `Order_Date`
- `Customer_ID`
- `Customer_Name`
- `Category`
- `Sub_Category`
- `Product`
- `Region`
- `City`
- `Quantity`
- `Sales`
- `Discount`
- `Profit`

The cleaned dataset is saved as `retail_sales_cleaned.csv`.

## Data Cleaning

The data-cleaning process includes:

- Checking dataset dimensions and missing values.
- Identifying and removing duplicate records.
- Converting order dates into a proper date format.
- Filling missing customer names and city values with `Unknown`.
- Filling missing discount values using the median.
- Exporting the cleaned dataset for further analysis.

## Analysis and Visualizations

The project explores the following business questions:

- Which product categories generate the most sales?
- Which categories generate the highest profit?
- How do sales vary across regions?
- What are the monthly sales trends?
- Which products perform best by sales?
- How are discounts related to profit?

## Machine Learning

The project includes experiments with:

- **Linear Regression:** Exploring sales prediction.
- **Random Forest Classification:** Exploring high-profit and low-profit classification.
- **K-Means Clustering:** A possible extension for customer segmentation, if implemented.

Model results should be interpreted carefully, and the features used for prediction should be checked to avoid data leakage.

## Power BI Dashboard

The planned dashboard includes key performance indicators and visuals such as:

- Total Sales
- Total Profit
- Total Orders
- Profit Margin
- Sales Trend
- Sales by Category
- Sales by Region
- Top Products
- Year, Category, Region, and Sub-Category filters

Add your dashboard screenshots to this README after uploading them to the repository.

## Project Structure

```text
Retail-Sales-Analysis/
├── dataset/
│   ├── retail_sales.csv
│   └── retail_sales_cleaned.csv
├── python/
│   ├── 02_data_cleaning.py
│   └── 04_visualization.py
├── README.md
└── .gitignore
```

*This is a simplified structure. Update it if your actual project contains additional scripts, SQL files, or dashboard files.*

## How to Run

1. Clone or download this repository.
2. Install the required Python libraries:

   ```bash
   pip install pandas matplotlib scikit-learn
   ```

3. Place the source dataset in the `dataset/` folder.
4. Run the data-cleaning script from the project root:

   ```bash
   python python/02_data_cleaning.py
   ```

5. Run the visualization script if its dependencies and paths are configured:

   ```bash
   python python/04_visualization.py
   ```

6. Open the Power BI report, if included in the repository, to explore the dashboard.

## Key Learnings

- Data cleaning and preprocessing using Python.
- Exploratory data analysis and visualization.
- SQL and MySQL for structured data analysis.
- Business performance analysis using sales and profit metrics.
- Power BI dashboard development.
- Introductory machine learning workflows.
- Project version control using Git and GitHub.

## Data Privacy

Do not upload confidential customer information, private datasets, credentials, or other sensitive files to a public repository. Share only data and screenshots that are safe to make public.

## Conclusion

This project demonstrates an end-to-end retail data analysis workflow, from data preparation and exploration to visualization, dashboard reporting, and machine learning experimentation. It provides practice in using data tools to understand retail performance and communicate findings.

---

**Author:** Kartik Kundhare  
**Project:** Retail Sales Analysis
