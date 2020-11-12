# У Саши в грузовике стоит суперсовременный цифровой циферблат для
# подсчёта пробега, но он постоянно глючит и сбрасывается. Саша заметил
# закономерность: каждый раз, когда сумма цифр на циферблате превышает
# число текущего дня, циферблат сбрасывается.
# Напишите программу, которая получает на вход от пользователя два числа:
# пробег и номер дня (первое — обязательно трёхзначное), затем находит
# сумму цифр первого числа и, если эта сумма больше второго числа, выводит
# сообщение: «Сброс», — и сбрасывает пробег до нуля. В противном случае
# выводится: «Сегодня не сломался». В конце также выводится сам пробег.
mileage = int(input('Пробег: '))
num_day = int(input('Номер дня: '))
summ_num_mileage = (mileage // 100) + (mileage // 10 % 10) + mileage % 10
if summ_num_mileage > num_day:
  print('Сброс')
  mileage = 0
else:
  print('Сегодня не сломался')
print(f'Пробег {mileage}')