# Напишите программу, которая рисует с помощью символьной графики
# прямоугольную рамку. Для вертикальных линий используйте символ
# вертикального штриха “|”, а для горизонтальных - дефис “-”. Пусть
# пользователь вводит ширину и высоту рамки.
high_row = int(input('Введи высоту рамки: '))
width_col = int(input('Введи ширину рамки: '))

for row in range(high_row +1):
    for col in range(width_col + 1):
        if col == 0 or col == width_col:
            print('|', end='')
        elif row == 0 or row == high_row:
            print('-', end='')
        else:
            print(' ', end='')
    print()
