### Lambdas ###
# Vamos a entenderlas como funciones anónimas (no tienen nombre)

sum_two_values = lambda first_value, second_value: first_value + second_value
print(sum_two_values(2, 4)) # Si se asignan a una variable, esta actúa como función

multiply_values = lambda first_value, second_value: first_value * second_value - 3
print(multiply_values(2, 4))

# Lambda dentro de una función

def sum_three_values(value):
    return lambda first_value, second_value: first_value + second_value + value

print(sum_three_values(5)(2, 4))

