import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import os

# Customer model from create_tables
# from Schema.create_tables import DimCustomer, Base
# from Schema.create_tables import DimCustomer, Base
from schema.create_tables import DimCustomer, Base

engine = create_engine('sqlite:///db/sales_dw.db')
Sessionmaker = sessionmaker(bind=engine)
session = Sessionmaker()

# read customer data
csv_path = os.path.join('data', 'customers.csv')
df = pd.read_csv(csv_path)

def load_customers():
    print("Loading customers...")
    for _, row in df.iterrows():
        customer = DimCustomer(
            customer_id=row['customer_id'],
            name=row['name'],
            email=row['email'],
            gender=row['gender'],
            age=int(row['age']),
           join_date=datetime.strptime(row['join_date'], "%Y-%m-%d")
        )
        session.merge(customer)
    session.commit()
    print("Customers loaded into dim_customer table.")

if __name__ == '__main__':
    load_customers()