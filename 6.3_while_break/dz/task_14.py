# Поменяйте мальчика и компьютер из прошлой задачи местами. Теперь
# мальчик загадывает число между 1 и 100 (включительно). Компьютер
# может спросить у мальчика: «Твое число равно, меньше или больше,
# чем число N?», где N — число, которое хочет проверить компьютер.
# Мальчик отвечает одним из трёх чисел: 1 — равно, 2 — больше, 3 — меньше.
#
# Напишите программу, которая с помощью цепочки таких вопросов и ответов
# мальчика угадывает число.
#
# Дополнительно: сделайте так, чтобы можно было гарантированно угадать
# число за семь попыток.
left = 1
right = 100
number = int(input(f'Введите число от {left} до {right}: '))
n = 50
while True:
    qst = input(f'Твое число равно, меньше или больше, чем число {n}? 1(равно)/2(больше)/3(меньше) ')
    if qst == '2':  # больше
        left = n + 1
        n = (left + right) // 2
    elif qst == '3': # меньше
        right = n - 1
        n = (left + right) // 2
    else:
        print(f'Ты загадал число {n}')
        break
