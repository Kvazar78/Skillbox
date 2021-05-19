# Роботы
#
# На военную базу завезли несколько интересных моделей роботов, которые похожи между собой, но имеют немного разные функции.
# У каждого робота есть номер модели и действие operate, которое означает, что делает робот. Особенности роботов следующие:
#
#     У робота-пылесоса есть мешок для мусора, изначально он пустой (0). При команде operate робот сообщает, что он пылесосит пол,
# и выводит текущую заполняемость мешка.
#     У военного робота есть оружие, и при команде operate он выводит сообщение о защите военного объекта с помощью этого оружия.
#
# Ещё есть робот — подводная лодка, который также является военным. У этого робота есть значение глубины, и при команде
# operate он делает то же, что и военный робот, плюс сообщает, что охрана ведётся под водой.
#
# Напишите программу, которая реализует все необходимые классы роботов.
class Robot:

    def __init__(self, model):
        self.__model = model

    def get_model(self):
        return self.__model

    def operate(self):
        pass


class HooverBot(Robot):
    __garbage_bag = 0

    def __init__(self, model):
        super().__init__(model)

    def operate(self):
        self.set_garbage_load()
        print(f'Робот {self.get_model()} начал пылесосить. Емкость заполнена на {self.get_garbage_bag()}...')

    def set_garbage_load(self):
        self.__garbage_bag += 1

    def get_garbage_bag(self):
        return self.__garbage_bag


class WarBot(Robot):

    def __init__(self, model, weapon):
        super().__init__(model)
        self.weapon = weapon

    def operate(self):
        print(f'Робот {self.get_model()} приступил к охране объекта используя {self.weapon}')


class SubmarineBot(Robot):
    __depth = 0

    def __init__(self, model, weapon):
        super().__init__(model)
        self.weapon = weapon

    def set_depth(self, value):
        self.__depth -= value

    def get_depth(self):
        return self.__depth

    def operate(self):
        self.set_depth(15)
        print(f'Робот {self.get_model()} приступил к охране объекта используя {self.weapon} на глубине {self.get_depth()}')


hb1 = HooverBot('Prilips')
wb1 = WarBot('r2d2', 'vulcan')
sb1 = SubmarineBot('YellowSubmarine', 'torpedos')

hb1.operate()
wb1.operate()
sb1.operate()
hb1.operate()