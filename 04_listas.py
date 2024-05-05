### Listas ###

# Creación
my_list = list()
mu_other_list = []

print(len(my_list))

# Inicialización / Relleno
my_list = [35, 50, 24, 62, 53, 30, 17]

print(my_list)
print(len(my_list)) # Cuenta el número de elementos de la lista

my_other_list = [50, 1.73, "Joan Lluís", "Guerrero Torta"]
print(my_other_list)
print(type(mu_other_list))

# Acceso a la lista
print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1]) # Accede al último elemento de la lista
print(my_other_list[-3])
print(my_other_list.count("Guerrero Torta")) # Count cuenta el número de ocurrencias de la cadena pasada en la lista
# print(my_other_list[4])  # IndexError
# print(my_other_list[-5]) # IndexError

age, height, name, surname = my_other_list # Desempaqueta TODOS elementos en variables.
print(name)

print(my_list + my_other_list) # Concatenación de listas

# Añadir elementos
my_other_list.append("Mi Empresa") # Inserta al final de la lista
print(my_other_list)

my_other_list.insert(4,"Rojo") # Inserta un string en una posición de la lista
print(my_other_list)

my_other_list.remove("Rojo") # Elimina del la lista el primer elemento que coincie con el parámetro
print(my_other_list)

my_other_list.insert(4, "Rojo")

print(my_list.pop()) # Quita el último elemento de la lista y devuelve el valor que quita 
print(my_list)

my_pop_element = my_list.pop(2) # Quita el elemento de la lista indicado por el índice y devuelve el valor que quita 
print(my_pop_element)
print(my_list)

del my_list[2] # Elimina un elemento de la lista 
print(my_list)

my_list.clear() # Vacía toda la lista
print(my_list)

my_other_list.remove("Rojo")
my_other_list.insert(4, "Azul") # Reemplazamos el Rojo por el Azul
print(my_other_list)

my_other_list[4] = "Rojo" # Reemplazamos el Azul por el Rojo de nuevo
print(my_other_list)

my_new_list = my_other_list.copy() # Hace una copia idéntica de la lista en otra posición de memoria
my_other_list.clear() # Borra la lista original
print(my_other_list) # Vacía
print(my_new_list) # Copia

my_new_list.reverse() # Cambia a orden inverso los valores de la lista
print(my_new_list)

my_list = [35, 50, 24, 62, 53, 30, 17]
my_list.sort() # Ordena lis valores de la lista (No sirve para float ni str)
print(my_list)

