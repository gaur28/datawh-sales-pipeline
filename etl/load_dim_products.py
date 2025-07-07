import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from schema.create_tables import DimProduct

engine = create_engine('sqlite:///db/sales_dw.db')
Session = sessionmaker(bind=engine)
session = Session()

def load_products():
    print("🔄 Loading products...")
    df = pd.read_csv(os.path.join('data', 'products.csv'))
    for _, row in df.iterrows():
        product = DimProduct(
            product_id=row['product_id'],
            product_name=row['product_name'],
            category=row['category'],
            price=row['price']
        )
        session.merge(product)
    session.commit()
    print("✅ Products loaded into dim_product table.")

if __name__ == '__main__':
    load_products()