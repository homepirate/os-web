from fastapi import FastAPI
import uvicorn
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles


class ProductCategory:
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description


class Product:
    def __init__(self, id, name, price, description, category):
        self.id = id
        self.name = name
        self.price = price
        self.description = description
        self.category = category


category1 = ProductCategory(1, "Electronics", "Category for electronic devices")
category2 = ProductCategory(2, "Clothing", "Category for clothing items")
category3 = ProductCategory(3, "Books", "Category for books")

product1 = Product(1, "Laptop", 1000, "A high-performance laptop", category1)
product2 = Product(2, "T-shirt", 20, "A casual cotton t-shirt", category2)
product3 = Product(3, "Python Crash Course", 30, "A book for Python beginners", category3)

# Создаем списки с объектами
product_categories = [category1, category2, category3]
products = [product1, product2, product3]

app = FastAPI()
app.mount('/static', StaticFiles(directory='static'), name='static')


@app.get("/")
async def main_page():
    return FileResponse('static/index.html')


@app.get("/health")
async def health_check():
    return {"status": "ok"}


@app.get("/category")
async def get_category():
    return product_categories


@app.get("/products")
async def get_category():
    return products

if __name__ == "__main__":
    uvicorn.run(app, port=8000)
