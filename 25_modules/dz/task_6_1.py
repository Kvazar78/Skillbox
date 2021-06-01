import random


class Death(Exception):
    pass


class House:

    def __init__(self):
        self.__money = 100
        self.__food = 50
        self.__cat_food = 30
        self.__mud = 0

    def get_money(self):
        return self.__money

    def get_food(self):
        return self.__food

    def get_cat_food(self):
        return self.__cat_food

    def get_mud(self):
        return self.__mud

    def set_money(self, money):
        self.__money += money
        if self.get_money() <=0:
            raise Exception('В доме закончились деньги!')

    def set_food(self, food):
        self.__food += food
        if self.get_food() <=0:
            raise Exception('В доме закончилась еда!')

    def set_cat_food(self, cat_food):
        self.__cat_food += cat_food
        if self.get_cat_food() <= 0:
            raise Exception('Коту нечего жрать!')

    def set_mud(self, mud):
        self.__mud += mud
        if self.get_mud() > 90:
            print(f'Грязи уже - {self.get_mud()}... Пора бы и прибраться!')


class Residents:

    def __init__(self, name, house):
        self.__name = name
        self.house = house
        self.__satiety = 30

    def get_name(self):
        return self.__name

    def get_satiety(self):
        return self.__satiety

    def set_satiety(self, satiety):
        self.__satiety += satiety


class Cat(Residents):

    def __init__(self, name, house):
        super().__init__(name, house)

    def act(self):
        if self.get_satiety() > 0:
            fortuna = random.randint(1, 3)
            print('Сегодня кот решил', end=' ')
            if fortuna == 1:
                print('пожрать...')
                self.cat_eat()
            elif fortuna == 2:
                print('поспать...')
                self.sleep()
            else:
                print('порвать обои...')
                self.tear_wallpaper()
        else:
            raise Death('Кот сдох! Наконец-то!')

    def cat_eat(self):
        value_eat = random.randint(1, 10)
        if self.house.get_cat_food() > value_eat:
            self.house.set_cat_food(value_eat * -1)
            print(f'Кот {self.get_name()} сожрал {value_eat} еды и в холодильнике осталось {self.house.get_cat_food()} кошачей еды... Ска!')
            self.set_satiety(value_eat * 2)
            print(f'Зато теперь он доволен и сытость его {self.get_satiety()}')

    def sleep(self):
        self.set_satiety(-10)
        print(f'Кот решил поспать и до кучи проголодался до уровня {self.get_satiety()}')

    def tear_wallpaper(self):
        self.set_satiety(-10)
        self.house.set_mud(5)
        print(f'Кота вдруг посетила шиза и он подрал обои... Мало того что он проголодался до {self.get_satiety()}, так еще и мусора в дом добавил - {self.house.get_mud()}')


class People(Residents):

    def __init__(self, name, house):
        super().__init__(name, house)
        self.__happiness = 100

    def get_happiness(self):
        return self.__happiness

    def set_happiness(self, happy):
        self.__happiness += happy
        if self.get_happiness() <= 0:
            raise Death(f'объект {self.get_name()} взгрустнул до смерти...')

    def people_eat(self):
        value_eat = random.randint(1, 30)
        if self.house.get_food() > value_eat:
            self.house.set_food(value_eat * -1)
            self.set_satiety(value_eat)
        else:
            print(f'{self.get_name()} не хватило еды... Жена чешет за продуктами.')
            Wife.buy_food()


crazy_house = House()
cat1 = Cat('Васька', crazy_house)
lst_residence = [cat1]

try:
    for i_day in range(1, 366):
        # for i_elem in lst_residence:
        #     if i_elem.get_satiety() <= 0:
        #         raise Exception(f'объект {i_elem.get_name()} не выжил...')
        print(f'Наступил {i_day} день... Понеслась!')
        cat1.act()

except Death as error:
    print('\nПрожить год не вышло -', end=' ')
    print(str(error))

else:
    print('\nГод прожит без потерь!')