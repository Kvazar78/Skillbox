# Напишите программу, которая находит и выводит все двузначные числа,
# которые равны утроенному произведению своих цифр. К таким относятся,
# например, 15 и 24.
for num in range(10, 100):
    product = (num // 10) * (num % 10) * 3
    if product == num:
        print(num)