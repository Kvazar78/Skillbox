def towers(n, x=1, y=3):
    if n == 1:
        move(1, x, y)
    else:
        tmp_dildo = 6 - x - y
        towers(n - 1, x, tmp_dildo)
        move(n, x, y)
        towers(n - 1, tmp_dildo, y)


def move(num, x, y):
    print(f'Переложить диск {num} со стержня номер {x} на стержень номер {y}')


n = int(input('Введите количество дисков: '))
towers(n)
