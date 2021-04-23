from random import randint


class Human:
    corpse_flag = False

    def __init__(self, name, house):
        self.name = name
        self.satiety = 50
        self.house = house

    def act(self):
        fortuna = randint(1, 4)
        if fortuna == 1:
            self.eat()
        elif fortuna == 2:
            self.go_to_work()
        elif fortuna == 3:
            self.shopping()
        elif fortuna == 4:
            self.play()

    def eat(self):
        if self.satiety < 20 and self.house.food > 10:
            self.house.food -= 10
            self.satiety += 10
            print('Хорошо покушал...!')
        else:
            print(f'Так как сейчас в доме {self.house.food}, то жрать особо не чего...')
        self._status_house()

    def go_to_work(self):
        if self.house.money < 50 and self.satiety >= 15:
            self.satiety -= 15
            self.house.money += 20
            print(f'{self.name} поработал, заработал но и проголодался...\n', self._status_house())
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

    def _status_house(self):
        return f'Сейчас в доме {self.house.food} еды и {self.house.money} денег'

    def _info_hunger(self):
        return f'Что-то {self.name} голодный чтобы'


class House:

    def __init__(self):
        self.food = 50
        self.money = 0


crazy_house = House()
person = Human('Kolya', crazy_house)
count_days = 0

for _ in range(365):
    if person.satiety <= 0:
        print(f'{person.name} - сдох!')
        break
    else:
        count_days += 1
        print(f'День - {count_days}:')
        person.act()