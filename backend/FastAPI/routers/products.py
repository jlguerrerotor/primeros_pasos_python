# Si Arrancamos el servidor mediante $ uvicorn users:app --reload, no funciona ya que la instancia arranca con el fichero users
# Para que funcione, hay que crear en main 2 routers, uno para users i otro para products.
# Además hay que definir los objetos como APIRouter
from fastapi import APIRouter

router = APIRouter(prefix="/products", 
                   tags=["products"], # Usado para agrupar la Documentación
                   responses={404: {"message": "No encontrado"}})

products_list = ["Producto 1","Producto 2","Producto 3","Producto 4","Producto 5"]

# GET de Products
@router.get("/")
async def products():
    return products_list

@router.get("/{id}")
async def products(id: int):
    return products_list[id]
