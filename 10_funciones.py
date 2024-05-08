### Funciones ###

def my_function():
    print("Esto es una función")

my_function()
my_function()

def sum_two_values(first_value, second_value):
    print(first_value + second_value)

sum_two_values(5, 7)
sum_two_values(3245, 7578)
sum_two_values("5", "7")
sum_two_values(1.3, 4.7)

def sum_two_values_with_return(first_value, second_value):
    return first_value + second_value

my_result = sum_two_values_with_return(10, 5)
print(my_result)

def print_name(name, surname):
    print(f"{name} {surname}")

print_name("Joan Lluís", "Guerrero Torta")
print_name(surname="Guerrero Torta", name="Joan Lluís") # Reordeno los parámetros

def print_name_with_default(name, surname, alias="Sin alias"): # Valor por defecto del parámetro alias
    print(f"{name} {surname} {alias}")

print_name_with_default("Joan Lluís", "Guerrero Torta", "J.L.")
print_name_with_default("Joan Lluís", "Guerrero Torta") # Usa el alias ya que el tercer parámetro está vacío.

def print_texts(*texts): # * implica que le puedo pasar tantos parámetros como quiera.
    for text in texts:
        print(text)

print_texts("Hola", "Python", "J.L.")

def print_upper_texts(*texts): # * implica que le puedo pasar tantos parámetros como quiera.
    for text in texts:
        print(text.upper()) # Convierte a mayúscula todos los textos.

print_upper_texts("Hola", "Python", "J.L.")
