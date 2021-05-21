# Кастомные исключения
#
# Исключения в Python также являются классами, и все они берут свои истоки от самого главного класса — Exception.
# И для создания своего собственного класса ошибки достаточно написать его дочерний класс. Например:
#
# class MyOwnException(Exception):
#     pass
#
# raise MyOwnException('Это моя ошибка!')
#
# Причём содержимое объекта исключения чаще всего так и оставляют (просто pass), чтобы не сломать автоматические обработчики исключений.
#
# Напишите программу, которая считывает из файла numbers.txt пары чисел, делит первое число на второе и выводит ответ на экран.
# Если первое число меньше второго, то программа выдаёт исключение DivisionError (нельзя делить большее на меньшее).
#
# Дополнительно, с помощью try except, можно обработать исключение на своё усмотрение.
from random import randint


class MyException(Exception):
    pass


def check(string):
    string_lst = string.split()
    if string_lst[0] < string_lst[1]:
        raise MyException(f'{string_lst[0]} меньше {string_lst[1]} - делить не будем')
    else:
        print(string_lst[0] / string_lst[1])


with open('numbers.txt', 'a') as file_to_write:
    for _ in range(5):
        string = str(randint(0, 101)) + ' ' + str(randint(0, 101)) + '\n'
        file_to_write.write(string)

with open('numbers.txt', 'r') as file_to_read:
    for i_line in file_to_read:
        print('обрабатывается строка:', i_line)
        check(i_line)

