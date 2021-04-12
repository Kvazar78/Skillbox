def line_proc(string_list):
    if len(string_list) != 3:
        raise ValueError
    elif not string_list[0].isalpha():
        raise NameError
    elif '@' not in string_list[1] or '.' not in string_list[1]:
        raise SyntaxError
    elif not string_list[2].isdigit() or 10 < int(string_list[2]) > 99:
        raise ValueError


def write_error(string, error):
    bad_log.write(string.strip() + ' - ' + error + '\n')


with open('registrations.txt', 'r') as file_data, \
        open('registrations_good.log', 'a') as good_log, \
        open('registrations_bad.log', 'a') as bad_log:

    for i_line in file_data:
        try:
            line_proc(i_line.strip().split())

        except ValueError:
            error = 'НЕ присутствуют все три поля!'
            write_error(i_line, error)
        except NameError:
            error = 'Поле имени содержит НЕ только буквы:'
            write_error(i_line, error)
        except SyntaxError:
            error = 'Поле «Имейл» НЕ содержит @ и .(точку)'
            write_error(i_line, error)
        else:
            good_log.write(i_line)

    print('Файл обработан')