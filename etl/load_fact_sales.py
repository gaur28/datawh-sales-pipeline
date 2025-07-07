import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from schema.create_tables import FactSales

engine = create_engine('sqlite:///db/sales_dw.db')
Session = sessionmaker(bind=engine)
session = Session()

def load_sales():
    print("🔄 Loading sales...")
    df = pd.read_csv(os.path.join('data', 'sales.csv'))
    for _, row in df.iterrows():
        date_id = int(datetime.strptime(row['date'], "%Y-%m-%d").strftime("%Y%m%d"))
        sale = FactSales(
            sale_id=row['sale_id'],
            date_id=date_id,
            customer_id=row['customer_id'],
            product_id=row['product_id'],
            region_id=row['region_id'],
            quantity_sold=row['quantity_sold'],
            total_amount=row['total_amount']
        )
        session.merge(sale)
    session.commit()
    print("✅ Sales loaded into fact_sales table.")

if __name__ == '__main__':
    load_sales()