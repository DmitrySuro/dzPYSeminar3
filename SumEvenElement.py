# Задайте список из нескольких чисел. Напишите
# программу, которая найдёт сумму элементов списка, стоящих
#  на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from re import I


my_list = [2, 3, 5, 9, 3]
sum_even_elements = 0
index = 1
while index < len(my_list):
    sum_even_elements += my_list[index]
    index += 2
print(sum_even_elements)
