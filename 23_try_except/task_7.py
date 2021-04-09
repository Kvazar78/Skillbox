def line_proc(string):
    expression_list = string.strip().split()
    expression_list = [int(expression_list[i]) if i == 0 or i == 2 else expression_list[i]
                       for i in range(len(expression_list))]
    if expression_list[1] != '//' and len(expression_list[1]) > 1:
        select = input(f'Обнаружена ошибка в строке: {i_line.strip()}! \
        Хотите исправить? (да\нет) ')
        if select == 'да':
            expression_list = line_proc(input('Введите исправленную строку: '))
        else:
            raise SyntaxError(f'Т.к. строка {count_line} написана с ошибкой ({i_line}) - пропускаем...')
    return expression_list

summ = 0
count_line = 0

with open('calc.txt', 'r') as file_to_read:

    for i_line in file_to_read:
        count_line += 1
        try:
            i_line_list = line_proc(i_line)

            if len(i_line_list) != 3:
                raise Warning(f'В строке {count_line} слишком много операндов ({i_line.strip()}) \
                 - не осилим! Пропускаем...')
            else:
                if i_line_list[1] == '/' and i_line_list[2] == 0:
                    raise ZeroDivisionError(f'Делить {i_line_list[0]} на ноль неправильно ({i_line.strip()})!\
                     Пропускаем...')
                elif i_line_list[1] == '/':
                    result = i_line_list[0] / i_line_list[2]
                elif i_line_list[1] == '+':
                    result = i_line_list[0] + i_line_list[2]
                elif i_line_list[1] == '-':
                    result = i_line_list[0] - i_line_list[2]
                elif i_line_list[1] == '*':
                    result = i_line_list[0] * i_line_list[2]
                elif i_line_list[1] == '%':
                    result = i_line_list[0] % i_line_list[2]
                elif i_line_list[1] == '//':
                    result = i_line_list[0] // i_line_list[2]

                summ += result
        except (Warning, ZeroDivisionError, SyntaxError) as error:
            print(error)
print('\nСумма результатов всех выражений равна:', summ)