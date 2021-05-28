# Совместное проживание 2
#
# Артём увлёкся предыдущим экспериментом и решил расширить его, создав целую семью из Мужа, Жены и Кота. Условия эксперимента следующие.
#
# # Каждый день участники жизни могут делать только одно действие. Все вместе они должны прожить год и не умереть.
# #
# # Муж может:
# #     есть,
# #     играть,
# #     ходить на работу.
# #
# # Жена может:
# #     есть,
# #     покупать продукты,
# #     покупать шубу,
# #     убираться в доме.
# #
# # Кот может:
# #     есть,
# #     спать,
# #     драть обои.
# #
# # Все они живут в одном доме, дом характеризуется:
# #       кол-во денег в тумбочке (вначале 100),
# #       кол-во еды в холодильнике (вначале 50),
# #       еда для кота (вначале 30),
# #       кол-во грязи (вначале 0).
# #
# # У людей есть имя, степень сытости (вначале 30) и степень счастья (вначале 100). Все люди могут гладить кота (+5 к счастью).
# # У кота есть имя и степень сытости (вначале 30).
# #
# # Любое действие (в том числе и кота), кроме «есть», приводит к уменьшению степени сытости на 10 пунктов.
# # Взрослые едят максимум по 30 единиц еды, степень сытости растёт на один пункт за один пункт еды.
# # Кот ест максимум по 10 единиц еды, степень сытости растёт на два пункта за один пункт еды.
# #
# # Степень сытости не должна падать ниже нуля, иначе человек или кот умрёт от голода.
# #
# # Деньги в тумбочку добавляет муж, после работы — сразу 150 единиц.
# #
# # Еда стоит 10 денег за 10 единиц еды. Шуба стоит 350 единиц.
# #
# # Еда для кота тоже покупается: за 10 денег 10 еды.
# #
# # Грязь добавляется каждый день по пять пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# #
# # Если кот дерёт обои, то грязи тоже становится больше на пять пунктов.
# #
# # Если в доме грязи больше 90, у людей падает степень счастья каждый день на 10 пунктов.
# #
# # Степень счастья растёт: у мужа от игры в компьютер (на 20), у жены от покупки шубы (на 60, но шуба дорогая).
# #
# # Степень счастья не должна падать ниже 10, иначе человек умирает от депрессии.
# #
# #
# # Реализуйте такую программу. Подведите итоги жизни за год: сколько было заработано денег, сколько съедено еды, сколько куплено шуб.
# #
# # Дополнительно: добавьте ещё ребёнка и несколько котов.
import random


class House:
    '''
    Класс описывающий дом

    Attributes:
        __money - количество денег в доме
        __food  - количество еды в холодильнике
        __cat_food - количество еды для кота
        __mud   - количество грязи в доме
    '''

    def __init__(self):
        self.__money = 100
        self.__food = 50
        self.__cat_food = 30
        self.__mud = 0

    def get_food(self):
        return self.__food

    def get_cat_food(self):
        return self.__cat_food

    def set_money(self, money):
        '''
        Сеттер для изменения количества денег в доме

        Args:
            money (int) - передается количество потраченных/заработанных денег
        '''
        self.__money += money

    def set_food(self, food):
        '''
        Сеттер для изменения количества еды в доме

        Args:
            food (int) - передается количество купленной/съеденной еды
        '''
        self.__food += food

    def set_cat_food(self, cat_food):
        '''
        Сеттер для изменения количества еды для кота в доме

        Args:
            cat_food (int) - передается количество купленной/съеденной еды для этого ушлепка
        '''
        self.__cat_food += cat_food

    def set_mud(self, mud):
        '''
        Сеттер для изменения количества грязи в доме

        Args:
            mud (int) - передается количество грязи занесенной/убранной в доме
        '''
        self.__mud += mud
        if self.__mud > 90:
            People.set_happiness(-10)


class Residents:
    '''
    Базовый класс, отписывающий жильца дома

    Args:
        name (str) - передается имя жителя
        house -   передается дом проживания
    Attributes:
        __satiety - задается начальное значение сытости
    '''
    def __init__(self, name, house):
        self.__name = name
        self.house = house
        self.__satiety = 30

    def set_satiety(self, satiety):
        '''
        Сеттер для изменения степени сытости

        Args:
             satiety (int) - передается некое количество сытости
        '''
        self.__satiety += satiety
        if self.get_satiety() < 0:
            raise Exception(f'{self.get_name()} умер с голоду...')
        elif self.get_satiety() < 10:
            print('Надо пойти поесть...')
            self.eat()

    def get_satiety(self):
        '''
        Геттер для получения значения уровня счастья
        :return:  __satiety
        '''
        return self.__satiety

    def get_name(self):
        return self.__name

    def eat(self):
        pass

    # def eat_for_all(self, value):



class People(Residents):
    '''
    Базовый класс людей. Родитель: Residents

    Args:
        name (str) - передается имя жителя
        house -   передается дом проживания
    Attributes:
        __happiness (int) - задается начальное значение счастья
    '''

    def __init__(self, name, house):
        super().__init__(name, house)
        self.__happiness = 100

    def set_happiness(self, happiness):
        '''
        Сеттер для изменения уровня счастья

        Args:
            happiness (int) - передается некое количество счастья
        '''
        self.__happiness += happiness
        if self.get_happiness() < 10:
            raise Exception(f'{self.get_name()} умирает от депрессии...')

    def get_happiness(self):
        '''
        Геттер для получения значения уровня счастья
        :return: __happiness
        '''
        return self.__happiness

    def pet_cat(self):
        '''
        Метод "погладить кота" - добавляет к атрибуту __happiness значение 5
        '''
        self.set_happiness(5)

    def eat(self):
        value_eat = random.randint(1, 30)
        if self.house.get_food() > value_eat:
            self.house.set_food(value_eat * -1)
            self.set_satiety(value_eat)
        else:
            print(f'{self.get_name()} не хватило еды... Жена чешет за продуктами.')
            Wife.buy_food()


class Husband(People):

    def __init__(self, name, house):
        super().__init__(name, house)

    def play(self):
        self.set_satiety(-10)
        self.set_happiness(20)
        print(f'Поиграл... значение сытости {self.set_satiety()}, счастья {self.get_happiness()}')

    def go_to_work(self):
        self.set_satiety(-10)
        self.house.set_money(150)


class Wife(People):

    def __init__(self, name, house):
        super().__init__(name, house)

    def buy_food(self):
        if self.house.get_food < 50
        self.set_satiety(-10)
        pass

    def buy_coat(self):
        self.set_satiety(-10)
        pass

    def clean_house(self):
        self.set_satiety(-10)
        pass


class Cat(Residents):

    def __init__(self, name, house):
        super().__init__(name, house)

    def eat(self):
        value_eat = random.randint(1, 10)
        if self.house.get_cat_food() > value_eat:
            self.house.set_food(value_eat * -1)
            self.set_satiety(value_eat * 2)
        else:
            print(f'Коту {self.get_name()} не хватает еды. Хозяйка идет за продуктами')
            Wife.buy_food()

    def sleep(self):
        self.set_satiety(-10)

    def tear_wallpaper(self):
        self.set_satiety(-10)
        self.house.set_mud(5)