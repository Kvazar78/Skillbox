# У нас есть квадратный конверт размера 12х12 сантиметров и письмо на квадратном листе бумаги,
# которое не помещается в конверт. Напишите программу, которая подскажет сколько раз нужно сложить письмо
# пополам, чтобы оно поместилось в конверт. Размеры письма вводятся с клавиатуры.
a = int(input('Введите длину стороны листа письма: '))
a_convert = 12
count = 0
while True:
    if a_convert ** 2 < a ** 2:
        count += 2
        a /= 2
    else:
        break
print(f'Лист нужно сложить {count} раз')