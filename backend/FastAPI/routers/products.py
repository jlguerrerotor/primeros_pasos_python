# Si Arrancamos el servidor mediante $ uvicorn users:app --reload, no funciona ya que la instancia arranca con el fichero users
# Para que funcione, hay que crear en main 2 routers, uno para users i otro para products.
# Además hay que definir los objetos como APIRouter
from fastapi import APIRouter

router = APIRouter()

# GET de Products
@router.get("/products/")
async def products():
    return ["Producto 1","Producto 2","Producto 3","Producto 4","Producto 5"]