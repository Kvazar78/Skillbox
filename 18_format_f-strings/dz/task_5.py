# Капитан Флинт
#
# Капитан Флинт зарыл клад на Острове сокровищ. Он оставил описание, как найти клад.
# Описание состоит из строк вида: "North 5", где  слово – одно из "North", "South",
# "East", "West", – задает направление движения, а  число – количество шагов,
# которое необходимо пройти в этом направлении.
#
# Напишите программу, которая по описанию пути к кладу определяет точные координаты
# клада, считая, что начало координат находится в начале пути, ось OX направлена на
# восток, ось OY – на север.
#
# Пример:
#
# По оси OY: South 19
# По оси OX: East 2
#
# Координаты: 2 -19
axis_oy = input('По оси OY: ').lower().split()
axis_ox = input('По оси OX: ').lower().split()
y = int(axis_oy[1])
x = int(axis_ox[1])

if 'south' in axis_oy:
    y *= (-1)

if  'west' in axis_ox:
    x *= (-1)

print('\nКоординаты:', x, y)