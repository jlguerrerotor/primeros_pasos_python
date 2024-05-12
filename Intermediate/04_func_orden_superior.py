### Funciones de Orden Superior ###
# Funciones que hacen cosas con funciones dentro. Parecido a funciones anidadas

def sum_one(value):
    return value + 1

def sum_five(value):
    return value + 5

def sum_two_values_and_one(first_value, second_value, f_sum): # Estamos pasando un parámetro que en realidad es una función
    return f_sum(first_value + second_value) # COmo resultado devuelve la suma de los dos valores y la aplica la función f_sum

print(sum_two_values_and_one(5, 2, sum_one))
print(sum_two_values_and_one(5, 2, sum_five))
