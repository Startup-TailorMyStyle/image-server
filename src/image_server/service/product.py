from typing import Optional
from sqlalchemy.orm import Session
from sqlalchemy import Engine
from image_server.db.models.product import Product
from image_server.db.session import get_db_engine


class ProductService:
    def __init__(self, db_engine: Optional[Engine] = None):
        self.db_engine = db_engine or get_db_engine()

    def get_product_by_id(self, product_id: int) -> Product | None:
        """Get a product by its ID"""
        with Session(self.db_engine) as db:
            return db.query(Product).filter(Product.id == product_id).first()

    def get_products_by_category(self,category: str) -> list[Product]:
        """Get all products in a category"""
        with Session(self.db_engine) as db:
            return db.query(Product).filter(Product.category == category).all()

    def get_all_products(self) -> list[Product]:
        """Get all products"""
        with Session(self.db_engine) as db:
            return db.query(Product).all()

