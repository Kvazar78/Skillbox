# Пароль
#
# При регистрации на сайте помимо логина нужно ещё придумать надёжный пароль. Этот
# пароль должен состоять минимум из 8 символов, в нём должна быть хотя бы одна большая
# буква и хотя бы 3 цифры. Тогда он будет считаться надёжным.
#
# Напишите программу, которая запрашивает у пользователя пароль до тех пор, пока он
# не введёт надежный пароль. Буквы используются из латинского алфавита.
#
# Пример:
#
# Придумайте пароль: qwerty
#
# Пароль ненадёжный. Попробуйте ещё раз.
#
# Придумайте пароль: qwerty12
#
# Пароль ненадёжный. Попробуйте ещё раз.
#
# Придумайте пароль: qwerty123
#
# Пароль ненадёжный. Попробуйте ещё раз.
#
# Придумайте пароль: qWErty123
#
# Это надёжный пароль!
while True:
    passTrue = False
    password = input('\nПридумайте пароль: ')
    if len(password) >= 8 and password.isalnum():
        for sym in password:
            if sym.isupper():
                passTrue = True
    if passTrue:
        print('\nЭто надёжный пароль!')
        break
    else:
        print('\nПароль ненадёжный. Попробуйте ещё раз.')
