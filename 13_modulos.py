### Módulos ###

# No deja importar nombres de ficheros que comienzan por un número
# my_function() # NameError: name 'my_function' is not defined. Es una función externa

# import my_module # Importa todo el módulo

# my_module.sum(5, 3, 6) # Debemos referencia al nombre del módulo
# my_module.printValue("Hola Python!")

# from my_module import sum # Importa una función del fichero
from my_module import sum, printValue # Importa VARIAS funciones del fichero

sum(5, 3, 1) # No hace falta referenciar al nombre del módulo ya que hemos importado la función
printValue("Hola Python!")

import math # Podemos importar módulos del sistema Python

print(math.pi)
print(math.pow(2, 8))

from math import pi as PI_VALUE # Le damos un alias (PI_VALUE) al valor pi importado de math

print(PI_VALUE)
