### Funciones de Orden Superior ###
# Funciones que hacen cosas con funciones dentro. Parecido a funciones anidadas

from functools import reduce


def sum_one(value):
    return value + 1

def sum_five(value):
    return value + 5

def sum_two_values_and_one(first_value, second_value, f_sum): # Estamos pasando un parámetro que en realidad es una función (f_sum)
    return f_sum(first_value + second_value) # Como resultado devuelve la suma de los dos valores y la aplica la función f_sum

print(sum_two_values_and_one(5, 2, sum_one))
print(sum_two_values_and_one(5, 2, sum_five))

### Closures ###

def sum_ten(original_value):
    def add(value): # Función devuielta
        return value + original_value + 10
    return add # Devuelve una función

# Forma de llamar a sum_ten
add_closure = sum_ten(1)
print(add_closure(5))

# Otra forma de llamar a sum_ten como una lambda
print(sum_ten(5)(1)) # A sum_ten le pasa un 5 i al resultado (una función) le pasamos 1.

### Build-in Funciones de Orden Superior ###

numbers = [2, 5, 10, 21, 3, 30]

# Map - Itera cada un o de los valores del elemento iterable (lista) y le aplica a cada uno la función pasada (multiply_two)

def multiply_two(number):
    return number * 2

print(list(map(multiply_two, numbers)))
print(list(map(lambda number: number*2, numbers)))

# Filter

def filter_greater_than_ten(numero):
    return numero > 10

print(list(filter(filter_greater_than_ten, numbers)))
print(list(filter(lambda number: number > 10, numbers)))

# Reduce - Itera la lista (iterable) acumulando el resultado de la función (suma) al siguiente valor
# 2+5=7+10=17+21=38+3=41+30=71

def sum_two_values(first_value, second_value):
    return first_value + second_value

print(reduce(sum_two_values, numbers))