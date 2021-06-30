num = 7
number_attempts = 1

while True:
    number = int(input('Введите число: '))
    if number == num:
        break
    elif number > num:
        print('Число больше, чем нужно. Попробуйте ещё раз!')
    else:
        print('Число меньше, чем нужно. Попробуйте ещё раз!')
    number_attempts += 1

print('Вы угадали! Число попыток: ', number_attempts)