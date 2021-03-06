# Совместное проживание
#
# Для того чтобы понять, стоит ли Артёму жить с кем-то или всё же остаться в гордом одиночестве, он решил провести довольно
# необычное исследование. Для этого он реализовал модель человека и модель дома.
#
# Человек может:
#
#     Есть (+ сытость, − еда).
#     Работать (− сытость, + деньги).
#     Играть (− сытость).
#     Ходить в магазин за едой (+ еда, − деньги).
#
# У человека есть имя, степень сытости (изначально 50) и дом.
#
# В доме есть холодильник с едой (изначально 50 еды) и тумбочка с деньгами (изначально 0 денег).
#
# Если сытость человека становится меньше нуля, то человек умирает.
#
# Логика действий человека определяется следующим образом:
#
#     Генерируется число кубика от 1 до 6.
#     Если сытость < 20, то поесть.
#     Иначе, если еды в доме < 10, то сходить в магазин.
#     Иначе, если денег в доме < 50, то работать.
#     Иначе, если кубик равен 1, то работать.
#     Иначе, если кубик равен 2, то поесть.
#     Иначе играть.
#
#
# По такой логике эксперимента человеку надо прожить 365 дней.
#
#
# Реализуйте такую программу и создайте двух людей, живущих в одном доме. Проверьте работу программы несколько раз.
#
# Надеемся, эти люди живы...


class Human:

    def __init__(self, name, satiety=50):
        self.name = name
        self.satiety = satiety  # Сытость
        self.holod = Refrigerator()
        self.safe = Safe()

    def action(self):
        fortune = ra
    def status(self):
        if self.safe.money < 50:
            print(f'Денег {self.safe.money} - придется топать на работу!')
            self.work()
        elif self.satiety <= 0:
            print(f'{self.name} проголодался и перешел в мир иной...')
        elif self.satiety < 20:
            print(f'{self.name} хочет кушать и нырнул в холодильник...')
            self.eat()
        return self.satiety

    def eat(self):
        if self.holod.food > 20:
            self.holod.food -= 20
            print('В холодильнике мало еды - пошли в магазин')
            self.shopping()
            return f'В холодильнике убавилось продуктов, осталось {self.holod.food}'
        else:
            print('Т.к. еды мало - придется пойти поработать :(')
            self.work()

    def work(self):
        self.satiety -= 20
        self.safe.money += 25

    def play(self):
        print('Скучно? Ну поиграй!')
        self.satiety -= 10

    def shopping(self):
        if self.safe.money > 25:
            self.holod.food += 25
            self.safe.money -= 15
        else:
            print('Недостаточно налички - чешем на работу...')
            self.work()


class Refrigerator:

    def __init__(self, food=50):
        self.food = food

class Safe:

    def __init__(self, money=0):
        self.money = money


person = Human('Vasya')
# birysa = Refrigerator()
print(person.holod.food())