### Fechas ###

from datetime import datetime as dt

now = dt.now() # Inicializa un objeto a la hora actual

print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)

timestamp = now.timestamp() # Ojeto que contiene toda la información del momento desde 1970

print(timestamp) # 1715270794.412381

# Carga de una fecha
year_2024 = dt(2024, 1, 1)

def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp())

print_date(now)
print_date(year_2024)

from datetime import time as t

current_time = t(21,6,0) # Inicializmos el tiempo

print(current_time.hour)
print(current_time.minute)
print(current_time.second)

from datetime import date as d

current_date = d.today() # Inicializmos la fecha actual
new_date = d(2024,1,1) # Inicializmos una fecha

print(current_date.year)
print(current_date.month)
print(current_date.day)

print(new_date.year)
print(new_date.month)
print(new_date.day)

# Operaciones con fechas

diff = year_2024 - now 
print(diff) # -130 days, 5:22:36.538635
diff = year_2024.date() - current_date 
print(diff) # -130 days, 5:22:36.538635
print(year_2024.time())

from datetime import timedelta as td # Sirve para trabajar con franjas de fechas

start_timedelta = td(200, 100, 100, weeks=10)
end_timedelta = td(300, 100, 100, weeks=13)
print(end_timedelta - start_timedelta)
print(end_timedelta + start_timedelta)