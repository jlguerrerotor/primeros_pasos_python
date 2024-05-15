### Manejo de Ficheros ###

import os 

# Ficheros .txt

txt_file = open("Intermediate/my_file.txt", "r+") # La ruta relativa ha de ser desde el fichero raíz del proyecto. r+ significa rw
# print(txt_file.read()) # Lee todo el fichero
txt_file.write("Mi nombre es Joan Lluís\nMi apellido es Guerrero\n50 años\nMi lenguaje preferido es Python")
print(txt_file.read(10)) # Lee los 10 primeros caracteres del fichero
print(txt_file.readline()) # Lee una línea entera del fichero
# print(txt_file.readlines()) # Lee el fichero colocando cada línea en un celda de un array
for line in txt_file.readlines():
     print(line)
txt_file.write("\nAunque también me gusta Kotlin") # Escribe una nueva línea en el fichero
print(txt_file.readline())

os.remove("Intermediate/my_file.txt")