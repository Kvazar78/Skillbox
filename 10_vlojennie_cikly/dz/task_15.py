# В одной компьютерной текстовой игре рисуются всяческие элементы
# ландшафта.
#
# Напишите программу, которая получает на вход число N и выводит на
# экран числа в виде “ямы” вот так:
depth = int(input('Введи глубину ямы: '))

for row in range(1, depth + 1):
    for col in range(1, depth * 2 + 1):
        if col < row +1:
            print(depth +1 - col, end='')
        elif col > (depth * 2) + (-row):
            print(-depth + col, end='')
        else:
            print('.', end='')
    print()
