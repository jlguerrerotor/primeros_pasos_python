# Arrancar el servidor mediante $ uvicorn users:app --reload
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel # Para poder definir objetos.

router = APIRouter(prefix="/users",
                   tags=["Users"], # Usado para agrupar la Documentación
                   responses={404: {"message":"No encontrado"}})

# Entidad User. Objeto que implementa el comportamiento de BaseModel. Esto hace que podamos convertirlo directamente en un JSON
class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int

users_list = [User(id=1, name="Joan Lluís", surname="Guerrero", url="https://moure.dev", age=50),
         User(id=2, name="Lluís", surname="Torta", url="https://mouredev.com", age=35),
         User(id=3, name="Andrea", surname="Peris", url="https://andre.com", age=20)]

'''
@router.get("/usersjson")
async def usersjson():
    return [{"name":"Joan Lluís","surname":"Guerrero","url":"https://moure.dev","age":50},
            {"name":"Lluís","surname":"Torta","url":"https://mouredev.com","age":34},
            {"name":"Andrea","surname":"Peris","url":"https://andre.com","age":20}]
'''

# GET de Users
@router.get("/")
async def users():
    return users_list

# GET - Parámetros de PATH
# Se suele usar para parámetros que són obligatorios y fijos
@router.get("/{id}") # Parámetros a través del path http://127.0.0.1:8000/user/2
async def user(id: int):
    return search_user(id)

# GET - Parametros de Query
# Se suele usar para parámetros que pueden NO ser obligatorios
# Ejemplo devolver un nº determinado de usuarios cuaddo hay muchos (Paginación)
@router.get("/") # Parámetros a través de query http://127.0.0.1:8000/user/?id=2
async def user(id: int):
    return search_user(id)

# POST de User
# Insertar datos
# http://127.0.0.1:8000/user/ -> JSON {"id":4,"name":"Cinta","surname":"Peris","url":"https://moure.cat","age":45}
# status_code indica el codigo de mensaje que queremos que devuelva por defecto si la operación sale bien. 201 -> Creado
# response_molde indica (de cara a la documentación) el tipo de objeto que devuelve la función
@router.post("/", response_model=User, status_code=201)
async def user(user: User):
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code=204,detail="El usuario ya existe") # Lanza la excepción indicada
    else: # Este else no haria falta ponerlo ya que en el if hace un return
        users_list.append(user)
        return user

# PUT de User
# Modificar un dato (edad)
# http://127.0.0.1:8000/user/ -> JSON {"id":4,"name":"Cinta","surname":"Peris","url":"https://moure.cat","age":18}
@router.put("/")
async def user(user: User):
    found = False
    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True
    if not found:
        return {"error":"No se ha actualizado el usuario"}
    else: # Este else no haria falta ponerlo ya que en el if hace un return
        return user

# DELETE de User
# Eliminar un usuario
# http://127.0.0.1:8000/user/4
@router.delete("/{id}")
async def user(id: int):
    found = False
    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            found = True
    if not found:
        return {"error":"No se ha eliminado el usuario"}
    else: # Este else no haria falta ponerlo ya que en el if hace un return
        return {"id": id}


def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list) # Buscamos el usuario en la lista
    try: 
        return list(users)[0] # Devuelve el usuario encontrado si existe
    except: # Si no ha encontrado ningún usuario devuelve un error en formato JSON
        return {"error":"No se ha encontrado el usuario"}

