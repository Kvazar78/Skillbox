# Мы делаем текстовую игру - гонку и нам нужно вывести на экран что-то
# вроде трассы, где будут соревноваться наши машины. Напишите программу,
# которая выводит такую дорогу на экран (поле 20 на 50)
# for row in range(20):
#     for col in range(50):
#         if row == 9:
#             print('-', end='')
#         elif col == 19 - row:
#             print('/', end = ' ')
#         elif col == 29 + row:
#             print('\\', end=' ')
#         elif col == 24:
#             print('|', end=' ')
#         else:
#             print(' ', end='')
#     print()

# Что нужно сделать, чтобы обочины рисовались поверх горизонтальной линии?

for row in range(20):
    for col in range(50):
        if col == 19 - row:
            print('/', end = ' ')
        elif col == 29 + row:
            print('\\', end=' ')
        elif row == 9:
            print('-', end='')
        elif col == 24:
            print('|', end=' ')
        else:
            print(' ', end='')
    print()