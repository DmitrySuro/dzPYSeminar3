# Напишите программу, которая будет преобразовывать 
# десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10


res_dec = int(input('Insert your number: '))
print(f'{res_dec} => {bin(res_dec)[2:]}')