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


def find_file(path_to_file, file_name, lst_path=None):
    lst_path = lst_path if lst_path else []
    for i_elem in os.listdir(path_to_file):
        path = os.path.join(path_to_file, i_elem)
        if file_name == i_elem:
            print('Файл найден в:', path)
            # lst_path.append(path)
        if os.path.isdir(path):
            find_file(path, file_name, lst_path)
            lst_path.append(path)
    # return lst_path


path_to_file = input('Ищем в: ')
file_name = input('Имя файла: ')
print()

list_files = find_file(path_to_file, file_name)
print(list_files)