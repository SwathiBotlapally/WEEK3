
import pandas as pd

# Load the dataset
df = pd.read_csv("sales_data.csv")

# ---------------------------
# Explore the data
# ---------------------------
print("Dataset Shape:", df.shape)
print("\nColumns:\n", df.columns)
print("\nData Types:\n", df.dtypes)

# ---------------------------
# Clean the data
# ---------------------------

# Handle missing values
df['Quantity'] = df['Quantity'].fillna(0)
df['Price'] = df['Price'].fillna(0)

# Recalculate Total_Sales if missing
df['Total_Sales'] = df['Quantity'] * df['Price']

# Remove duplicate rows
df = df.drop_duplicates()

# ---------------------------
# Analyze sales
# ---------------------------

# 1. Total Revenue
total_revenue = df['Total_Sales'].sum()

# 2. Best-Selling Product (by revenue)
best_product = df.groupby('Product')['Total_Sales'].sum().idxmax()
best_product_sales = df.groupby('Product')['Total_Sales'].sum().max()

# 3. Average Sales per Transaction
average_sales = df['Total_Sales'].mean()

# ---------------------------
# Display Report
# ---------------------------
print("\n📊 SALES ANALYSIS REPORT")
print("-" * 30)
print(f"Total Revenue: ₹{total_revenue:,.2f}")
print(f"Best-Selling Product: {best_product}")
print(f"Revenue from Best Product: ₹{best_product_sales:,.2f}")
print(f"Average Sales per Transaction: ₹{average_sales:,.2f}")
print("-" * 30)
print("Analysis completed successfully ✅")
