hours = int(input('Введите время в часах: '))
if (hours < 8) or (10 <= hours < 12) or (14 <= hours <15) or (18 <= hours < 20) or (hours >= 22):
  print('Получить посылку нельзя')
else:
  print('Получить посылку можно')