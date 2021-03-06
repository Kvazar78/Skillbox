# Реализуйте программу — чат, в котором могут участвовать сразу несколько человек, то есть программа может работать
# одновременно для нескольких пользователей. При запуске запрашивается имя пользователя. После этого он выбирает одно из действий:
#
#     Посмотреть текущий текст чата.
#     Отправить сообщение (затем вводит сообщение).
#
# Действия запрашиваются бесконечно.
#
# Примечание: для решения задачи вам будет достаточно текущих знаний, нужно лишь проявить немного фантазии и хитрости.
# Не нужно лезть в дебри работы с сетями, создания GUI-приложений и прочих штук. (Но если очень хочется, то останавливать
# вас никто не будет!)

while True:
    name = input('Введите имя: ')
    select = int(input('Выберите действие: 1 - прочитать историю, 2 - написать сообщение: '))
    try:
        if select == 1:
            print('\nИстория сообщений:')
            with open('chat.txt', 'r', encoding='utf-8') as chat:
                for i_line in chat:
                    print('\t', i_line.strip())
        elif select == 2:
            with open('chat.txt', 'a', encoding='utf-8') as chat:
                string = input('\nВведите сообщение: ')
                chat.write(f'{name}: ' + string + '\n')
        else:
            raise ValueError('Требуется ввести 1 или 2!')
    except ValueError as error:
        print(error)