# Arrancar el servidor mediante $ uvicorn users:app --reload
from fastapi import FastAPI

app = FastAPI()

# GET de Products
@app.get("/products/")
async def products():
    return ["Producto 1","Producto 2","Producto 3","Producto 4","Producto 5"]