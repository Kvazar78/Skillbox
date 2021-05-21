# Полёт
#
# Иногда для реализации дочерних классов используется так называемый класс-роль, где также описываются общие атрибуты и методы,
# но в программе инициализируются объекты только дочерних классов, а базовый класс-роль не трогается. К примеру, что общего у
# бабочки и ракеты? Они обе могут летать и приземляться.
#
# Реализуйте класс «Может летать».
#
# Атрибуты:
#
#     Высота = 0.
#     Скорость = 0.
#
# Методы:
#
#     Взлететь (в теле прописать pass).
#     Лететь (в теле прописать pass).
#     Приземлиться (установить высоту и скорость в значение 0).
#     Вывести высоту и скорость на экран.
#
# Затем реализуйте два дочерних класса:
#
# «Бабочка», который может:
#
#     Взлететь (высота = 1).
#     Лететь (скорость = 0.5).
#
# «Ракета», которая может:
#
#     Взлететь (высота = 500, скорость = 1000).
#     Приземлиться (высота = 0, взрыв).
#     Взорваться (тут уже что угодно).
class Can_fly:
    __height = 0
    __speed = 0
    __dead = False

    def set_height(self, height):
        self.__height = height

    def set_speed(self, speed):
        self.__speed = speed

    def _set_dead(self):
        self.__dead = True

    def get_height(self):
        return self.__height

    def get_speed(self):
        return self.__speed

    def takeoff(self): # Взлететь
        pass

    def fly(self): # Лететь
        pass

    def land(self): # Посадка
        self.set_height(0)
        self.set_speed(0)

    def __str__(self):
        if self.__dead:
            return 'Объект уничтожен...'
        else:
            return f'Текущая высота - {self.get_height()}, скорость - {self.get_speed()}'


class Butterfly(Can_fly):

    def __init__(self):
        super().__init__()

    def takeoff(self):
        self.set_height(1)

    def fly(self):
        self.set_speed(0.5)


class Rocket(Can_fly):

    def __init__(self):
        super().__init__()

    def takeoff(self):
        self.set_height(500)
        self.set_speed(1000)

    def land(self):
        self.set_height(0)
        self._set_dead()

    def explode(self):
        self._set_dead()


but1 = Butterfly()
rock1 = Rocket()

but1.takeoff()
print(but1)
but1.fly()
print(but1)

rock1.takeoff()
print(rock1)
rock1.explode()
print(rock1)