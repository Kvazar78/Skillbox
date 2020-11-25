# Напишите программу, которая рисует координатные оси на поле 20x50.
# Результат должен получиться таким
for row in range(20):
    for col in range(50):
        if row == 9:
            print('-', end = '')
        elif col == 24:
            print('|', end = ' ')
        else:
            print(' ', end='')
    print()