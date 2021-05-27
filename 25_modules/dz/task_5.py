# А-а-автомобиль!
#
# Автомобиль имеет координаты своего положения и угол, описывающий направление движения. Он может быть изначально поставлен
# в любую точку с любым направлением (конструктор), может проехать в выбранном направлении определённое расстояние и может
# повернуть, то есть изменить текущее направление на любое другое (передаём привет математике и формулам).
#
# Реализуйте класс автомобиля, а также класс, который будет описывать автобус. Кроме того, что имеется у автомобиля, у автобуса
# должны быть поля, содержащие число пассажиров и количество полученных денег, изначально равные нулю. Также должны быть методы
# «войти» и «выйти», изменяющие число пассажиров. Наконец, метод move должен быть переопределён, чтобы увеличивать количество
# денег в соответствии с количеством пассажиров и пройденным расстоянием.
from random import randint
import math


class Transport:

    def __init__(self, x=randint(0, 10), y=randint(0, 10), angle=randint(1, 360)):
        self.__x = x
        self.__y = y
        self.__angle = angle

    def __str__(self):
        return f'Машина сейчас в координатах (x, y) - {round(self.get_x(), 2)}, {round(self.get_y(), 2)}. Направление - {self.get_angle()} градусов'

    def get_angle(self):
        return self.__angle

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def set_angle(self, angle):
        self

    def set_x(self, x):
        self.__x += x

    def set_y(self, y):
        self.__y += y

    def move(self, distance):
        # x = distance * math.cos(self.get_angle())
        # y = distance * math.sin(self.get_angle())
        self.set_x(distance * math.cos(self.get_angle()))
        self.set_y(distance * math.sin(self.get_angle()))


car1 = Transport()
print(car1)
car1.move(3)
print(car1)

