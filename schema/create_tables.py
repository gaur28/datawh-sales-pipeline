from sqlalchemy import create_engine, Column, Integer, String, Float, Date, ForeignKey, MetaData, Table
from sqlalchemy.orm import declarative_base

engine = create_engine('sqlite:///db/sales_dw.db')
Base = declarative_base()
metadata = MetaData()

# Dimension Table
class DimDate(Base):
    __tablename__ = 'dim_date'
    date_id = Column(Integer, primary_key=True)
    date = Column(Date)
    day = Column(Integer)
    month = Column(Integer)
    quarter = Column(Integer)
    year = Column(Integer)

class DimCustomer(Base):
    __tablename__= "dim_customer"
    customer_id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    gender = Column(String)
    age = Column(Integer)
    join_date = Column(Date)
    
class DimProduct(Base):
    __tablename__ = 'dim_product'
    product_id = Column(Integer, primary_key=True)
    product_name = Column(String)
    category = Column(String)
    price = Column(Float)

class DimRegion(Base):
    __tablename__ = "dim_region"
    region_id = Column(Integer, primary_key=True)
    region_name = Column(String)
    country = Column(String)

# Fact Table
class FactSales(Base):
    __tablename__ = "fact_sales"
    sale_id = Column(Integer, primary_key=True)
    date_id = Column(Integer, ForeignKey('dim_date.date_id'))
    # date_id = Column(Integer, ForeignKey('dim_date.date_id'))
    customer_id = Column(Integer, ForeignKey('dim_customer.customer_id'))
    product_id = Column(Integer, ForeignKey('dim_product.product_id'))
    region_id = Column(Integer, ForeignKey('dim_region.region_id'))
    quantity_sold = Column(Integer)
    total_amount = Column(Float)
    
# ---------------------
# Create all tables
# ---------------------

if __name__ == '__main__':
    Base.metadata.create_all(engine)
    print("All tables created successfully in sales_dw.db")
