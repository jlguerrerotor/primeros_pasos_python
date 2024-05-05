### Strings ###

my_string = "Mi String"
my_other_string = 'Mi otro String'

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)

my_new_line_string = "Este es un string \ncon salto de linea"
print(my_new_line_string)

my_tab_string = "\tEste es un string \tcon tabulación"
print(my_tab_string)

my_scape_string = "\\tEste es un string \\nescapado"
print(my_scape_string)

# Formateo

name, surname, edad = "Joan Lluís", "Guerrero", 50

print("Mi nombre es {} {} y mi edad es {}".format(name, surname, edad))
print("Mi nombre es %s %s y mi edad es %d" %(name, surname, edad))
print(f"Mi nombre es {name} {surname} y mi edad es {edad}".format(name, surname, edad))

# Desempaquetado de caracteres
language = "Python"
a, b, c, d, e, f = language
print(a)
print(e)

# División
laguage_slice = language[1:3] # de 1 a 2. Comienza por 0, 1 y menor que 3
print(laguage_slice)
laguage_slice = language[1:] # de 1 a 2. Comienza por 0, 1 y el resto
print(laguage_slice)
laguage_slice = language[-2] # segundo caracter desde el final
print(laguage_slice)

laguage_slice = language[0:6:2] # Pilla los caracteres del 0 al 6 dando saltos de 2 en 2
print(laguage_slice)

# Reverse
reversed_language = language[::-1]
print(reversed_language)

#Funciones
print(language.capitalize()) # POne la primera letra en mayúscula
print(language.upper()) # Pone todo en mayúscula
print(language.count("t")) # Cuenta cuantas veces aparece la cadena en el string
print(language.isnumeric()) # Indica si la cadena es un numérico
print(language.lower()) # Pone todo en minúsculas
print(language.upper().isupper()) # Indica se la cadena es mayúscula o no
print(language.startswith("Py")) # Indica si la variable empieza por la cadena
