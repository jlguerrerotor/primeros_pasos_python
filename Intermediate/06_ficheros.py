### Manejo de Ficheros ###

import os 

# Ficheros .txt

txt_file = open("Intermediate/my_file.txt", "w+") # La ruta relativa ha de ser desde el fichero raíz del proyecto. r+ significa rw
# print(txt_file.read()) # Lee todo el fichero
txt_file.write("Mi nombre es Joan Lluís\nMi apellido es Guerrero\n50 años\nMi lenguaje preferido es Python")
print(txt_file.read(10)) # Lee los 10 primeros caracteres del fichero
print(txt_file.readline()) # Lee una línea entera del fichero
# print(txt_file.readlines()) # Lee el fichero colocando cada línea en un celda de un array
for line in txt_file.readlines():
     print(line)
txt_file.write("\nAunque también me gusta Kotlin") # Escribe una nueva línea en el fichero
print(txt_file.readline())

txt_file.close()

with open("Intermediate/my_file.txt", "a") as my_other_file:
     my_other_file.write("\nY Swift")

os.remove("Intermediate/my_file.txt") # Elimina el fichero

# Ficheros .json

import json

# Diccionario a json
json_file = open("Intermediate/my_file.json", "w+") # La ruta relativa ha de ser desde el fichero raíz del proyecto. w+ significa rw
json_test = {
     "Nombre":"Joan Lluís", 
     "Aplellido":"Guerrero Torta", 
     "Edad":50, 
     "Lenguajes":["Python","Swift","Kodlin"],
     "Website":"https://www.guepehome.com"
}
json.dump(json_test, json_file, indent=4) # Grabamos el json

json_file.close() # Cerramos el fichero json

with open("Intermediate/my_file.json", "r+") as my_other_file: # Abrimos el json en modo lectura
     for line in my_other_file.readlines():
          print(line)

# json a diccionario
json_file = open("Intermediate/my_file.json")
json_dict = json.load(json_file) # Carga el fichero json en un diccionario
print(json_dict)
print(type(json_dict))
print(json_dict["Nombre"])
json_file.close()

# Ficheros .csv

import csv

csv_file = open("Intermediate/my_file.csv", "w", newline="", encoding="utf-8")
csv_writer = csv.writer(csv_file,delimiter=";")   

csv_writer.writerow(["Nombre","Aplellido","Edad","Lenguaje","Website"])
csv_writer.writerow(["Joan Lluís","Guerrero Torta",50,"Python","https://www.guepehome.com"])
csv_file.close()

# Ficheros .xlsx

import pyexcel # debe instalarse el módulo

# Ficheros .xml

import xml
