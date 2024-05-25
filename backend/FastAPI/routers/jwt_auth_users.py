
### JWT -> JSON Web Token ###
# pip install "python-jose[cryptography]"
# pip install "passlib[bcrypt]"

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel # Para poder definir objetos.
# Importamos las clases encargadas de la autenticación en FastAPI:
# OAuth2PasswordBearer -> Se encarga de gestionar la autenticación (usuario y contraseña)
# OAuth2PasswordRequestForm -> Forma en la que se va a enviar a nuestra API los criterios de autenticación
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone
import os

ALGORITHM = "HS256"
ACCESS_TOKEN_DURATION = 1 # Tiempo de vida del TOKEN (1 min)
SECRET = os.urandom(22)

router = APIRouter()

oauth2 = OAuth2PasswordBearer(tokenUrl="login")

crypt = CryptContext(schemes=["bcrypt"])

# Entidad User. Objeto que implementa el comportamiento de BaseModel. Esto hace que podamos convertirlo directamente en un JSON
class User(BaseModel):
    username: str
    full_name: str
    email: str
    disabled: bool

class UserDB(User):
    password: str

# Encriptamos las contraseñas de BD
# https://bcrypt-generator.com/
users_db = {
    "mouredev": {
        "username": "mouredev",
        "full_name": "Brais Moure",
        "email": "braismoure@mouredev.com",
        "disabled": False,
        "password": "$2a$12$PByM3WRRyPTMM5XfnIOqx..zvOMt7eMYjU2LyDj4SKC.MEZ/KvYIK"
    },
    "mouredev2": {
        "username": "mouredev2",
        "full_name": "Brais Moure 2",
        "email": "braismoure2@mouredev.com",
        "disabled": True,
        "password": "$2a$12$rdl/WUHXYTOsO3VeZLnil.UjwDfDxzPioHXJsl9fjyoa9GODLc7nO"
    }
}

def search_user_db(username: str):
    if username in users_db:
        return UserDB(**users_db[username])

def search_user(username: str):
    if username in users_db:
        return User(**users_db[username])    

@router.post("/login")
# Depends indica que depende de algo, en este caso de los datos que entrega el formulario
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="El usuario no existe") # Lanza la excepción indicada
    
    user = search_user_db(form.username)

    # Comprobamos si el password que recibimos del form es el que está encriptado en la BD. Si coinciden, continúa.
    if not crypt.verify(form.password, user.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="La contraseña no es correcta") # Lanza la excepción indicada
    
    access_token_expiration = timedelta(minutes=ACCESS_TOKEN_DURATION) # Va a crear un delta que sea 1 min mas sobro lo que tenemos.
    expire = datetime.now(timezone.utc) + access_token_expiration # Hora exacta a la que expira el TOKEN

    access_token = {
        "sub": user.username,
        "exp": expire
    }

    # El access_token debería ser una clave única encriptada. Para simplificar lo definimos como el username
    return {"access_token": jwt.encode(access_token, SECRET, algorithm=ALGORITHM), "token_type": "bearer"}

async def auth_user(token: str = Depends(oauth2)):

    exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales de auteticación inválidas", 
            headers={"www_Authenticate": "Bearer"}        
        )  # Lanza la excepción indicada
    
    try:
        username = jwt.decode(token, SECRET, algorithms=[ALGORITHM]).get("sub")
        if username is None:
            raise exception
        
    except JWTError:
        raise exception

    return search_user(username)
    
async def current_user(user: User = Depends(auth_user)):
    if user.disabled:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Usuario inactivo"
        )
    
    return user

@router.get("/users/me")
async def me(user: User = Depends(current_user)):
    return user

# LOGIN OK
# 1. POST http://127.0.0.1:8000/login
# 2. Creamos un formulario en el Body del POST donde pasamos username y password. El password que pasamos es incorrecto.
# 3. Devuelve el token 
# {
#   "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJtb3VyZWRldiIsImV4cCI6MTcxNjYzNDY1OX0.hIxPzp1udfnFfedRLBq8ttOCzfD_Rbk_Nisa1xZCH18",
#   "token_type": "bearer"
# }
# 4. En https://jwt.io/ podemos desencriptar el token para ver su contenido