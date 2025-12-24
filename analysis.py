# Sales Data Analysis
# Author: Swathi
# Description: Analyze sales data to calculate total revenue,
# best-selling product, and generate a clean report

import pandas as pd

# ---------------------------
# Load the dataset
# ---------------------------
df = pd.read_csv("sales_data.csv")

# ---------------------------
# Explore the data
# ---------------------------
print("📌 Dataset Shape:", df.shape)
print("\n📌 Column Names:")
print(df.columns)
print("\n📌 Data Types:")
print(df.dtypes)

# ---------------------------
# Data Cleaning
# ---------------------------

# Check for missing values
print("\n📌 Missing Values:")
print(df.isnull().sum())

# Fill missing values if any
df['Quantity'] = df['Quantity'].fillna(0)
df['Price'] = df['Price'].fillna(0)
df['Total_Sales'] = df['Total_Sales'].fillna(df['Quantity'] * df['Price'])

# Remove duplicate rows
df = df.drop_duplicates()

# ---------------------------
# Sales Analysis
# ---------------------------

# 1. Total Revenue
total_revenue = df['Total_Sales'].sum()

# 2. Best-Selling Product (by Total Sales)
product_sales = df.groupby('Product')['Total_Sales'].sum()
best_selling_product = product_sales.idxmax()
best_selling_amount = product_sales.max()

# 3. Average Sales per Order
average_sales = df['Total_Sales'].mean()

# ---------------------------
# Display Report
# ---------------------------
print("\n📊 SALES DATA ANALYSIS REPORT")
print("=" * 35)
print(f"Total Revenue: ₹{total_revenue:,.2f}")
print(f"Best-Selling Product: {best_selling_product}")
print(f"Revenue from Best-Selling Product: ₹{best_selling_amount:,.2f}")
print(f"Average Sales per Transaction: ₹{average_sales:,.2f}")
print("=" * 35)
print("✅ Analysis completed successfully")
