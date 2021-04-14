# Драка
#
# Вы работаете в команде разработчиков мобильной игры, и вам досталась вот такая часть от ТЗ заказчика:
#
# Есть два юнита, каждый из них называется «Воин». Каждому устанавливается здоровье в 100 очков. Они бьют друг друга
# в случайном порядке. Тот, кто бьёт, здоровья не теряет. У того, кого бьют, оно уменьшается на 20 очков от одного удара.
# После каждого удара надо выводить сообщение, какой юнит атаковал и сколько у противника осталось здоровья. Как только у
# кого-то заканчивается ресурс здоровья, программа завершается сообщением о том, кто одержал победу.
from random import choice


class Warrior:
    health = 100

    def __init__(self, index):
        self.index = index


class Fight:

    def __init__(self):
        self.warriors = [Warrior(index) for index in range(2)]

    def hit(self):
        while self.warriors[0].health > 0 and self.warriors[1].health > 0:
            fighter = choice(self.warriors)
            print('Бьет воин: ', fighter.index + 1)
            if fighter.index == 0:
                self.warriors[1].health -= 20
                self.hit_info(1)
            else:
                self.warriors[0].health -= 20
                self.hit_info(0)

        for i_war in self.warriors:
            if i_war.health == 0:
                self.end(i_war.index + 1)

    def hit_info(self, injured):
        print('Воин {} потерял 20 очков здоровья, теперь у него {} очков здоровья'.format(
            self.warriors[injured].index + 1, self.warriors[injured].health
        ))

    def end(self, looser):
        print('\nПроиграл {} воин.'.format(looser))


fight = Fight()
fight.hit()