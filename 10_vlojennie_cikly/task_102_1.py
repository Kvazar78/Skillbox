# Напишите программу, которая выводит квадратную матрицу размера N на N.
# В каждой нечетной строке матрицы идут числа от 1 до N, а в каждой чётной
# - просто числа равные номеру этой строки.
size = int(input('Введите размер матрицы: '))
for row in range(1, size + 1):
    for col in range(1, size + 1):
        if row % 2 == 0:
            print(row, end = ' ')
        else:
            print(col, end = ' ')
    print()