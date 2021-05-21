# Налоги
#
# Реализуйте иерархию классов, описывающих имущество налогоплательщиков. Она должна состоять из базового класса Property и
# производных от него классов Apartment, Car и CountryHouse.
#
# Базовый класс должен иметь атрибут worth (стоимость), который передаётся в конструктор, и метод расчёта налога,
# переопределённый в каждом из производных классов. Налог на квартиру вычисляется как 1/1000 её стоимости, на машину — 1/200, на дачу — 1/500.
#
# Каждый дочерний класс должен иметь конструктор с одним параметром, передающий свой параметр конструктору базового класса.
#
# Разработайте интерфейс программы. Пусть она запрашивает у пользователя количество его денег и стоимость имущества, а затем
# выдаёт ему налог на соответствующее имущество и сколько денег ему не хватает (если это так).
class Property:

    def __init__(self, worth):
        self.__worth = worth

    def get_worth(self):
        return self.__worth

    def tax_calculation(self):
        pass


class Apartment(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def tax_calculation(self):
        return self.get_worth() / 1000


class Car(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def tax_calculation(self):
        return self.get_worth() / 200


class CountryHouse(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def tax_calculation(self):
        return self.get_worth() / 500


cash = int(input('Сколько имеется наличности? '))

app = Apartment(int(input('Укажите стоимость квартиры: ')))
car = Car(int(input('Укажите стоимость машины: ')))
ran = CountryHouse(int(input('Укажите стоимость дачи: ')))
all_tax = app.tax_calculation() + car.tax_calculation() + ran.tax_calculation()

print(f'\nРезультат вычислений:'
      f'\n\t-налог на квартиру составит - {app.tax_calculation()}'
      f'\n\t-налог на машину составит - {car.tax_calculation()}'
      f'\n\t-налог на дачу составит - {ran.tax_calculation()}'
      f'\nИТОГО: {all_tax}'
      )

if cash > all_tax:
    print('\nИмеющихся денег ({}) вам хватит чтобы оплатить налоги.'.format(str(all_tax)))
else:
    print('\nУвы... У вас всего {}, а налоговой нужно {} - придется что-то продать или искать подработку...'.format(str(cash), str(all_tax)))