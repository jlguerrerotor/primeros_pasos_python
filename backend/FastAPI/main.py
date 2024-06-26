# Arrancar servidor UVICORN: uvicorn main:app --reload
# main es el fichero raíz que queremos arrancar
# :app es nuestra instancia de FastAPI
# --reload -> Hará que cambie el contexto del servidor cada vez que cambiemos el fichero main
# Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)


from fastapi import FastAPI
# Un router permite que se puedan lanzar peticiones al servidor sobre 2 ficheros de objeto distintos.
from routers.products import router as products_router
from routers.users import router as users_router
from routers.basic_auth_users import router as basic_auth_users_router
from routers.jwt_auth_users import router as jwt_auth_users_router
from routers.users_db import router as usersdb_router
from fastapi.staticfiles import StaticFiles # Imágenes, PDFs

app = FastAPI()

# Routers
app.include_router(products_router)
app.include_router(users_router)

app.include_router(basic_auth_users_router)
app.include_router(jwt_auth_users_router)

app.include_router(usersdb_router)

app.mount("/static", StaticFiles(directory="static"), name="static") # http://127.0.0.1:8000/static/images/python.jpg muestra el fichero

# GET -> Obtener / Leer Datos
@app.get("/") # Vamos a acceder a la raíz de un sitio
async def root(): # Siempre que accedemos a un servidor la operación debe ser asíncrona ya que no sabemo cuanto va a tardar en responder.
    return "¡Hola FastAPI!" # Si llamamos a 127.0.0.1:8000, nos va a devolver este mensaje

@app.get("/url") # http://127.0.0.1:8000/url
async def url():
    return { "url_curso":"https://mouredev.com/python" } # Devuelve un JSON

# Ejecutando la url http://127.0.0.1:8000/docs en el navegador, nos genera automáticamente la documentación usando Swagger
# Ejecutando la url http://127.0.0.1:8000/redoc en el navegador, nos genera automáticamente la documentación usando Redocly

# POST -> Crear Datos

# PUT -> Actualizar Datos. Todo el registro entero

# PATCH -> Actualizar un dato. Un campo de un registro

# DELETE -> Borrar Datos