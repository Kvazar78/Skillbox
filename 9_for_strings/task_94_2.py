# У Никиты дома есть много компьютеров, которые он хочет подключить
# к одной локальной сети. Для этого ему нужно сгенерировать айпи адрес
# для каждого компьютера. Айпи адрес записывается как 4 числа, которые
# отделяются точкой. Не долго думая, для генерации Никита решил использовать
# арифметическую прогрессию, причём первые 3 числа в адресе - это члены
# прогрессии, а последнее число - это её сумма.
#
# Напишите программу, где пользователь вводит первый член прогрессии
# и разность и в результате получает айпи-адрес.
num = int(input('Введи число: '))
summ = 0
print('\nIp-адрес:', end = ' ')
for i in range(3):
    print(num, end = '.')
    summ += num
    num += 1
print(summ)