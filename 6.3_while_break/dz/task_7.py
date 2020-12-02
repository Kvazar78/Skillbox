# Напишите программу, которая получает на вход: число a — первый член
# прогрессии, d — разность арифметической прогрессии и число n — количество
# членов в прогрессии. Программа выводит каждый член прогрессии и их сумму в конце.
#
# Пример:
# Введите первый член прогрессии: 5
# Введите разность: 3
# Введите количество членов прогрессии: 4
# 5
# 8
# 11
# 14
# Сумма арифметической прогрессии: 38
a = int(input('Введи первый член прогрессии: '))
d = int(input('Введи разность арифметической прогрессии: '))
n = int(input('Введи количество членов в прогрессии: '))
summ = 0
while n != 0:
    print(a)
    summ += a
    a += d
    n -= 1
print(f'Сумма арифметической прогрессии: {summ}')