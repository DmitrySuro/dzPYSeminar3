# Напишите программу, которая найдёт произведение
# пар чисел списка. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

my_list = [2, 3, 4, 5, 6]
product_pair_numbers = 0
for i in range(0, len(my_list)-1):
    product_pair_numbers = my_list[i]*my_list[len -1]
