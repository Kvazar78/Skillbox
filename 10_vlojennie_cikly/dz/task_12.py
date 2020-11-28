# Автограф разрабочика
#
# Напишите программу, которая печатает на экране ваше имя в прямоугольной
# рамке. Для вертикальных линий используйте символ вертикального штриха “|”,
# а для горизонтальных - дефис “-”.
name = input('Введите имя: ')
countSym = 0

for i in name:
    countSym += 1

for row in range(3):
    for col in range(countSym + 4):
        if col == 0 or col == countSym + 3:
            print('|', end='')
        # if row == 1 and col == (countSym + 3) - countSym:
        #     print(name, end='')
        elif row == 0 or row == 2:
            print('-', end='')
        else:
            print(' ', end='')
    print()
print(countSym)
