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
