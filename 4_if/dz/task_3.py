# Стоматолог посоветовал Маше использовать зубную нить каждый чётный день.
# Чтобы не забывать, Маша написала скрипт на Python, который в случае чего
# напоминает ей про совет стоматолога.
# Напишите программу, которая проверяет, чётное ли число ввёл пользователь,
# и выводит соответствующее сообщение. Подсказка: для проверки чётности
# используйте оператор %.
day = int(input('Введите число: '))
if day % 2 == 0:
  print('Сегодня четный день - пора использовать зубную нить')
