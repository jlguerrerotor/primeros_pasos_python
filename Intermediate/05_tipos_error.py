### Tipos de Error ###

# SyntaxError
# print "¡Hola comunidad!" # SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
print("¡Hola comunidad!") 

# NameError
# print(var_saludo) # NameError: name 'var_saludo' is not defined
var_saludo = "Hola"
print(var_saludo)

# IndexError
my_list = ["Python", "Swift", "Kotlin", "Dart", "JavaScript"]
# print(my_list[5]) # IndexError: list index out of range
print(my_list[4])

# ModuleNotFoundError
# import mat # ModuleNotFoundError: No module named 'mat'
import math

# AttributeError
# print(math.PI) # AttributeError: module 'math' has no attribute 'PI'. Did you mean: 'pi'?
print(math.pi)

# KeyError (Diccionarios)
my_other_dict = {"Nombre":"Joan Lluís", "Aplellido":"Guerrero Torta", "Edad":50, 1:"Python"}
# print(my_other_dict["Edadd"]) # KeyError: 'Edadd'
print(my_other_dict["Edad"])

# TypeError
# print(my_list["Nombre"]) # TypeError: list indices must be integers or slices, not str
print(my_list[1])

# ImportError
# from math import PI # ImportError: cannot import name 'PI' from 'math' (unknown location). Did you mean: 'pi'?
from math import pi
print(pi)

# ValueError
# my_int = int("10 Años") # ValueError: invalid literal for int() with base 10: '10 Años'
my_int = int("10")
print(my_int)

# ZeroDivisionError
# print(5/0) # ZeroDivisionError: division by zero
print(5/2)

# FileNotFoundError
# open("my_file.txt") # FileNotFoundError: [Errno 2] No such file or directory: 'my_file.txt'