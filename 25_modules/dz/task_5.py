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


class Transport:

    def __init__(self, x=randint(0, 10), y=randint(0, 10), angle=randint(1, 360)):
        self.__x = x
        self.__y = y
        self.__angle = angle

