# Корабли
#
# Даны два класса кораблей — грузовой и военный. У каждого из этих кораблей есть своя модель, и каждый может сделать два действия:
# сообщить свою модель и идти по воде.
#
# Грузовой корабль имеет такой атрибут, как заполненность, изначально он равен нулю. У него есть ещё два действия:
# погрузить и выгрузить груз с корабля.
#
# У военного же корабля нет никаких грузов, есть только оружие, которое передаётся вместе с моделью.
# Также, вместо погрузки и выгрузки, у него есть другое действие — атаковать.
#
# Реализуйте классы грузового и военного кораблей. Для этого выделите общие атрибуты и методы в отдельный класс «Корабль»
# и используйте наследование. Не забудьте про функцию super в дочерних классах.
class Ship:

    def __init__(self, model):
        self.__model = model

    def __str__(self):
        return f'Корабль модели {self.__model}'

    def sail(self):
        print(f'Корабль {self.__model} куда-то поплыл...')

    def get_model(self):
        return self.__model


class WarShip(Ship):

    def __init__(self, model, weapon):
        super().__init__(model)
        self.weapon = weapon

    def attack(self):
        print(f'Корабль {self.get_model()} атакует используя {self.weapon}')


class CargoShip(Ship):

    def __init__(self, model):
        super().__init__(model)
        self.__tonnage = 0

    def get_tonnage(self):
        return self.__tonnage

    def set_tonnage(self, cargo):
        self.__tonnage += cargo

    def cargo_load(self, cargo):
        if isinstance(cargo, int):
            self.set_tonnage(cargo)
        else:
            raise Exception('Вы что там грузите?!')

    def cargo_unload(self, cargo):
        if isinstance(cargo, int):
            if cargo < self.get_tonnage():
                cargo *= -1
                self.set_tonnage(cargo)
            else:
                print(f'Внимание на корабле {self.get_model()} всего {self.get_tonnage()} груза!')
        else:
            raise Exception('Выгружать можно только цифры ;)')


warship = WarShip('wqe', 'minigun')
cargoship = CargoShip('aaas')
print(warship)
warship.sail()
warship.attack()

print(cargoship)
cargoship.cargo_load(5)
print(cargoship.get_tonnage())
cargoship.sail()
cargoship.cargo_unload(3)
print(cargoship.get_tonnage())
