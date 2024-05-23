# Arrancar el servidor mediante $ uvicorn users:app --reload
from fastapi import FastAPI
from pydantic import BaseModel # Para poder definir objetos.

app = FastAPI()

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

@app.get("/usersjson")
async def usersjson():
    return [{"name":"Joan Lluís","surname":"Guerrero","url":"https://moure.dev","age":50},
            {"name":"Lluís","surname":"Torta","url":"https://mouredev.com","age":34},
            {"name":"Andrea","surname":"Peris","url":"https://andre.com","age":20}]

# GET de Users
@app.get("/users")
async def users():
    return users_list

# GET - Parámetros de PATH
# Se suele usar para parámetros que són obligatorios y fijos
@app.get("/user/{id}") # Parámetros a través del path http://127.0.0.1:8000/user/2
async def user(id: int):
    return search_user(id)

# GET - Parametros de Query
# Se suele usar para parámetros que pueden NO ser obligatorios
# Ejemplo devolver un nº determinado de usuarios cunado hay muchos
@app.get("/user/") # Parámetros a través de query http://127.0.0.1:8000/user/?id=2
async def user(id: int):
    return search_user(id)

def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list) # Buscamos el usuario en la lista
    try: 
        return list(users)[0] # Devuelve el usuario encontrado si existe
    except: # Si no ha encontrado ningún usuario devuelve un error en formato JSON
        return {"error":"No se ha encontrado el usuario"}

