#  Корабли
#
# Даны два класса кораблей — грузовой и военный. У каждого из этих кораблей есть своя модель, и каждый может
#  сделать два действия: сообщить свою модель и идти по воде.
#
# Грузовой корабль имеет такой атрибут, как заполненность, изначально он равен нулю. У него есть ещё два действия:
#  погрузить и выгрузить груз с корабля.
#
# У военного же корабля нет никаких грузов, есть только оружие, которое передаётся вместе с моделью. Также,
#  вместо погрузки и выгрузки, у него есть другое действие — атаковать.
#
# Реализуйте классы грузового и военного кораблей. Для этого выделите общие атрибуты и методы в отдельный класс
# «Корабль» и используйте наследование. Не забудьте про функцию super в дочерних классах.
class Ship:

    def __init__(self, model):
        self.model = model

    def info(self):
        print(f'Корабль модели {self.model}')

    def sail(self):
        print(f'Корабль модели {self.model} куда-то поплыл...')


class WarShip(Ship):

    def __init__(self, model, weapon):
        super().__init__(model)
        self.weapon = weapon

    def attack(self):
        print(f'Корабль модели {self.model} в кого-то шмальнул из {self.weapon}...')


class CargoShip(Ship):

    def __init__(self, model):
        super().__init__(model)
        self.tonnage = 0

    def submerge(self):
        self.tonnage += 1
        print(f'Текущая загруженность корабля модели {self.model} - {self.tonnage}')

    def unloading(self):
        if self.tonnage > 0:
            self.tonnage -= 1
            print(f'Текущая загруженность корабля модели {self.model} - {self.tonnage}')
        else:
            print(f'Разгрузка невозможна корабля модели {self.model} пустой!')


war = WarShip('Орлан', 'калибр')
cargo = CargoShip('Воровайка')

war.info()
war.sail()
war.attack()

cargo.info()
cargo.unloading()
cargo.submerge()