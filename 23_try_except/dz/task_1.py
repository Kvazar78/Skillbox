# Имена 2
#
# Есть файл people.txt, в котором построчно хранится N имён пользователей.
#
# Напишите программу, которая берёт количество символов в каждой строке файла и в качестве ответа выводит общую сумму.
# Если в какой-либо строке меньше трёх символов (не считая литерала \n), то вызывается ошибка и сообщение, в какой именно
# строке ошибка возника. Программа при этом не завершается и обрабатывает все имена файла.
#
# Также при желании можно вывести все ошибки в отдельный файл errors.log.
count_symbol = 0
count_lines = 0

with open('people.txt', 'r') as file_to_read, open('error.log', 'a') as error_log:

        for i_line in file_to_read:
            count_lines += 1
            count_symbol += len(i_line.strip())
            try:
                if len(i_line.strip()) < 3:
                    raise BaseException(f'В строке №{count_lines} меньше трех символов!')
            except BaseException as error:
                # string_error = f'В строке №{count_lines} меньше трех символов!'
                print(str(error))
                error_log.write(str(error))
                print('Считаем дальше....')
        print('Количество символов в файле:', count_symbol)