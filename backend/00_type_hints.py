### FastAPI ###
# Recomienda especificar el tipo de dato aunque en principio no es necesario.
# La interfaz de VS Code, en funcion del tipo especificado va a sugerirnos las funciones y atributos disponibles.
# FastAPI requerirá que el tipo que li llegue del frontend sea el que se ha especificado en el diseño del backend.

### Type Hints ###

my_string_variable = "Esto es un string"
print(my_string_variable)
print(type(my_string_variable))

my_string_variable = 5 # Tipado dinámico. Cambio el tipo en tiempo de ejecución. str -> int
print(my_string_variable)
print(type(my_string_variable))

my_typed_variable: str = "My typed String variable"
print(my_typed_variable)
print(type(my_typed_variable))

my_typed_variable: int = 5
print(my_typed_variable)
print(type(my_typed_variable))

