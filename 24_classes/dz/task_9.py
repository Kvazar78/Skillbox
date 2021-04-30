from random import choice


class Pole:
    lst = [i for i in range(1, 10)]

    def input(self, player, coord):
        self.lst[coord - 1] = player.symbol

    def print_pole(self):
        count_elem = 0
        print("-" * 13)
        for i_elem in self.lst:
            count_elem += 1
            print(f'| {i_elem}', end=' ')
            if count_elem % 3 == 0:
                print('|')
                print("-" * 13)

    # def test(self):


class Player:

    def __init__(self, name, sym):
        self.name = name
        self.symbol = sym


player1 = Player('Vasya', 'X')
player2 = Player('Roma', '0')
pole1 = Pole()

pole1.print_pole()


print(first_player)
# for _ in range(4):
#     znak = input('введи координаты через пробел: ').split()
#     pole1.input(znak)
# print(pole1.pole)
# count = 0
# for i_elem in pole1.pole:
#     count += i_elem.count('x')
# print(count)
#
#
# field = range(1, 10)
# print("-" * 12)
# for i in range(3):
#     print("|", field[0 + i * 3],
#           "|", field[1 + i * 3],
#           "|", field[2 + i * 3], "|")
#     print("-" * 12)