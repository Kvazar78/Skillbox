import os

def write_file(path_start):
    for i_elem in os.listdir(path_start):
        path = os.path.join(path_start, i_elem)
        if os.path.isdir(path):
            write_file(path)
        else:
            file_read = open(path)
            data = file_read.read()
            scripts.write(data)
            file_read.close()
            razdel = '\n' * 2 + '*' * 40 + '\n' * 2
            scripts.write(razdel)


start_path = input('Откуда начнем сбор: ')
scripts = open('scripts.txt', 'a')

path = os.path.abspath(start_path)

write_file(path)

scripts.close()