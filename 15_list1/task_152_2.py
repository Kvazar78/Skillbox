#  Кратность
#
# Пользователь вводит список из N чисел и число K. Напишите код, выводящий на экран сумму индексов элементов списка,
#  которые кратны K.
#
# Пример:
#
# Кол-во чисел в списке: 4
#
# Введите 1 число: 1
# Введите 2 число: 20
# Введите 3 число: 30
# Введите 4 число: 4
#
# Введите делитель: 10
#
# Индекс числа 20: 1
# Индекс числа 30: 2
#
# Сумма индексов: 3
nums_list = []
N = int(input('Кол-во чисел в списке: '))

for i in range(N):
    num = int(input(f'Введите {i + 1} число: '))
    nums_list.append(num)

deliver = int(input('Введите делитель: '))
summ = 0

for i in nums_list:
    if i % 10 == 0:
        number_index = nums_list.index(i)
        print(f'Индекс числа {i}: {number_index}')
        summ += number_index

print(f'Сумма индексов: {summ}')