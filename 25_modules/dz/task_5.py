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

    def __init__(self, model, x=randint(0, 10), y=randint(0, 10), angle=randint(1, 360)):
        self.__model = model
        self.__x = x
        self.__y = y
        self.__angle = angle

    def __str__(self):
        return f'{self.__model} сейчас в координатах (x, y) - {round(self.get_x(), 2)}, {round(self.get_y(), 2)}. Направление - {self.get_angle()} градусов'

    def get_angle(self):
        return self.__angle

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get_model(self):
        return self.__model

    def set_angle(self, angle):
        self.__angle = angle

    def set_x(self, x):
        self.__x += x

    def set_y(self, y):
        self.__y += y

    def move(self, distance):
        print(f'\nЕдем вперед на расстояние {distance}...')
        self.set_x(distance * math.cos(self.get_angle()))
        self.set_y(distance * math.sin(self.get_angle()))


class Bus(Transport):

    def __init__(self, model, x=randint(0, 10), y=randint(0, 10), angle=randint(1, 360)):
        super().__init__(model, x, y, angle)
        self.__num_pass = 0
        self.__money = 0

    def get_num_pass(self):
        return self.__num_pass

    def get_money(self):
        return self.__money

    def set_num_pass(self, num_pass):
        self.__num_pass += num_pass

    def set_money(self, money):
        self.__money += money

    def come_in(self, num_pass):
        self.set_num_pass(num_pass)

    def go_out(self, num_pass):
        self.set_num_pass(num_pass * -1)

    def move(self, distance):
        super().move(distance)
        self.set_money(self.get_num_pass() * distance * 10)


car1 = Transport("VAZ")
print(car1)
car1.move(3)
car1.set_angle(90)
print(car1)
bus1 = Bus("LIAZ")
bus1.come_in(3)
print(f'В автобус марки {bus1.get_model()} зашло {bus1.get_num_pass()} пассажиров')
print(bus1)
bus1.move(4)
print(bus1)
it_was_pass = bus1.get_num_pass()
print(f'Заработано - {bus1.get_money()} рублей')
bus1.go_out(2)
print(f'Вышло {it_was_pass - bus1.get_num_pass()} пассажиров')