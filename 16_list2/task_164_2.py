count_spman = int(input('Кол-во участников: '))
count_inCommand = int(input('Кол-во человек в команде: '))
list_command = []
num = 1

if count_spman % count_inCommand == 0:
    for _ in range(count_spman // count_inCommand):
        list_command.append(list(range(num, num + 3)))
        num += 3
    print('Общий список команд:', list_command)
else:
    print(f'{count_spman} участников невозможно поделить на команды по {count_inCommand} человек!')