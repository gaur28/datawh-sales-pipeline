Sales Data Warehouse Project

This project implements a basic Data Warehouse using Python, SQLite, and Pandas. It covers the full ETL (Extract, Transform, Load) pipeline, mock data generation, analytical queries, and exporting reports to Excel.

📁 Project Structure

Basic Data Warehouse/
├── Schema/               # SQLAlchemy model definitions
├── etl/                  # ETL scripts to load data into DW
├── data/                 # Mock CSV data files
├── db/                   # SQLite database file
├── output/               # Generated Excel reports
├── main.py               # Entry point to run full ETL pipeline
└── queries_report.py     # Runs analytical queries and exports Excel

✅ Features Covered

1. Data Warehouse Schema

Star schema includes:

dim_customer: Customer details

dim_product: Product information

dim_region: Geographical data

fact_sales: Sales facts linked to all dimension tables

2. Mock Data Creation

Created realistic CSV files under data/:

customer.csv

product.csv

region.csv

sales.csv

3. ETL Pipeline

Each ETL script reads from CSV and loads into the SQLite database (sales_dw.db):

load_dim_customer.py

load_dim_product.py

load_dim_region.py

load_fact_sales.py

Handled data parsing, type conversions, and foreign key assignments.

4. Orchestration with main.py

main.py calls all ETL scripts in sequence.

Outputs progress logs and confirms successful loading of each table.

5. Analytical Reporting

Wrote SQL queries in queries_report.py:

Total Sales by Region

Total Quantity Sold by Product

Top 5 Customers by Purchase Amount

6. Export to Excel

Used Pandas and XlsxWriter to export query results to output/sales_report.xlsx.

Each result is written to a separate sheet in the workbook.

📊 Sample Reports (Excel Output)

Filename: output/sales_report.xlsx

Sheet 1: Total Sales by Region

Sheet 2: Total Quantity Sold by Product

Sheet 3: Top 5 Customers by Total Purchase

⚡ Technologies Used

Python 3.10

SQLite3

Pandas

SQLAlchemy

XlsxWriter

✍ Author

Tushar Gaur

📅 Project Status

✅ Phase 1: Schema, ETL, Reports completed
