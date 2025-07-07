from sqlalchemy import create_engine, text
import pandas as pd
import os

engine =  create_engine('sqlite:///db/sales_dw.db')

def run_query(title, query):
    print(f"\n{title}\n")
    with engine.connect() as conn:
        result = pd.read_sql_query(text(query), conn)
        print(result)

# 1. Total Sales by Region
query1 = """
SELECT r.region_name, SUM(f.total_amount) AS total_sales
FROM fact_sales f
JOIN dim_region r ON f.region_id = r.region_id
GROUP BY r.region_name
ORDER BY total_sales DESC
"""

# 2. Quantity Sold by Product
query2 = """
SELECT p.product_name, SUM(f.quantity_sold) AS total_quantity
FROM fact_sales f
JOIN dim_product p ON f.product_id = p.product_id
GROUP BY p.product_name
ORDER BY total_quantity DESC
"""

# 3. Top 5 Customers by Spending
query3 = """
SELECT c.name, SUM(f.total_amount) AS total_spent
FROM fact_sales f
JOIN dim_customer c ON f.customer_id = c.customer_id
GROUP BY c.name
ORDER BY total_spent DESC
LIMIT 5
"""

# Run queries
run_query("Total Sales by Region", query1)
run_query("Total Quantity Sold by Product", query2)
run_query("Top 5 Customers by Total Purchase", query3)

report_data = {}
with engine.connect() as conn:
    report_data["Total Sales by Region"] = pd.read_sql_query(text(query1), conn)
    report_data["Total Quantity Sold by Product"] = pd.read_sql_query(text(query2), conn)
    report_data["Top 5 Customers by Total Purchase"] = pd.read_sql_query(text(query3), conn)

    # Print preview
    for sheet, df in report_data.items():
        print(f"\n📊 {sheet} ({len(df)} rows):")
        print(df.head())

# Export to Excel
excel_path = "output/sales_report.xlsx"
with pd.ExcelWriter(excel_path, engine="xlsxwriter") as writer:
    for sheet_name, df in report_data.items():
        df.to_excel(writer, sheet_name=sheet_name[:31], index=False)

print(f"\n✅ All reports exported to: {os.path.abspath(excel_path)}")