from sqlalchemy import create_engine, Column, Integer, String, Text, DECIMAL, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class ProductCategory(Base):
    __tablename__ = 'product_category'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    description = Column(Text)
    created_at = Column(TIMESTAMP, server_default='CURRENT_TIMESTAMP')
    modified_at = Column(TIMESTAMP, server_default='CURRENT_TIMESTAMP', onupdate='CURRENT_TIMESTAMP')
    deleted_at = Column(TIMESTAMP)

class Product(Base):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    description = Column(Text)
    SKU = Column(String(50), unique=True)
    category_id = Column(Integer, ForeignKey('product_category.id'))
    inventory_id = Column(Integer)
    price = Column(DECIMAL(10, 2), nullable=False)
    discount_id = Column(Integer)
    created_at = Column(TIMESTAMP, server_default='CURRENT_TIMESTAMP')
    modified_at = Column(TIMESTAMP, server_default='CURRENT_TIMESTAMP', onupdate='CURRENT_TIMESTAMP')
    deleted_at = Column(TIMESTAMP)

    category = relationship("ProductCategory")


engine = create_engine('sqlite:///product.db')
Base.metadata.create_all(engine)
