from fastapi import FastAPI

app = FastAPI()

@app.get("/") # Vamos a acceder a la raíz de un sitio
async def root(): # Siempre que accedemos a un servidor la operación debe ser asíncrona.
    return "¡Hola FastAPI!"