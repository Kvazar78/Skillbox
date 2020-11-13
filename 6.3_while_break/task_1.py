# Представим, что у нас далёкое будущее и мы можем заниматься спортом
# на планетах со странными перепадами температур. Спортсмен бегает по
# стадиону до тех пор, пока температура на улице больше 15 градусов.
# Он пробегает 20 метров, затем температура падает на два градуса, и,
# если уже в этот момент она стала меньше либо равна 15 градусам, спорт
# сразу заканчивается. Если же всё в порядке, то он проходит пешком
# ещё 10 метров. Затем всё это повторяется.
#
# Напишите программу, которая спрашивает у пользователя, сколько на улице
# градусов, и, исходя из погоды, считает количество пройденных по стадиону
# метров и выводит ответ на экран.
weather = int(input('Сколько на улице градусов? '))
distance = 0
while weather > 15:
    distance +=20
    weather -= 2
    if weather <= 15:
        break
    distance += 10
print(f'Пройдено {distance} метров')