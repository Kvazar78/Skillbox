# Меню ресторана
#
# Один ресторан заказал вам написать приложение, которое в один клик отображало бы
# пользователю доступное меню в удобном виде. Для этого ресторан любезно предоставил
# свой сайт, откуда можно получить актуальную информацию о меню в виде идущих подряд
# названий.
#
# Напишите программу, которая выводит это меню на экран. На вход подаётся строка из
# названий блюд, разделённые символом “;”, а на выходе эти названия перечисляются
# через запятую и пробел.
#
# Пример:
#
# Доступное меню: утиное филе;фланк-стейк;банановый пирог;плов
#
# На данный момент в меню есть: утиное филе, фланк-стейк, банановый пирог, плов
# string = input('Доступное меню: ')
string = 'утиное филе;фланк-стейк;банановый пирог;плов'

print('На данный момент в меню есть: ', string.replace(';', ', '))