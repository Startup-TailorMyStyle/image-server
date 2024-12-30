from fastapi import HTTPException
from image_server.schema.product import ProductSchema
from image_server.service.product import ProductService
from fastapi import APIRouter

product_service = ProductService()
router = APIRouter()

@router.get("/products/{id}", response_model=ProductSchema)
def get_product(id: int):
    product = product_service.get_product_by_id(id)
    if not product:
        raise HTTPException(status_code=204)
    return ProductSchema.from_db_model(product)

@router.get("/products", response_model=list[ProductSchema]) 
def get_all_products():
    products = product_service.get_all_products()
    if not products:
        raise HTTPException(status_code=204)
    return [ProductSchema.from_db_model(p) for p in products]

@router.get("/products/category/{category}", response_model=list[ProductSchema])
def get_products_by_category(category: str):
    products = product_service.get_products_by_category(category)
    if not products:
        raise HTTPException(status_code=204)
    return [ProductSchema.from_db_model(p) for p in products]
