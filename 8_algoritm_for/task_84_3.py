# Пока все прятались, “голя” решил схитрить и считать секунды быстрее,
# чем нужно.
#
# Напишите программу, которая выводит только чётные числа в порядке
# убывания от N до 1 включительно, используя цикл for. Нельзя использовать
# условный оператор.
n = int(input('Введи количество секунд: '))
for i in range(n, 0 , -2):
    print(i)
print('Я иду искать!')