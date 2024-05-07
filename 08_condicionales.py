### Condicionales ###

my_condition = False

if my_condition: # igual que if my_condition == True:
    print("Se ejecuta la condición del if") # No se ejecuta

print("La ejecución continúa") # Se ejecuta siempre

my_condition = 5 * 2
if my_condition == 11:
    print("Se ejecuta la condición del segundo if") # NO Se ejecuta. Condición False

if my_condition >= 10:
    print("Es mayor o igual que 10") # Se ejecuta. Condición True
else: # Si no se cumple la condición
    print("Es menor que 10") # No Se ejecuta. Condición False

if my_condition >= 10 and my_condition <=20:
    print("Es mayor o igual que 10 y menor o igual que 20") # Se ejecuta. Condición True
else: # Si no se cumple la condición
    print("Es menor que 10 o mayor que 20") # No Se ejecuta. Condición False

if my_condition >= 10 and my_condition <=20:
    print("Es mayor o igual que 10 y menor o igual que 20") # Se ejecuta. Condición True
elif my_condition > 50:
    print("Es mayor 50") # No Se ejecuta. Condición False
else: # Si no se cumple la condición
    print("Es menor que 10 o mayor que 20 y menor o igual que 50") # No Se ejecuta. Condición False

my_string = "" # Vacío

if my_string: # No entra
    print("Mi cadena de texto es vacía")

my_string = "H"

if my_string: # Entra
    print("Mi cadena de texto NO es vacía")

my_string = "" # Vacío

if not my_string: # Entra
    print("Mi cadena de texto es vacía")
