from pydantic import BaseModel # Para poder definir objetos.
from typing import Optional

# Entidad User. Objeto que implementa el comportamiento de BaseModel. Esto hace que podamos convertirlo directamente en un JSON
class User(BaseModel):
    id: Optional[str] = None # Optional[str] -> Puede que el id no nos los pasen cuando se crea el usuario
    username: str
    email: str
