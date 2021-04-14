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


class Fight:

    def __init__(self):
        self.warriors = [index for index in range(2)]

    def info(self):
        for i_war in self.warriors:
            print('war:', i_war, 'health: ', Warrior.health)

    def hit(self):
        fighter = choice(self.warriors)
        print('Бьет воин: ', self.warriors[fighter])
        # if fighter == 0:
        #     Fight.1 =

fight = Fight()
fight.info()
fight.hit()