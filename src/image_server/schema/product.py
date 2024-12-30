from pydantic import BaseModel
from decimal import Decimal
from typing import Optional
from image_server.db.models.product import Product

class Rating(BaseModel):
    rate: Optional[Decimal] = None
    count: Optional[int] = None

class ProductSchema(BaseModel):
    id: int
    title: str
    price: Decimal
    description: Optional[str] = None
    category: str
    image: Optional[str] = None
    rating: Rating

    class Config:
        from_attributes = True

    @classmethod
    def from_db_model(cls, db_product: Product):
        return cls(
            id=db_product.id,
            title=db_product.title,
            price=db_product.price,
            description=db_product.description,
            category=db_product.category,
            image=db_product.image,
            rating=Rating(
                rate=db_product.rating_rate,
                count=db_product.rating_count
            )
        )
