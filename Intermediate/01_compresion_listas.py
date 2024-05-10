### Compresión de Listas ###

my_original_list = [0, 1, 2, 3, 4, 5, 6, 7]
print(my_original_list)

my_range = range(8)
print(list(my_range))

my_list = [i for i in range(8)]
print(my_list) # [0, 1, 2, 3, 4, 5, 6, 7]

my_list = [i+1 for i in my_original_list]
print(my_list) # [1, 2, 3, 4, 5, 6, 7, 8]

my_list = [i*2 for i in my_original_list]
print(my_list) # [0, 2, 4, 6, 8, 10, 12, 14]

my_list = [i*i for i in my_original_list]
print(my_list) # [0, 1, 4, 9, 16, 25, 36, 49]

def sum_five(number):
    return number + 5

my_list = [sum_five(i) for i in my_original_list]
print(my_list) # [5, 6, 7, 8, 9, 10, 11, 12]
