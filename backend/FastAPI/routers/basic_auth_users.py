from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel # Para poder definir objetos.
# Importamos las clases encargadas de la autenticación en FastAPI:
# OAuth2PasswordBearer -> Se encarga de gestionar la autenticación (usuario y contraseña)
# OAuth2PasswordRequestForm -> Forma en la que se va a enviar a nuestra API los criterios de autenticación
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

router = APIRouter()

oauth2 = OAuth2PasswordBearer(tokenUrl="login")

# Entidad User. Objeto que implementa el comportamiento de BaseModel. Esto hace que podamos convertirlo directamente en un JSON
class User(BaseModel):
    username: str
    full_name: str
    email: str
    disabled: bool

class UserDB(User):
    password: str

users_db = {
    "mouredev": {
        "username": "mouredev",
        "full_name": "Brais Moure",
        "email": "braismoure@mouredev.com",
        "disabled": False,
        "password": "123456" # El password debería estar encriptado pero por simplicidad lo hacemos en claro
    },
    "mouredev2": {
        "username": "mouredev2",
        "full_name": "Brais Moure 2",
        "email": "braismoure2@mouredev.com",
        "disabled": True,
        "password": "654321"
    }
}

def search_user_db(username: str):
    if username in users_db:
        return UserDB(**users_db[username])

def search_user(username: str):
    if username in users_db:
        return User(**users_db[username])

async def current_user(token: str = Depends(oauth2)):
    user = search_user(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales de auteticación inválidas", 
            headers={"www_Authenticate": "Bearer"}
        ) # Lanza la excepción indicada
    
    if user.disabled:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Usuario inactivo"
        )
    
    return user

@router.post("/login")
# Depends indica que depende de algo, en este caso de los datos que entrega el formulario
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="El usuario no existe") # Lanza la excepción indicada
    
    user = search_user_db(form.username)
    if not form.password == user.password:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="La contraseña no es correcta") # Lanza la excepción indicada
    
    # El access_token debería ser una clave única encriptada. Para simplificar lo definimos como el username
    return {"access_token": user.username, "token_type": "bearer"}

@router.get("/users/me")
async def me(user: User = Depends(current_user)):
    return user

# CONTRASEÑA INCORRECTA
# 1. http://127.0.0.1:8000/login -> Para autenticarnos
# 2. Creamos un formulario en el POST donde pasamos username y password. El passwor que pasamos es incorrecto.
# 3. Accede a la función login entregando la excepción {"detail": "La contraseña no es correcta"}. 
#    Al comparar el username respecto al que tenemos en BD coinciden. Por tanto continúa.
#    Al comparar la contraseña respecto a la que tenemos en BD ve que no son la misma y lanza la excepción.

# CONTRASEÑA CORRECTA
# 1. POST http://127.0.0.1:8000/login -> Para autenticarnos
# 2. Creamos un formulario en el Body del POST donde pasamos username y password. El password que pasamos es incorrecto.
# 3. Accede a la función login entregando el usuario encontrado {"access_token": "mouredev", "token_type": "bearer"}. 
#    Al comparar el username respecto al que tenemos en BD coinciden. Por tanto continúa.
#    Al comparar la contraseña respecto a la que tenemos en BD también coinciden y devuelve el token.
#    El token debería guardarlo ya que lo necesitaré en cada llamada a la API para que me reconozca como usuario autenticado.

# NO PASAMOS TOKEN BEARER
# 1. GET http://127.0.0.1:8000/user/me -> Operación autenticada que depende de la función current_user que esta, a su vez, depende 
#    de oauth2.
# 2. No se ha pasado TOKEN en el Auth / Bearer
# 3. Accede a la función current_user y al no encontrar el token lanza la excepción {"detail": "Not authenticated"}, 
#    debido a la Dependencia de oauth2

# PASAMOS TOKEN BEARER INCORRECTO
# 1. GET http://127.0.0.1:8000/user/me -> Operación autenticada que depende de la función current_user que esta, a su vez, depende 
#    de oauth2.
# 2. Se ha pasado TOKEN en el Auth / Bearer (mouredevdev). Este token NO coincide con el access_token y por lo tanto devuelve la
#    excepción {"detail": "Credenciales de auteticación inválidas"}
# 3. Accede a la función de dependencia current_user, que a su vez depende de oauth2, que ahora SÍ tiene un token.
# 4. Buscamos el User correspondiente a ese TOKEN. Como NO lo ha encontrado, devuelve la excepción.

# PASAMOS TOKEN BEARER CORRECTO
# 1. GET http://127.0.0.1:8000/user/me -> Operación autenticada que depende de la función current_user que esta, a su vez, depende 
#    de oauth2.
# 2. Se ha pasado TOKEN en el Auth / Bearer (mouredev). Este token coincide con el access_token y por lo tanto devuelve el User
#    {"username": "mouredev","full_name": "Brais Moure","email": "braismoure@mouredev.com","disabled": false}
# 3. Accede a la función de dependencia current_user, que a su vez depende de oauth2, que ahora SÍ tiene un token.
# 4. Buscamos el User correspondiente a ese TOKEN. Al encontrarlo, ahora devuelve el User.

# USUARIO INACTIVO
# 1. GET http://127.0.0.1:8000/user/me -> Operación autenticada que depende de la función current_user que esta, a su vez, depende 
#    de oauth2.
# 2. Se ha pasado TOKEN en el Auth / Bearer (mouredev2). Este token coincide con el access_token y por lo tanto pasa a comprobar si está activo.
#    Como moredev2 no está activo, devuelve la excepción {"detail": "Usuario inactivo"}
