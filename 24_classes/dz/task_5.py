# Весёлая ферма 2
#
# Мы продолжаем писать игру «Весёлая ферма» и теперь необходимо её немного модернизировать.
# Всё-таки кому-то же нужно собирать урожай, и для этого нам понадобится садовник, который имеет:
#
#     Имя.
#     Грядку с растением, за которым он ухаживает (в нашем случае пока только грядка с картошкой).
#
# И может:
#
#     Ухаживать за грядкой.
#     Собирать с неё урожай (количество картошки ― пустой список).
#
# Модернизируйте программу, используя новый класс «Садовник». На всякий случай вот описание картошки
# и грядки:
#
# У картошки есть её номер в грядке, а также стадия зрелости. Она может предоставлять информацию о
# своей зрелости и расти. Всего у картошки может быть четыре стадии зрелости.
#
# Грядка с картошкой содержит список картошки, которая на ней растёт, и может, собственно,
# взращивать всю эту картошку, а также предоставлять информацию о зрелости всей картошки на своей
# территории.
#
# Проверьте работу программы, создав грядку из пяти картошек и отдав эту грядку садовнику. Пусть
# поухаживает за грядкой и соберёт урожай (а, может быть, даже и не один).
class Potato:
    maturity_dict = {0: 'еще не вырасла',
                1: 'что-то появилось из земли...',
                2: 'неплохие кусты!',
                3: 'пора собирать, а то соседи помогут...!'}

    def __init__(self, number, maturity=0):
        self.number = number
        self.maturity = maturity

    def about_potato(self):
        return f'Катрошка №{self.number} на стадии - {self.maturity_dict[self.maturity]}'

    def grows(self):
        if self.maturity < 3:
            self.maturity += 1
        self.print_state()

    def is_ripe(self):
        if self.maturity == 3:
            return True
        return False

    def print_state(self):
        print('Картошка {} сейчас {}.'.format(
            self.number, Potato.maturity_dict[self.maturity]
            ))


class Experimental_field:

    def __init__(self, quantity):
        self.list_potatoes = [Potato(i) for i in range(1, quantity + 1)]

    def everyone_grows(self):
        print('Поливаем всю грядку...')
        for i_potato in self.list_potatoes:
            i_potato.grows()


class Gardener:

    def __init__(self, name, garden_bed):
        self.name = name
        self.garden_bed = garden_bed

    def water(self):
        self.garden_bed.everyone_grows()

    def harvest(self):
        if not all([i_potato.is_ripe() for i_potato in self.garden_bed.list_potatoes]):
            print('Картошка еще не созрела!\n')
        else:
            print('Вся картошка созрела. Можно собирать!\n')


dacha = Experimental_field(5)
kolhoznik = Gardener('Kolya', dacha)

for _ in range(3):
    kolhoznik.water()
kolhoznik.harvest()