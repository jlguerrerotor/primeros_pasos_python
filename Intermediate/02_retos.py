'''
Reto #0: EL FAMOSO "FIZZ BUZZ"
---------------------------------
Escribe un programa que muestre por consola (con un print) los
números de 1 a 100 (ambos incluidos y con un salto de línea entre
cada impresión), sustituyendo los siguientes:
- Múltiplos de 3 por la palabra "fizz".
- Múltiplos de 5 por la palabra "buzz".
- Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
'''

def fizz_buzz():
    for index in range(1,101):
        v = f"{index}: "
        if index % 3 == 0:
            v += "fizz"
        if index % 5 == 0:
            v += "buzz"
        v += "\n"
        print(v)

fizz_buzz()

'''
Reto #2: ¿ES UN ANAGRAMA?
------------------------------------
Escribe una función que reciba dos palabras (String) y retorne
verdadero o falso (Bool) según sean o no anagramas.
- Un Anagrama consiste en formar una palabra reordenando TODAS
  las letras de otra palabra inicial.
- NO hace falta comprobar que ambas palabras existan.
- Dos palabras exactamente iguales no son anagrama.
'''

def is_anagram(first_word, second_word):
    if first_word.lower() == second_word.lower():
        return False
    return sorted(first_word.lower()) == sorted(second_word.lower()) # Sorted devuelve una lista ordenando cada letra

print(is_anagram("Amor", "Roma"))

'''
Reto #3: LA SUCESIÓN DE FIBONACCI
--------------------------------------
Escribe un programa que imprima los 50 primeros números de la sucesión
de Fibonacci empezando en 0.
- La serie Fibonacci se compone por una sucesión de números en
  la que el siguiente siempre es la suma de los dos anteriores.
  0, 1, 1, 2, 3, 5, 8, 13...
'''

def fibonacci():
    prev = 0
    next = 1
    for index in range(0,50):
        print(prev)
        fib = prev + next
        prev = next
        next = fib
    
fibonacci()

'''
Reto #4: ¿ES UN NÚMERO PRIMO?
----------------------------------------
Escribe un programa que se encargue de comprobar si un número es o no primo.
Hecho esto, imprime los números primos entre 1 y 100.
'''

def is_prime(numero):
    if numero < 2:
        return False
    for index in range(2, numero):
        if numero % index == 0:
            return False
    return True

for number in range(101):
    result = is_prime(number)
    if result:
        print(f"Es primo {number}: {result}")

'''
Reto #7: INVIRTIENDO CADENAS
----------------------------------------
Crea un programa que invierta el orden de una cadena de texto
sin usar funciones propias del lenguaje que lo hagan de forma automática.
- Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
'''

def invertir(cadena):
    cadena_invertida = ""
    longitud = len(cadena)
    for index in range(longitud):
        cadena_invertida += cadena[longitud-index-1]
    return cadena_invertida

print(invertir("Hola mundo"))
