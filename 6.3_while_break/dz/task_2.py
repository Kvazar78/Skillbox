# Ваня решил попрактиковаться в программировании и выбрал своей целью
# микроволновку. Он перепрограммировал её, и теперь на дисплее ведётся
# обратный отсчёт в секундах, а в конце проигрывается забавный звук.
# Пользователь вводит число секунд seconds. Напишите программу, которая
# выводит на экран отсчёт от seconds до 0.
#
# Пример:
# Сколько секунд ждать? 5
# 5
# 4
# 3
# 2
# 1
# 0
seconds = int(input('Введите количество секунд: '))
while seconds >= 0:
    print(seconds)
    seconds -= 1