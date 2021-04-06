# Поиск файла 2
#
# Как мы помним, скрипты — это просто куча строк текста, хоть они и понятны только программисту.
# Таким образом, с ними можно работать точно так же, как и с обычными текстовыми файлами.
#
# Используя функцию поиска файла из предыдущего урока, реализуйте программу, которая находит
# внутри указанного пути все файлы с искомым названием и выводит на экран текст одного из них
# (выбор можно сгенерировать случайно).
#
# Подсказка: можно использовать, например, список для сохранения найденного пути.
import os
import random


def find_file(path_to_file, file_name, lst_path=None):
    lst_path = [] if lst_path is None else lst_path
    for i_elem in os.listdir(path_to_file):
        path = os.path.join(path_to_file, i_elem)
        if i_elem in file_name:
            print('Файл найден в:', path)
            lst_path.append(path)
        if os.path.isdir(path):
            find_file(path, file_name, lst_path)

    return lst_path


# path_to_file = input('Ищем в: ')
path_to_file = '/home/kvazar/work/'
# file_name = input('Имя файла: ')
file_name = 'group_1.txt'
# lst_path = []
print()

list_files = find_file(path_to_file, file_name)

print(list_files)
open_file = open(list_files[random.randint(0, len(list_files) - 1)], 'r')
for i_line in open_file:
    print(i_line)

open_file.close()