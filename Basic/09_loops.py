### Loops ###

# While (Iterar en función de una condición)

my_condition = 0
while my_condition < 10:
    print(my_condition)
    my_condition += 2
else:
    print("Mi condición es >= 10")
print("La ejecución continúa")

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Mi condición es 15")
        break # Se detiene la ejecución saliendo del while

    print(my_condition)
print("La ejecución continúa") # Al salir del bucle se ejecuta

# For (Iterar un listado de elementos)

my_list = [35, 50, 24, 62, 53, 30, 17]

for element in my_list:
    print(element)

my_tuple = (50, 1.73, "Joan Lluís", "Guerrero Torta", "A")
my_set = {"Joan Lluís", "Guerrero Torta", 50}
my_dict = {
    "Nombre":"Joan Lluís", 
    "Apellido":"Guerrero Torta", 
    "Edad":35, 
    "Lenguajes": {"Python", "Swift", "Kotlin"}, # Dentro del diccionario tenemos un SET
    1:1.73
}

for element in my_tuple:
    print(element)

for element in my_set:
    if element == "Guerrero Torta":
        continue # Continuamos con el for
    print(element)

for element in my_dict:
    if element == "Edad":
        break 
    print(element)

for element in my_dict.values():
    print(element)
else:
    print("El for para el Diccionario ha finalizado")
