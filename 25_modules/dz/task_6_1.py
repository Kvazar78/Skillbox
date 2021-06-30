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
        if self.get_money() <= 0:
            raise Exception('В доме закончились деньги!')

    def set_food(self, food):
        self.__food += food
        if self.get_food() <= 0:
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

    def action(self):
        if self.get_satiety() > 0:
            if self.get_satiety() > 10:
                fortuna = random.randint(1, 3)
                print(f'\nСегодня кот {self.get_name()} решил', end=' ')
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
                print(f'У кота {self.get_name()} сильно урчит в животе - пошел жрать...')
                self.cat_eat()
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
    __all_eaten = 0

    def __init__(self, name, house):
        super().__init__(name, house)
        self.__happiness = 100

    def get_all_eaten(self):
        return self.__all_eaten

    def set_all_eaten(self, value_eat):
        self.__all_eaten += value_eat

    def get_happiness(self):
        return self.__happiness

    def set_happiness(self, happy):
        self.__happiness += happy
        if self.get_happiness() <= 0:
            raise Death(f'объект {self.get_name()} взгрустнул до смерти...')

    def people_eat(self):
        value_eat = random.randint(1, 30)
        self.set_all_eaten(value_eat)
        if self.house.get_food() > value_eat:
            self.house.set_food(value_eat * -1)
            self.set_satiety(value_eat)
            print(f'Сытость {self.get_name()} составляет сейчас {self.get_satiety()}')
        else:
            print(f'{self.get_name()} не хватило еды... Жена чешет за продуктами.')

    def pet_cat(self):
        self.set_happiness(5)
        print(f'Кот поглажен, теперь уровень счастья - {self.get_happiness()}')


class Wife(People):
    __count_coat = 0

    def __init__(self, name, house):
        super().__init__(name, house)

    def get_count_coat(self):
        return self.__count_coat

    def action(self):
        print(f'\n{self.get_name()} действует:', end=' ')
        if self.get_satiety() < 10:
            print(f'У {self.get_name()} сильно урчит в животе - пошел кушать...')
            self.people_eat()
        elif self.house.get_mud() > 90:
            print('принудительная уборка')
            self.set_happiness(-10)
        elif self.house.get_cat_food() < 10 or self.house.get_food() < 60:
            print('Пошла в магазин')
            self.buy_food()
        else:
            if self.get_satiety() > 0:
                fortuna = random.randint(1, 4)
                if fortuna == 1:
                    print('Выпало покушать... ')
                    self.people_eat()
                elif fortuna == 2:
                    print('Выпало погладить кота...')
                    self.pet_cat()
                elif fortuna == 3:
                    print(f'Выпала уборка дома... На текущий момент в доме {self.house.get_mud()} грязи.')
                    self.clean_house()
                else:
                    print('Выпало - купить шубу...')
                    self.buy_coat()
            else:
                raise Death(f'{self.get_name()} умерла от неправильного образа жизни...')

    def buy_food(self):
        self.set_satiety(-10)
        buy_fo, buy_cat_fo = 0, 0
        if self.house.get_food() > 100:
            print(f'В холодильнике еще достаточно еды - {self.house.get_food()}')
        else:
            print(f'Мне с мужем надо что-то будет пожрать...')
            buy_fo = self.house.get_money() // 3 * 2
            self.house.set_food(buy_fo)
            self.house.set_money(buy_fo * -1)
        if self.house.get_cat_food() > 50:
            print(f'В холодильнике еще достаточно еды для кота - {self.house.get_cat_food()}')
        else:
            print('Надо чем-то кормить кота...')
            buy_cat_fo = self.house.get_money() // 3
            self.house.set_cat_food(buy_cat_fo)
            self.house.set_money(buy_cat_fo * -1)
        print(f'{self.get_name()} потратила на покупки {buy_cat_fo + buy_fo} рублей')

    def clean_house(self):
        self.set_satiety(-10)
        if self.house.get_mud() >= 100:
            self.house.set_mud(-100)
        else:
            if self.house.get_mud() < 20:
                self.house.set_mud(self.house.get_mud() * -1)
            else:
                self.house.set_mud(-20)
        print(f'Теперь в доме {self.house.get_mud()} грязи')

    def buy_coat(self):
        if self.house.get_money() >= 370:
            self.set_satiety(-10)
            self.house.set_money(-350)
            self.__count_coat += 1
        else:
            print(f'Черт, шубу купить не получится - мало денег ({self.house.get_money()})')


class Husband(People):
    __total_money = 0

    def __init__(self, name, house):
        super().__init__(name, house)

    def get_total_money(self):
        return self.__total_money

    def set_total_money(self, salary):
        self.__total_money += salary

    def action(self):
        print(f'\n{self.get_name()} действует:', end=' ')
        if self.get_satiety() < 10:
            print(f'У {self.get_name()} сильно урчит в животе - пошел кушать...')
            self.people_eat()
        elif self.house.get_money() < 50:
            print(f'В доме осталось мало денег - {self.get_name()} пошел работать...')
            self.go_to_work()
        else:
            if self.get_satiety() > 0:
                fortuna = random.randint(1, 4)
                if fortuna == 1:
                    print('Выпало покушать... ')
                    self.people_eat()
                elif fortuna == 2:
                    print('Выпало погладить кота...')
                    self.pet_cat()
                elif fortuna == 3:
                    print('Выпало поиграть...')
                    self.play()
                else:
                    print('Выпало - поработать...')
                    self.go_to_work()
            else:
                raise Death(f'{self.get_name()} умер от неправильного образа жизни...')

    def play(self):
        self.set_satiety(-10)
        self.set_happiness(20)
        print(f'{self.get_name()} поиграл, теперь у него счастья {self.get_happiness()}, сытость - {self.get_satiety()}')

    def go_to_work(self):
        self.set_satiety(-10)
        self.house.set_money(150)
        self.set_total_money(150)
        print(f'{self.get_name()} поработал, теперь в доме {self.house.get_money()} денег, сытость - {self.get_satiety()}')


crazy_house = House()
cat1 = Cat('Васька', crazy_house)
cat2 = Cat('Рыжик', crazy_house)
wife1 = Wife('Ира', crazy_house)
husb1 = Husband('Коля', crazy_house)
lst_residence = [wife1, husb1, cat1, cat2]

try:
    for i_day in range(1, 366):
        print(f'\nНаступил {i_day} день... Понеслась!')
        for i_elem in lst_residence:
            i_elem.action()
        print('\nСтатистика по дому на конец дня:'
              f'\n\t\t {crazy_house.get_cat_food()} еды для кота'
              f'\n\t\t{crazy_house.get_food()} еды для людей'
              f'\n\t\t{crazy_house.get_money()} рублей в заначке')

except Death as error:
    print('\nПрожить год не вышло -', end=' ')
    print(str(error))

else:
    print('\nГод прожит без потерь!')
    print(f'Жена умудрилась купить за год {wife1.get_count_coat()} шуб')
    print(f'При этом ее муж {husb1.get_name()} заработал {husb1.get_total_money()}')
    print(f'За год {husb1.get_name()} и {wife1.get_name()} слопали {husb1.get_all_eaten()} еды')
