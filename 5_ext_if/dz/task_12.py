# Предприимчивый Василий хочет начать производство платков,
# но не хочет искать отдельно помещение и нужное количество станков.
# Он хочет найти сразу готовый вариант.
#
# Напишите программу, которая принимает на вход два числа:
# количество станков и площадь помещения. Ему нужны помещения не менее 100
# квадратных метров, в которых расположено хотя бы пять станков.
# Выведите сообщение: «Не подходит. Нужно искать дальше» или «Всё отлично,
# это наш вариант!».
kolvo_st = int(input('Количество станков: '))
area = int(input('Площадь помещения: '))
if area >= 100 and kolvo_st >= 5:
  print('Всё отлично, это наш вариант!')
else:
  print('Не подходит. Нужно искать дальше')