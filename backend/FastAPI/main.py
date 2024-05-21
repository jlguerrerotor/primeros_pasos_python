# Arrancar servidor UVICORN: uvicorn main:app --reload
# main es el fichero raíz que queremos arrancar
# :app es nuestra instancia de FastAPI
# --reload -> Hará que cambie el contexto del servidor cada vez que cambiemos el fichero main
# Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)


from fastapi import FastAPI

app = FastAPI()

@app.get("/") # Vamos a acceder a la raíz de un sitio
async def root(): # Siempre que accedemos a un servidor la operación debe ser asíncrona ya que no sabemo cuanto va a tardar en responder.
    return "¡Hola FastAPI!" # Si llamamos a 127.0.0.1:8000, nos va a devolver este mensaje

@app.get("/url") # http://127.0.0.1:8000/url
async def url():
    return { "url_curso":"https://mouredev.com/python" } # Devuelve un JSON

# Ejecutando la url http://127.0.0.1:8000/docs en el navegador, nos genera automáticamente la documentación usando Swagger
# Ejecutando la url http://127.0.0.1:8000/redoc en el navegador, nos genera automáticamente la documentación usando Redoc

