num = int(input('Введите число: '))
count_num = 0
print(f'В числе {num} - ', end='')

while num != 0:
    num //= 10
    count_num += 1

print(f'{count_num} знаков')