import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'etl')))

from load_dim_customer import load_customers
from load_dim_products import load_products
from load_dim_region import load_regions
from load_fact_sales import load_sales

def run_etl():
    print("Starting ETL Pipeline")
    load_customers()
    load_products()
    load_regions()
    load_sales()
    
    print("ETL Pipeline completed!....")
    
if __name__ == "__main__":
    run_etl()