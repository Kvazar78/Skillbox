# Машина
#
# Напишите класс Toyota, состоящий из четырёх статических атрибутов:
#
#     цвет машины (например, красный),
#     цена (один миллион),
#     максимальная скорость (200),
#     текущая скорость (ноль).
#
# Создайте три экземпляра класса и каждому из них поменяйте значение текущей скорости на случайное
# число от нуля до 200.
import random


class Toyota:
    color = 'red'
    price = 1000000
    max_speed = 200
    cur_speed = 0


car1, car2, car3 = Toyota(), Toyota(), Toyota()
car1.max_speed = random.randint(0, 200)
car2.max_speed = random.randint(0, 200)
car3.max_speed = random.randint(0, 200)

print(car1.max_speed)
print(car2.max_speed)
print(car3.max_speed)
