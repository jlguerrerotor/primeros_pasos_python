# Arrancar el servidor mediante $ uvicorn users:app --reload
from fastapi import APIRouter, HTTPException, status
from db.models.user import User
from db.client import db_client
from db.schemas.user import user_schema, users_schema
from bson import ObjectId

router = APIRouter(prefix="/userdb",
                   tags=["User DB"], # Usado para agrupar la Documentación
                   responses={status.HTTP_404_NOT_FOUND: {"message":"No encontrado"}})

# GET de Users http://127.0.0.1:8000/userdb
@router.get("/", response_model=list[User])
async def users():
    return users_schema(db_client.users.find())

# GET - Parámetros de PATH
# Se suele usar para parámetros que són obligatorios y fijos
@router.get("/{id}") # Parámetros a través del path http://127.0.0.1:8000/userdb/6654ad6f9217890b78ad66b2
async def user(id: str):
    return search_user("_id", ObjectId(id))

# GET - Parametros de Query
# Se suele usar para parámetros que pueden NO ser obligatorios
# Ejemplo devolver un nº determinado de usuarios cuaddo hay muchos (Paginación)
@router.get("/") # Parámetros a través de query http://127.0.0.1:8000/user/?id=2
async def user(id: str):
    return search_user("_id", ObjectId(id))

# POST de User
# Insertar datos
# http://127.0.0.1:8000/userdb -> JSON {"username": "brais","email": "brais@mouredev.com"}
# status_code indica el codigo de mensaje que queremos que devuelva por defecto si la operación sale bien. 201 -> Creado
# response_molde indica (de cara a la documentación) el tipo de objeto que devuelve la función
@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
async def user(user: User):
    if type(search_user("email",user.email)) == User:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="El usuario ya existe") # Lanza la excepción indicada
    # else: # Este else no haria falta ponerlo ya que en el if hace un return
    
    user_dict = dict(user)
    del user_dict["id"]

    id = db_client.users.insert_one(user_dict).inserted_id

    new_user = user_schema(db_client.users.find_one({"_id": id}))

    return User(**new_user)

# PUT de User
# Modificar un dato (edad)
# http://127.0.0.1:8000/userdb/ -> JSON {"id": "6654bcf9b2e79b0e8fbd9223", "username": "braismoure", "email": "brais@mouredev.com"}
@router.put("/", response_model=User)
async def user(user: User):
    
    user_dict = dict(user)
    del user_dict["id"]
    
    try:
        db_client.users.find_one_and_replace({"_id": ObjectId(user.id)}, user_dict)
    except:
        return {"error":"No se ha actualizado el usuario"}
    
    return search_user("_id", ObjectId(user.id))

# DELETE de User
# Eliminar un usuario
# http://127.0.0.1:8000/userdb/6654ad6f9217890b78ad66b2
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def user(id: str):
    found = db_client.users.find_one_and_delete({"_id": ObjectId(id)})

    if not found:
        return {"error":"No se ha eliminado el usuario"}

def search_user(field: str, key):
    try: 
        user = db_client.users.find_one({field: key})
        return User(**user_schema(user))
    except: # Si no ha encontrado ningún usuario devuelve un error en formato JSON
        return {"error":"No se ha encontrado el usuario"}
