# У нас есть квадратный конверт размера 12х12 сантиметров и письмо на квадратном листе бумаги,
# которое не помещается в конверт. Напишите программу, которая подскажет сколько раз нужно сложить письмо
# пополам, чтобы оно поместилось в конверт. Размеры письма вводятся с клавиатуры.
a = int(input('Введите длину стороны листа письма: '))
a_convert = 12
count = 0

for n in range(a_convert, a, -12):
    if a_convert >= a:
        break
    else:
        a /= 2
        count += 2

print(f'Лист нужно сложить {count} раз')
