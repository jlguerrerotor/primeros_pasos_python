### Diccionarios ###
# Parecido a un hashmap (Permite almacenar datos de tipo Clave:Valor). Parecido a un JSON

my_dict = dict()
my_other_dict = {}
print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre":"Joan Lluís", "Aplellido":"Guerrero Torta", "Edad":35, 1:"Python"}
print(my_other_dict)

my_dict = {
    "Nombre":"Joan Lluís", 
    "Apellido":"Guerrero Torta", 
    "Edad":35, 
    "Lenguajes": {"Python", "Swift", "Kotlin"}, # Dentro del diccionario tenemos un SET
    1:1.73
}
print(my_dict)

print(len(my_other_dict)) # 4 elementos clave:valor
print(len(my_dict)) # 5 elementos clave:valor

print(my_dict["Nombre"]) # Devuelve el nombre guardado en el diccionario
my_dict["Nombre"] = "Joan Ll." # Reemplaza el nombre por otro
print(my_dict)

my_dict["Calle"] = "Calle Mia" # Añade una nueva clave:valor al diccionario
print(my_dict)

del my_dict["Calle"] # Elimina el elemento indicado del diccionario -del my_dict- eliminaria el diccionario entero
print(my_dict)

print("Joan Ll." in my_dict) # False Busca por llave, no por valor
print("Apellido" in my_dict) # True Busca por llave, no por valor

print(my_dict.items()) # dict_items([('Nombre', 'Joan Ll.'), ('Apellido', 'Guerrero Torta'), ('Edad', 35), ('Lenguajes', {'Kotlin', 'Swift', 'Python'}), (1, 1.73)])
print(my_dict.keys()) # dict_keys(['Nombre', 'Apellido', 'Edad', 'Lenguajes', 1]). En formato Lista
print(my_dict.values()) # dict_values(['Joan Ll.', 'Guerrero Torta', 35, {'Kotlin', 'Swift', 'Python'}, 1.73]). En formato Lista

my_list = ["Nombre", 1, "Piso"]
my_new_dict = dict.fromkeys(my_list)
print(my_new_dict)

my_new_dict = dict.fromkeys(("Nombre", 1, "Piso")) # Crea un diccionario vacío
print(my_new_dict)

my_new_dict = dict.fromkeys(my_dict) # Crea un diccionario vacío a partir de otro
print(my_new_dict)

my_new_dict = dict.fromkeys(my_dict, "Joan Lluís") # Crea un diccionario inicializado con el objeto que queramos
print(my_new_dict)

print(list(my_new_dict)) # Si transformo el diccionario en una lista, lo que recibo son las claves
print(tuple(my_new_dict)) # Si transformo el diccionario en una tupla, lo que recibo son las claves
print(set(my_new_dict)) # Si transformo el diccionario en un conjunto, lo que recibo son las claves

print(list(my_new_dict.values())) # Si transformo el diccionario.values() en una lista, lo que recibo son los valores
