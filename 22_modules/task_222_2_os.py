# Поиск файла
#
# В уроке мы написали функцию, которая ищет нужный нам файл во всех подкаталогах указанной директории.
# Однако, как мы понимаем, файлов с таким названием может быть несколько.
#
# Напишите функцию, которая принимает на вход абсолютный путь до директории и имя файла, рекурсивно проходит
# по всем вложенным файлам и папкам и выводит на экран все абсолютные пути с этим именем.
#
# Пример:
#
# Ищем в: C:/Users/Roman/PycharmProjects/Skillbox
#
# Имя файла: lesson2
#
# Найдены следующие пути:
#
# C:/Users/Roman/PycharmProjects/Skillbox\Module15\lesson2.py
# C:/Users/Roman/PycharmProjects/Skillbox\Module16\lesson2.py
# C:/Users/Roman/PycharmProjects/Skillbox\Module17\lesson2.py
# C:/Users/Roman/PycharmProjects/Skillbox\Module18\lesson2.py
# C:/Users/Roman/PycharmProjects/Skillbox\Module19\lesson2.py
# C:/Users/Roman/PycharmProjects/Skillbox\Module20\lesson2.py
# C:/Users/Roman/PycharmProjects/Skillbox\Module21\lesson2.py
# C:/Users/Roman/PycharmProjects/Skillbox\Module22\lesson2.py
import os

def find_file(path_to_file, file_name):
    for i_elem in os.listdir(path_to_file):
        path = os.path.join(path_to_file, i_elem)
        if file_name == i_elem:
            print('Файл найден в:', path)
        if os.path.isdir(path):
            find_file(path, file_name)


path_to_file = input('Ищем в: ')
file_name = input('Имя файла: ')
print()

find_file(path_to_file, file_name)