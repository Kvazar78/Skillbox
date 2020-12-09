# Часы
#
# С начала суток прошло H часов, M минут, S секунд (0≤H<12, 0≤M<60, 0≤S<60). По данным числам
# H, M, S определите угол (в градусах), на который повернулаcь часовая стрелка с начала суток и
# выведите его в виде действительного числа.
#
# При решении этой задачи нельзя пользоваться условными операторами и циклами.
h = int(input('Введи час: '))
m = int(input('Введи минуты: '))
s = int(input('Введи секунды: '))

angle_hour = float(h * 30) + (30 / 60) * m

print(f'\nЧасовая стрелка повернулась на {angle_hour} градусов')
print(f'Минутная стрелка повернулась на {float(m * 6)} градусов')
print(f'Секундная стрелка повернулась на {float(s * 6)} градусов')