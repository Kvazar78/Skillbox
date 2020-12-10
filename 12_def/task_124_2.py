# Почта 2

# На почте немного поменялись правила: теперь в почтовом извещении нужно указывать фамилию, 
# имя, страну проживания, город, улицу, номер дома и номер квартиры.

# Реализуйте функцию, которая получает все эти данные и выводит на экран. В программе вызовите
#  функцию 3 раза с разными значениями аргументов.

# Подсказка: 7 аргументов

def card(secondname, firstname, country, city, street, home, apartment):
    print(f'\nФамилия: {secondname}')
    print(f'Имя: {firstname}')
    print(f'Страна проживания: {country}')
    print(f'Город: {city}')
    print(f'Улица: {street}')
    print(f'Дом: {home}')
    print(f'Квартира: {apartment}')

firstname = input('Введите имя: ')
secondname = input('Введите фамилию: ')
country = input('Введите страну проживания: ')
city = input('Введите город: ')
street = input('Введите улицу: ')
home = int(input('Введите номер дома: '))
apartment = int(input('Введите номер квартиры: '))

for i in range(3):
    card(secondname, firstname, country, city, street, home, apartment)