# Мы разрабатываем пошаговую игру по мотивам боевика. Игрок -
# главный герой и должен обезвредить бомбу, которая взорвётся через N
# секунд. Программа спрашивает пользователя хочет ли он обезвредить бомбу
# сейчас. Если ответ “0” (то есть “нет”), то счетчик бомбы уменьшается.
# Если он достиг нуля, то программа выдаёт сообщение “Бомба взорвалась”,
# а если не достиг, то программа вновь переспрашивает, не хочет ли игрок
# обезвредить бомбу, и сообщает, сколько времени осталось до взрыва..
# Если ответ “да”, то программа выводит на экран сообщение о том, что
# бомба обезврежена и сколько секунд оставалось до взрыва. Используйте цикл for.
timer = int(input('Сколько секунд до взрыва? '))
for t in range(timer, -1, -1):
    off_bomb = int(input('Хотел бы обезвредить бомбу сейчас? 0(нет)/1(да) - '))
    if off_bomb:
        print(f'Бомба обезврежена. До взрыва оставалось {t} секунд...')
        break
    else:
        print(f'До взрыва осталось {t} секунд!')
if off_bomb == False:
    print('Бомба взорвалась!')
