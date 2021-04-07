# Логирование
#
# Возможно, вы замечали, что некоторые программы не просто выдают ошибку и закрываются, но и записывают эту ошибку в файл.
# Таким образом проще сформировать отчёт об ошибках, а значит, программисту будет проще их исправить.
# Это называется логированием ошибок.
#
# Дан файл words.txt, в котором построчно записаны слова. Необходимо определить количество слов, из которых можно получить
# палиндром (привет предыдущим модулям). Если в строке встречается число,
# то программа выдаёт ошибку ValueError и записывает эту ошибку в файл errors.log
def palindrome(string):
    ood_count = 0
    sym_dict = dict()
    palindrome_flag = True

    for sym in string:
        if sym.isdigit():
            raise ValueError(f'В слове {string} есть цифра!')
        if sym in sym_dict:
            sym_dict[sym] += 1
        else:
            sym_dict[sym] = 1
    for item in sym_dict.values():
        if item % 2 == 1:
            ood_count += 1
            if ood_count > 1:
                palindrome_flag = False
                break

    return palindrome_flag


count_palindrome = 0
file_to_read = open('words.txt', 'r')
error_file = open('errors.log', 'w')

for i_line in file_to_read:
    try:
        if palindrome(i_line.strip()):
            count_palindrome += 1
    except ValueError:
        error_file.write('В слове попалась цифра.')
        error_file.close()
    # finally:
    #      file_to_read.close()
print(count_palindrome)