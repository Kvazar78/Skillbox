# Сжатие списка
#
# Дан список из N целых чисел. Напишите программу, которая выполняет «сжатие списка» — переставляет все нулевые
# элементы в конец массива. При этом все ненулевые элементы располагаются в начале массива в том же порядке.
# Затем все нули из списка удаляются.
import random

quantity_num = int(input('Сколько будет чисел? '))

list_nums = [random.randint(0, 1) for _ in range(quantity_num)]
print('Исходный список:', list_nums)
count_0 = list_nums.count(0)
if count_0 == len(list_nums):
    print('Список неудачно сгенерировался - одни нули :(')
else:
    list_nums = [i for i in list_nums if i != 0]
    for _ in range(count_0):
        list_nums.append(0)

    print('Отсортированный список', list_nums)

    list_nums = [i for i in list_nums if i != 0]
    print('Сжатый список', list_nums)
