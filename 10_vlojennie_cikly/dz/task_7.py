# После успешного первого задания Степан уже было обрадовался, что ему
# наконец можно будет работать программистом в хорошей компании. Но всё
# оказалось не так просто: ему дали ещё одно задание на вывод матрицы. Вот
# бы и правда на работу принимали после одного вопроса...
#
# Напишите программу, которая запрашивает у пользователя размер квадратной
# матрицы и выводит её на экран по следующему принципу: по двум диагоналям
# идут единицы, сверху от пересечения - нули, со всех остальных сторон - \
# двойки
size = int(input('Введите размер матрицы: '))

for row in range(size):
    for col in range(size):
        if row == col or col == size - 1 - row:
            print('1', end=' ')
        elif row > 0:
            print('2', end=' ')
        else:
            print('0', end=' ')
    print()
