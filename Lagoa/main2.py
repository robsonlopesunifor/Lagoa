from fastapi import FastAPI
from fastapi import status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from pydantic import BaseModel

app = FastAPI()


class Product(BaseModel):
    name: str | None = None
    price: float | None = None


@app.post("/product/")
def create_product(product: Product):
    status_code = status.HTTP_201_CREATED
    product_list = {"name": "leite", "price": 4.80}
    response = jsonable_encoder(product_list)
    return JSONResponse(content=response, status_code=status_code)


@app.get("/product/")
def list_product():
    status_code = status.HTTP_200_OK
    product_list = [{"name": "leite", "price": 4.80}]
    response = jsonable_encoder(product_list)
    return JSONResponse(content=response, status_code=status_code)


@app.get("/product/{product_id}")
def detail_product(product_id: str):
    status_code = status.HTTP_200_OK
    product_list = {"name": "leite", "price": 4.80}
    response = jsonable_encoder(product_list)
    return JSONResponse(content=response, status_code=status_code)


@app.put("/product/{product_id}")
def update_product(product_id: str, product: Product):
    status_code = status.HTTP_200_OK
    product_list = {"name": "leite", "price": 5.00}
    response = jsonable_encoder(product_list)
    return JSONResponse(content=response, status_code=status_code)
