# Дима написал программу-вирус специально для того, чтобы проучить
# своего друга-должника, который никак не хочет возвращать скейтборд.
# Программа не даёт работать за компьютером и постоянно выводит на экран
# сообщение «Компьютер заблокирован. Вернёшь скейт — скажу код разблокировки!».
# Как только вводится правильный код, вирус удаляется. Напишите такую же
# программу, которую написал Дима.
#
# Пример:
# Компьютер заблокирован. Вернёшь скейт — скажу код разблокировки!
# Введите код: 1005
# Компьютер заблокирован. Вернёшь скейт — скажу код разблокировки!
# Введите код: 7777
# Компьютер заблокирован. Вернёшь скейт — скажу код разблокировки!
# Введите код: 0550
# Код верный, завершаю работу...
while True:
    print('Компьютер заблокирован. Вернёшь скейт — скажу код разблокировки!')
    a = input('Введите код: ')
    if a == '0550':
        print('Код верный, завершаю работу...')
        break
