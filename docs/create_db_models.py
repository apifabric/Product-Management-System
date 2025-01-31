# using resolved_model self.resolved_model FIXME
# created from response, to create create_db_models.sqlite, with test data
#    that is used to create project
# should run without error in manager 
#    if not, check for decimal, indent, or import issues

import decimal
import logging
import sqlalchemy
from sqlalchemy.sql import func 
from decimal import Decimal
from logic_bank.logic_bank import Rule
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, Date, DateTime, Numeric, Boolean, Text, DECIMAL
from sqlalchemy.types import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from datetime import date   
from datetime import datetime
from typing import List


logging.getLogger('sqlalchemy.engine.Engine').disabled = True  # remove for additional logging

Base = declarative_base()  # from system/genai/create_db_models_inserts/create_db_models_prefix.py


from sqlalchemy.dialects.sqlite import *

class Product(Base):
    """description: This table represents all available products for sale and purchase, complete with unique identifiers, descriptions, photo URLs, and unit types."""
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True)
    description = Column(String, nullable=False)
    photo_url = Column(String)
    unit_type = Column(String)

class ProductVariant(Base):
    """description: This table holds different variants for each product (e.g., size and color), with a link back to the parent product."""
    __tablename__ = 'product_variant'
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('product.id'))
    size = Column(String)
    color = Column(String)

class ProductTransaction(Base):
    """description: This table logs product transactions, identifying whether they were sales or purchases, along with quantities and timestamps."""
    __tablename__ = 'product_transaction'
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('product.id'))
    transaction_type = Column(String)
    quantity = Column(Integer)
    transaction_date = Column(DateTime, default=datetime.utcnow)


# end of model classes


try:
    
    
    # ALS/GenAI: Create an SQLite database
    import os
    mgr_db_loc = True
    if mgr_db_loc:
        print(f'creating in manager: sqlite:///system/genai/temp/create_db_models.sqlite')
        engine = create_engine('sqlite:///system/genai/temp/create_db_models.sqlite')
    else:
        current_file_path = os.path.dirname(__file__)
        print(f'creating at current_file_path: {current_file_path}')
        engine = create_engine(f'sqlite:///{current_file_path}/create_db_models.sqlite')
    Base.metadata.create_all(engine)
    
    
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # ALS/GenAI: Prepare for sample data
    
    
    session.commit()
    product1 = Product(id=1, description='Smartphone', photo_url='http://example.com/smartphone.jpg', unit_type='unit')
    product2 = Product(id=2, description='Laptop', photo_url='http://example.com/laptop.jpg', unit_type='unit')
    product3 = Product(id=3, description='Milk', photo_url='http://example.com/milk.jpg', unit_type='liter')
    product4 = Product(id=4, description='Bread', photo_url='http://example.com/bread.jpg', unit_type='unit')
    variant1 = ProductVariant(id=1, product_id=1, size='Large', color='Black')
    variant2 = ProductVariant(id=2, product_id=2, size='15-inch', color='Silver')
    variant3 = ProductVariant(id=3, product_id=3, size='1-liter', color='White')
    variant4 = ProductVariant(id=4, product_id=4, size='Medium', color='Brown')
    transaction1 = ProductTransaction(id=1, product_id=1, transaction_type='sale', quantity=5, transaction_date=datetime(2023, 10, 5))
    transaction2 = ProductTransaction(id=2, product_id=2, transaction_type='purchase', quantity=8, transaction_date=datetime(2023, 10, 6))
    transaction3 = ProductTransaction(id=3, product_id=3, transaction_type='sale', quantity=10, transaction_date=datetime(2023, 10, 7))
    transaction4 = ProductTransaction(id=4, product_id=4, transaction_type='purchase', quantity=2, transaction_date=datetime(2023, 10, 8))
    
    
    
    session.add_all([product1, product2, product3, product4, variant1, variant2, variant3, variant4, transaction1, transaction2, transaction3, transaction4])
    session.commit()
    # end of test data
    
    
except Exception as exc:
    print(f'Test Data Error: {exc}')
