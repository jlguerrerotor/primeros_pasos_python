### Conjuntos o Sets ###
# Un set tiene de base una listas #

my_set = set()
my_other_set = {} # Inicialmente se define como un diccionario si lo creamos de esta manera.

print(type(my_set))
print(type(my_other_set))

my_other_set = {"Joan Lluís", "Guerrero Torta", 50} # Ahora le decimos que se convierta en un set.
print(type(my_other_set))

print(len(my_other_set)) # Tamaño del conjunto.

# print(my_other_set[0]) # TypeError: 'set' object is not subscriptable

my_other_set.add("Mi Empresa") # Añadir un elemento no implica que se añada al final. Un set no es una estructura ordenada.
print(my_other_set)

my_other_set.add("Mi Empresa") # Si volvemos a añadir el mismo valor, no lo añade ya que ya existía. NO ADMITE REPETIDOS.
print(my_other_set)

print("Joan Lluís" in my_other_set) # Comprobar si un elemento existe en el conjunto.
print("Joan Ll." in my_other_set)

my_other_set.remove("Joan Lluís") # Podemos eliminar un elemento del conjunto
print(my_other_set)

my_other_set.clear() # Limpia el contenido del conjunto
print(my_other_set)
print(len(my_other_set))

del my_other_set # se carga la variable y todo su contenido
# print(my_other_set) # NameError: name 'my_other_set' is not defined

my_set = {"Joan Lluís", "Guerrero Torta", 50}
my_list = list(my_set) # Convertimos un set en una lista. Pero no sabemos en que orden se nos va a crear.
print(my_list)

my_other_set = {"Kotlin", "Swift", "Python"}

my_new_set = my_set.union(my_other_set) # Une 2 conjuntos
print(my_new_set)

print(my_new_set.difference(my_set)) # Calcula la diferencia entre 2 conjuntos

print(my_new_set.intersection(my_set)) # Calcula los elementos en común entre los 2 conjuntos

print(my_set.issubset(my_new_set)) # Calcula si un conjunto es un subconjunto de otro. 