from random import randint


class Human:
    corpse_flag = False

    def __init__(self, name):
        self.name = name
        self.satiety = 50
        self.house = House()

    def action(self):
        fotune = randint(1, 6)
        if fotune == 1:
            self.eat()
        elif fotune == 2:
            self.shopping()
        elif fotune == 3:
            self.go_to_work()
        elif fotune == 4:

    def eat(self):
        if self.house.food > 10 and self.satiety < 20:
            self.house.food -= 10
            self.satiety += 10
            print('Хорошо покушал...!')
        else:
            print(f'Так как сейчас в доме {self.house.food}, то жрать особо не чего...')

    def go_to_work(self):
        if self.satiety >= 15:
            self.satiety -= 15
            self.house.money += 20
            print(f'{self.name} поработал, заработал но и проголодался...', self._status_house())
        else:
            print(self._info_hunger(), 'топать на работу, надо поесть!')

    def shopping(self):
        if self.house.money > 10:
            self.house.money -= 10
            self.house.food += 15
            print('Продукты куплены, деньги потрачены', self._status_house())
        else:
            print(f'У {self.name} мало денег! Надо поработать!')

    def play(self):
        if self.satiety > 10:
            self.satiety -= 10
        else:
            print(self._info_hunger(), 'играть, надо поесть!')
            self.eat()

    def _status_house(self):
        return f'Сейчас в доме {self.house.food} еды и {self.house.money} денег'

    def _info_hunger(self):
        return f'Что-то {self.name} голодный чтобы'


class House:

    def __init__(self):
        self.food = 50
        self.money = 0


person = Human('Kolya')

while person.satiety > 0:
    fortune = randint(1, 6)
