### Manejo de Paquetes en Python ###

# PIP https://pypi,org

# Terminal
# pip --version -> Ver la versión de pip
# pip install pip -> Instalar pip
# pip install numpy -> Instala el módulo numpy
# pip list -> Lista las librerías instaladas en python
# pip uninstall pandas -> Desisnstala la librería pandas de python
# pip show numpy -> Da informacion sobre un paquete

import numpy

import mypackage.arithmetics

print(numpy.version.version)

numpy_array = numpy.array([35, 50, 24, 62, 53, 30, 17])
print(type(numpy_array)) # <class 'numpy.ndarray'> Es un array extendido con operaciones de numpy
print(numpy_array * 2) # [ 70 100  48 124 106  60  34]

# pip install pandas 
import pandas

# pip install requests
import requests
response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=151") # Llamada a una API con un Get sin autenticación
print(response) # <Response [200]>
print(response.status_code) # 200
print(response.json()) # Es el json que contiene todos los datos solicitados en la llamada a la API

# Arithmetics Package

from mypackage import arithmetics

print(arithmetics.sum_two_values(1, 4))
