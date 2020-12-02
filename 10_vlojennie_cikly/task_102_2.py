# Преподаватель показал студентам несколько результатов программы и
# сказал “Кто догадается что делает программа и как она это делает -
# получит зачёт автоматом”. И студент Миша намерен получить этот зачёт.
# Он заметил, что в результатах программы есть определённая закономерность.
# Вот некоторые результаты:
#
# Напишите программу, которая запрашивает у пользователя размер матрицы и
# выводит соответствующие результаты. Подсказка: столбцы
size = int(input('Введите размер матрицы: '))
for row in range(1, size + 1):
    for col in range(1, size +1):
        if  row % 3 == 0:
            print(row, end = ' ')
        elif col % 3 == 0:
            print(col, end = ' ')
        else:
            print(row, end = ' ')
    print()