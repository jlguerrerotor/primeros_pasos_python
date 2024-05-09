### Tuplas ###
# Una tupla es un conjunto de valores que no se pueden cambiar una vez establecidos.

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (50, 1.73, "Joan Lluís", "Guerrero Torta", "A")
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
# print(my_tuple[4]) # IndexError

print(my_tuple.count("Joan Lluís")) # Cuenta las veces que aparece el parámetro en la tupla.

print(my_tuple.index("Joan Lluís")) # Devuelve el índice de la primera vez que aparece el parámetro en la tupla.

# my_tuple[1] = 1.80 # Error 'tuple' object does not support item assignment.
# del my_tuple[1] # TypeError: 'tuple' object doesn't support item deletion

my_other_tuple = (25, 34, 43)

my_sum_tuple = my_tuple + my_other_tuple # Podemos agregar una tupla a otra
print(my_sum_tuple)

print(my_sum_tuple[3:6]) # Obtenemos la subtupla entre el índice 3 i el 6 (sin tenerlo en cuenta)

my_tuple = list(my_tuple) # Transforma una tupla en una lista para poder modificarla
print(type(my_tuple))

my_tuple[4] = "Mi Empresa" # Como tenemos una lista, ahora podemos modificarla
my_tuple.insert(1, "Azul")
print(my_tuple)

my_tuple = tuple(my_tuple) # Volvemos a convertir la lista en una tupla.
print(type(my_tuple))
print(my_tuple)

del my_tuple # Elimina la variable, no la vacía. La elimina definitivamente.