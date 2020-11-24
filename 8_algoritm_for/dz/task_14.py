# X мальчиков и Y девочек пошли в кинотеатр и купили билеты
# на подряд идущие места в одном ряду. Напишите программу,
# которая выдаст, как нужно сесть мальчикам и девочкам, чтобы
# рядом с каждым мальчиком сидела хотя бы одна девочка, а рядом
# с каждой девочкой — хотя бы один мальчик.
#
# На вход подаются два числа - кол-во мальчиков X и кол-во девочек Y.
# В ответе выведите какую-нибудь строку, в которой будет ровно X
# символов “B” (обозначающих мальчиков) и Y символов “G” (обозначающих
# девочек), удовлетворяющую условию задачи. Пробелы между символами
# выводить не нужно. Если рассадить мальчиков и девочек согласно условию
# задачи невозможно, выведите строку “Нет решения”.
#
# Пример 1:
#
# Введите кол-во мальчиков: 5
# Введите кол-во девочек: 5
# Ответ: BGBGBGBGBG
#
# Пример 2:
#
# Введите кол-во мальчиков: 5
# Введите кол-во девочек: 3
# Ответ: BGBGBBGB
#
# Пример 3:
#
# Введите кол-во мальчиков: 100
# Введите кол-во девочек: 1
# Ответ: Нет решения
boys = int(input('Введите кол-во мальчиков: '))
girls = int(input('Введите кол-во девочек: '))
string = ''

if boys / girls > 2 or girls / boys > 2:
    string = 'Нет решения'
else:
    if boys > girls:
        for i in range(1, boys + 1):
            if boys == girls:
                break
            string += 'BGB'
            boys -= 2
            girls -= 1
    else:
        for i in range(1, girls + 1):
            if girls == boys:
                break
            string += 'GBG'
            girls -= 2
            boys -= 1
    for i in range(1, boys +1):
        string += 'BG'
print(f'Ответ: {string}')