# Напишите программу, которая выводит на экран крест из символов
# “^”.
#
# (Символы выводятся по диагоналям воображаемого квадрата.)
size = int(input('Введи размер стороны квадрата: '))

for row in range(size):
    for col in range(size):
        if col == row or col == size - (row + 1):
            print('^', end='')
        else:
            print(' ', end='')
    print()