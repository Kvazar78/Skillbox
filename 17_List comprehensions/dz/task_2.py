# Генерация
#
# Пользователь вводит целое число N. Напишите программу, которая генерирует список из N чисел, на чётных местах в нём
# стоят единицы, а на нечётных — числа, равные остатку от деления своего номера на 5.
#
# Пример:
#
# Введите длину списка: 10
#
# Результат: [1, 1, 1, 3, 1, 0, 1, 2, 1, 4]
list_length = int(input('Введите длину списка: '))

list_num = [1 if i % 2 == 0 else i % 5 for i in range(list_length)]

print('Результат:', list_num)