password = int(input('Введите пароль: '))

while password != 235:
    print('Неверный пароль!')
    password = int(input('Попробуйте ещё раз: '))

print('Пароль верный! Добро пожаловать.')