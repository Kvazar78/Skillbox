num = 50
count_attempts = 1
left = 0
right = 100

while True:
    sel = int(input(f'Твоё число равно, меньше или больше, чем число {num}? 1 — равно, 2 — больше, 3 — меньше '))
    if sel == 1:
        break
    elif sel == 2:
        left = num
        num += int((right - left) / 2) + left
    else:
        right = num
        num -= int((right - left) / 2) + left
    count_attempts += 1

print(f'Потребовалось {count_attempts} попыток')