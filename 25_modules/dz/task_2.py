# Карма
#
# Один буддист-программист решил создать свой симулятор жизни, в котором нужно набрать 500 очков кармы (это константа), чтобы достичь просветления.
#
# Каждый день вызывается специальная функция one_day(), которая возвращает количество кармы от 1 до 7 и может с вероятностью
# 1 к 10 выкинуть одно из исключений:
#
#     KillError
#     DrunkError
#     CarCrashError
#     GluttonyError
#     DepressionError
#
# Напишите такую программу. Функцию оберните в бесконечный цикл, выход из которого возможен только при накоплении кармы до уровня константы.
# Исключения обработайте и запишите в отдельный лог karma.log.
import random


class KillError(Exception):

    def __str__(self):
        return 'Ой убили...'
    # pass


class DrunkError(Exception):

    def __str__(self):
        return 'Ой... напился...'
    # pass


class CarCrashError(Exception):

    def __str__(self):
        return 'Упс... авария'

    # pass


class GluttonyError(Exception):

    def __str__(self):
        return 'Нажрался...'
    # pass


class DepressionError(Exception):

    def __str__(self):
        return 'Плохо мне... плохо...'
    # pass


def one_day(except_list):
    fortuna = random.randint(1, 10)
    if fortuna == 10:
        with open('karma.log', 'a') as karma_log:
            string = str(random.choice(except_list)) + '\n'
            karma_log.write(string)
        return 0
    else:
        return random.randint(1, 7)

except_list = [KillError, DrunkError, CarCrashError, GluttonyError, DepressionError]
karma_point = 0

with open('karma.log', 'a') as karma_log:
    while karma_point < 500:
        karma_point += one_day(except_list)

print(f'набралось {karma_point} очков кармы')
