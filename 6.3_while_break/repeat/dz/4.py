count_even = 0

while True:
    num = int(input('Введи число: '))
    if num == 0:
        print('Работа программы завершена...')
        break
    elif num % 2 == 0:
        count_even += 1

print(f'Количество четных чисел - {count_even}')