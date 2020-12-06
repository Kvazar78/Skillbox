# В рамках разработки шахматного ИИ стоит новая задача. По заданным вещественным координатам
# коня и второй точки программа должна определить может ли конь ходить в эту точку. Используйте
# как можно меньше конструкций if и логических операторов. Обеспечьте контроль ввода.
#
# Пример:
#
# Введите местоположение коня:
# 0.071
# 0.118
#
# Введите местоположение точки на доске:
# 0.213
# 0.068
#
# Конь в клетке (0, 1). Точка в клетке (2, 0).
# Да, конь может ходить в эту точку.
flag_coordinates = False

while flag_coordinates ==False:
    print('Введите местоположение коня')
    x = float(input(': '))
    y = float(input(': '))
    print('\nВведите местоположение точки на доске')
    x_dot = float(input(': '))
    y_dot = float(input(': '))
    if 0 < x < 0.8 and 0 < y < 0.8 and 0 < x_dot < 0.8 and 0 < y_dot < 0.8:
        flag_coordinates = True
    else:
        print('Придется вводить все заново - где-то опечата!')

x = int((x * 10) % 10)
y = int((y * 10) % 10)
x_dot = int((x_dot * 10) % 10)
y_dot = int((y_dot * 10) % 10)

print(f'Конь в клетке ({x}, {y}). Точка в клетке ({x_dot}, {y_dot}).')
flag_Xmove = False
flag_Ymove = False

list_x = [x + 2, x - 2, x + 1, x - 1]
list_y = [y + 2, y - 2, y + 1, y - 1]

for i in list_x:
    if i == x_dot:
        flag_Xmove = True
        break
for i in list_y:
    if i == y_dot:
        flag_Ymove = True
        break

if flag_Xmove and flag_Ymove:
    print('Да, конь может ходить в эту точку.')
else:
    print('Сюда ходить нельзя')