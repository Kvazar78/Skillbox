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
from random import randint


class KillError(Exception):
    pass


class DrunkError(Exception):
    pass


class CarCrashError(Exception):
    pass


class GluttonyError(Exception):
    pass


class DepressionError(Exception):
    pass


def one_day(except_list):
    fortuna = randint(1, 10)
    if fortuna == 10:
        with open('karma.log', 'a') as karma_log:
            karma_log.write()
    else:
        return randint(1, 7)

except_list = [KillError, DrunkError, CarCrashError, GluttonyError, DepressionError]
karma_point = 0

with open('karma.log', 'a') as karma_log:
    while karma_point < 500:

