# Модифицируйте пример с координатными осями так, чтобы в точке их
# пересечения рисовался знак “+”, на верхнем конце вертикальной оси была
# стрелка вверх “^”, а на правом конце горизонтальной оси стрелка вправо “>”.
# Это сделает рисунок более красивым и точным.
for row in range(20):
    for col in range(50):
        if row == 9 and col == 24:
            print('+', end='')
        elif row == 9 and col == 49:
            print('>', end='')
        elif row == 9 and col < 49 and col != 24:
            print('-', end='')
        elif col == 24 and row == 0:
            print('^', end=' ')
        elif col == 24:
            print('|', end=' ')
        else:
            print(' ', end='')
    print()