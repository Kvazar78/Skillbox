# Сервер
#
# У вас есть данные о сервере, которые хранятся в виде вот такого словаря:

server_data = {
    "server": {
        "host": "127.0.0.1",
        "port": "10"
    },
    "configuration": {
        "access": "true",
        "login": "Ivan",
        "password": "qwerty"
    }
}

# Напишите программу, которая выводит для пользователя эти данные так же красиво и понятно,
# как они представлены в словаре.
#
# Результат работы программы:
#
# server:
#     host: 127.0.0.1
#     port: 10
# configuration:
#     access: true
#     login: Ivan
#     password: qwerty
for item in server_data.keys():
    print(item,':')
    for i_key, i_val in server_data[item].items():
        print('\t{key} : {val}'.format(
            key=i_key,
            val=i_val
        ))
