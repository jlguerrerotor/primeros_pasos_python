### Manejo de Excepciones ###

numberOne, numberTwo = 5, 1
numberTwo = "1"

'''
if numberOne > 3:
    print(numberOne + numberTwo) # TypeError: unsupported operand type(s) for +: 'int' and 'str'
else:
    print("No se cumple la condición")
'''
# try except

try:
    print(numberOne + numberTwo)
    print("NO Se ha producido un error") # Si error, esta linea no se ejecuta
except:
    print("Se ha producido un error") # Se ejecuta si se produce un error

# try except else finally

numberTwo = 1
try:
    print(numberOne + numberTwo)
    print("NO Se ha producido un error") # Si error, esta linea no se ejecuta
except: # Obligatorio
    print("Se ha producido un error") # Se ejecuta si se produce un error
else: # Opcional
    print("La ejecución continúa correctamente") # Se ejecuta si NO se produce un error
finally: # Opcional
    print("La ejecución continúa") # Se ejecuta siempre

# Captura de exceptiones por tipo

numberTwo = "1"
try:
    print(numberOne + numberTwo) # TypeError: unsupported operand type(s) for +: 'int' and 'str'
    print("NO Se ha producido un error") # Si error, esta linea no se ejecuta
except TypeError: # Obligatorio. Se ejecuta solamente si se produce un TypeError
    print("Se ha producido un error") # Se ejecuta si se produce un error

try:
    print(numberOne + numberTwo) #TypeError: unsupported operand type(s) for +: 'int' and 'str'
    print("NO Se ha producido un error") # Si error, esta linea no se ejecuta
except ValueError: # Obligatorio. Se ejecuta solamente si se produce un ValueError
    print("Se ha producido un ValueError") # Se ejecuta si se produce un ValueError
except TypeError: # Obligatorio. Se ejecuta solamente si se produce un TypeError
    print("Se ha producido un TypeError") # Se ejecuta si se produce un Typerror

# Captura de la información de la exception

try:
    print(numberOne + numberTwo) #TypeError: unsupported operand type(s) for +: 'int' and 'str'
    print("NO Se ha producido un error") # Si error, esta linea no se ejecuta
except TypeError as error: # Obligatorio. Se ejecuta solamente si se produce un TypeError. Captura el error en la variable error.
    print("TypeError: " + str(error)) # Se ejecuta si se produce un TypeError
except Exception as exception: # Otra excepción cualquiera
    print("Exception: " + str(exception))
