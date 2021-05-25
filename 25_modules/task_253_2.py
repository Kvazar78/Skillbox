#  Роботы
#
# На военную базу завезли несколько интересных моделей роботов, которые похожи между собой, но имеют немного разные функции.
#  У каждого робота есть номер модели и действие operate, которое означает, что делает робот. Особенности роботов следующие:
#
#     У робота-пылесоса есть мешок для мусора, изначально он пустой (0). При команде operate робот сообщает, что он
#  пылесосит пол, и выводит текущую заполняемость мешка.
#     У военного робота есть оружие, и при команде operate он выводит сообщение о защите военного объекта с помощью этого оружия.
#
# Ещё есть робот — подводная лодка, который также является военным. У этого робота есть значение глубины, и при команде
#  operate он делает то же, что и военный робот, плюс сообщает, что охрана ведётся под водой.
#
# Напишите программу, которая реализует все необходимые классы роботов.
class Robot:

    def __init__(self, model):
        self.model = model

    def operate(self):
        pass


class HooverRobot(Robot):

    def __init__(self, model):
        super().__init__(model)
        self.garbage_bag = 0

    def operate(self):
        self.garbage_bag += 1
        print(f'Робот {self.model} пылесосит пол, мешок загружен на {self.garbage_bag}')


class WarRobot(Robot):

    def __init__(self, model, weapon):
        super().__init__(model)
        self.weapon = weapon

    def operate(self):
        print(f'Робот {self.model} приступил к охране объекта с помощью {self.weapon}')


class SubmarineRobot(Robot):

    def __init__(self, model, weapon, depth=0):
        super().__init__(model)
        self.weapon = weapon
        self.depth = depth

    def operate(self):
        self.depth += 10
        print(f'Робот {self.model} приступил к охране объекта с помощью {self.weapon} на глубине {self.depth}')


bot1 = HooverRobot('Xiomi')
bot2 = WarRobot('r2d2', 'лазер')
bot3 = SubmarineRobot('Акула', 'торпеды')

bot1.operate()
bot2.operate()
bot3.operate()