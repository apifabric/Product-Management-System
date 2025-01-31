# coding: utf-8
from sqlalchemy import DECIMAL, DateTime  # API Logic Server GenAI assist
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

########################################################################################################################
# Classes describing database for SqlAlchemy ORM, initially created by schema introspection.
#
# Alter this file per your database maintenance policy
#    See https://apilogicserver.github.io/Docs/Project-Rebuild/#rebuilding
#
# Created:  January 31, 2025 15:42:43
# Database: sqlite:////tmp/tmp.Nz6TGNCfnZ-01JJYGDVXRCF2JAFXY7YYZJEGD/Product_Management_System/database/db.sqlite
# Dialect:  sqlite
#
# mypy: ignore-errors
########################################################################################################################
 
from database.system.SAFRSBaseX import SAFRSBaseX, TestBase
from flask_login import UserMixin
import safrs, flask_sqlalchemy, os
from safrs import jsonapi_attr
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.sql.sqltypes import NullType
from typing import List

db = SQLAlchemy() 
Base = declarative_base()  # type: flask_sqlalchemy.model.DefaultMeta
metadata = Base.metadata

#NullType = db.String  # datatype fixup
#TIMESTAMP= db.TIMESTAMP

from sqlalchemy.dialects.sqlite import *

if os.getenv('APILOGICPROJECT_NO_FLASK') is None or os.getenv('APILOGICPROJECT_NO_FLASK') == 'None':
    Base = SAFRSBaseX   # enables rules to be used outside of Flask, e.g., test data loading
else:
    Base = TestBase     # ensure proper types, so rules work for data loading
    print('*** Models.py Using TestBase ***')



class Product(Base):  # type: ignore
    """
    description: This table represents all available products for sale and purchase, complete with unique identifiers, descriptions, photo URLs, and unit types.
    """
    __tablename__ = 'product'
    _s_collection_name = 'Product'  # type: ignore

    id = Column(Integer, primary_key=True)
    description = Column(String, nullable=False)
    photo_url = Column(String)
    unit_type = Column(String)

    # parent relationships (access parent)

    # child relationships (access children)
    ProductTransactionList : Mapped[List["ProductTransaction"]] = relationship(back_populates="product")
    ProductVariantList : Mapped[List["ProductVariant"]] = relationship(back_populates="product")



class ProductTransaction(Base):  # type: ignore
    """
    description: This table logs product transactions, identifying whether they were sales or purchases, along with quantities and timestamps.
    """
    __tablename__ = 'product_transaction'
    _s_collection_name = 'ProductTransaction'  # type: ignore

    id = Column(Integer, primary_key=True)
    product_id = Column(ForeignKey('product.id'))
    transaction_type = Column(String)
    quantity = Column(Integer)
    transaction_date = Column(DateTime)

    # parent relationships (access parent)
    product : Mapped["Product"] = relationship(back_populates=("ProductTransactionList"))

    # child relationships (access children)



class ProductVariant(Base):  # type: ignore
    """
    description: This table holds different variants for each product (e.g., size and color), with a link back to the parent product.
    """
    __tablename__ = 'product_variant'
    _s_collection_name = 'ProductVariant'  # type: ignore

    id = Column(Integer, primary_key=True)
    product_id = Column(ForeignKey('product.id'))
    size = Column(String)
    color = Column(String)

    # parent relationships (access parent)
    product : Mapped["Product"] = relationship(back_populates=("ProductVariantList"))

    # child relationships (access children)
