import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from schema.create_tables import DimRegion

engine = create_engine('sqlite:///db/sales_dw.db')
Session = sessionmaker(bind=engine)
session = Session()

def load_regions():
    print("🔄 Loading regions...")
    df = pd.read_csv(os.path.join('data', 'regions.csv'))
    for _, row in df.iterrows():
        region = DimRegion(
            region_id=row['region_id'],
            region_name=row['region_name'],
            country=row['country']
        )
        session.merge(region)
    session.commit()
    print("✅ Regions loaded into dim_region table.")

if __name__ == '__main__':
    load_regions()