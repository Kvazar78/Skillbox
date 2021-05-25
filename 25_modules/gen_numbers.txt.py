from random import randint

with open('numbers.txt', 'a') as file_to_write:
    for _ in range(15):
        string = str(randint(0, 99)) + ' ' + str(randint(0, 99)) + '\n'
        file_to_write.write(string)

