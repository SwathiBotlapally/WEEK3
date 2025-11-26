import pandas as pd

df = pd.read_csv("sales.csv")

df["Sales"] = df["Price"] * df["Quantity"]

total_sales = df["Sales"].sum()

product_sales = df.groupby("Product")["Sales"].sum()
best_product = product_sales.idxmax()
best_product_sales = product_sales.max()

report = f"""SALES ANALYSIS REPORT
---------------------
Total Sales: {total_sales}

Best Selling Product: {best_product}
Sales from Best Product: {best_product_sales}

Product-wise Sales:
{product_sales}
"""

with open("report.txt", "w") as f:
    f.write(report)

print(report)
