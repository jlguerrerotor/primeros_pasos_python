### Expresiones Regulares ###
# https://regex101.com para aprender y validar expresiones regulares

import re # Módulo que contiene las funcionalidades relacionadas con la expresiones regulares

my_string = "Esta es la lección número 7: Expresiones Regulares"
my_other_string = "Esta no es la lección número 6: Manejo de Ficheros"

# match

match = re.match("Esta es la lección",my_string, re.I)
print(match)
span = match.span() # Tupla formado por el valor donde comienza la cadena i donde acaba
print(span)
start, end = span
print(my_string[start:end])


match = re.match("Esta no es la lección",my_other_string)
#if not(match == None): # Tres formas de comparar el None
if match is not None:
#if match != None:
    print(match)
    start, end = match.span()
    print(my_other_string[start:end])
'''
print(re.match("Esta es la lección",my_string)) # <re.Match object; span=(0, 18), match='Esta es la lección'>
print(re.match("Esta es la lección",my_other_string)) # None
print(re.match("Expresiones Regulares",my_string)) # None ya que busca desde el principio
'''

# search

search = re.search("lección",my_string, re.I) # <re.Match object; span=(11, 18), match='lección'> ENcuentra la primera ocurrencia
print(search)
span = search.span() # Tupla formado por el valor donde comienza la cadena i donde acaba
print(span)
start, end = span
print(my_string[start:end])

# findall

my_string = "Esta es la lección número 7:\nLección llamada Expresiones Regulares"
findall = re.findall("lección",my_string, re.I) # ['lección', 'Lección'] Lista de las veces que encuentra la palabra
print(findall)

# split

split = re.split("\n",my_string, re.I) # ['Esta es la lección número 7:', 'Lección llamada Expresiones Regulares'] Divide por el caracter que se le pasa en forma de lista
print(split)

# sub

sub = re.sub("Expresiones","expresiones", my_string) # Lección llamada expresiones Regulares -> Sustituye una cadena por otra en el string.
print(sub)
sub2 = re.sub("[l|L]ección","LECCIÓN", sub)
print(sub2)

# Patrones

pattern = r"[Ll]ección"
print(re.findall(pattern, my_string)) # ['lección', 'Lección']

pattern = r"[Ll]ección|Expresiones"
print(re.findall(pattern, my_string)) # ['lección', 'Lección', 'Expresiones']

pattern = r"[0-9]"
print(re.findall(pattern, my_string)) # ['7']
print(re.search(pattern, my_string)) # <re.Match object; span=(26, 27), match='7'>

pattern = r"[\d]"
print(re.findall(pattern, my_string)) # ['7']

pattern = r"[\D]"
print(re.findall(pattern, my_string)) # [Todas las letras menos las del pattern '7']

pattern = r"[l]."
print(re.findall(pattern, my_string)) # ['la', 'le', 'll', 'la']

pattern = r"[l].*"
print(re.findall(pattern, my_string)) # ['la lección número 7:', 'llamada Expresiones Regulares']

# Validación de email con RegEx
def is_valid_email(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z-.]+$"
    return re.match(pattern,email)

print(is_valid_email(my_string)) # None
print(is_valid_email("jlguerrerotor@gmail.com")) # <re.Match object; span=(0, 23), match='jlguerrerotor@gmail.com'>
print(is_valid_email("jlguerrerotor@gmail")) # None
print(is_valid_email("jlguerrerotor@gmail.com.es")) # <re.Match object; span=(0, 26), match='jlguerrerotor@gmail.com.es'>