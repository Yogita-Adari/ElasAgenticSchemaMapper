import pandas as pd
from sqlalchemy import Table, Column, Integer, String, MetaData, Float
from db import get_connection, engine

metadata = MetaData()

def create_sales_table():
    sales_table = Table(
        'sales', metadata,
        Column('id', Integer, primary_key=True, autoincrement=True),
        Column('employee_id', Integer),
        Column('customer_id', Integer),
        Column('type_sale', String),
        Column('amount_spent', Float),
        Column('optional1', String),
        Column('optional2', String)
    )
    metadata.create_all(engine)
    print("✅ Sales table created successfully!")

def insert_sales_data(csv_path):
    df = pd.read_csv(csv_path)
    df.to_sql('sales', con=engine, if_exists='append', index=False)
    print(f"✅ {len(df)} records inserted successfully into sales table.")

if __name__ == "__main__":
    create_sales_table()
    insert_sales_data("sales.csv")
