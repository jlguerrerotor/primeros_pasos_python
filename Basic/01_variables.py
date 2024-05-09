'''
Comentario en varias
LÍNEAS
'''

"""
Otro
Comentario en varias
LÍNEAS
"""

my_string_variable = "Esto es un string"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)
print(type(my_int_variable))

my_int_to_string_variable = str(my_int_variable)
print(my_int_to_string_variable)
print(type(my_int_to_string_variable))

my_bool_variable = False
print(my_bool_variable)
print(type(my_bool_variable))

print(my_string_variable, my_int_variable, my_int_to_string_variable, my_bool_variable) # Concatena variables aunque sean de tipos distintos

# Algunas Funciones del Sistema
print('La longitud de la cadena es:', len(my_string_variable), 'caracteres')   # Longitud de una cadena

# Variables en una sola linea. NO ABUSAR
name, surname, age = "Joan Lluís", "Guerrero Torta", 50
print("Me llamo", name, surname, "y tengo",age,"años")

# Input. SOlicitar información al usuario
name = input("What's your name?")
age = input("How old are you?")
print("Soy", name, "de", age, "años")

# Aunque indiquemos el tipo de datos, puedo cambiarlo simplemente asignando a la variable otro valor de un tipo distinto.
address: str = "Mi dirección"
