# У Евгения много работы, а ещё он очень забывчивый. Иногда он забывает
# о какой-нибудь важной встрече, и ему приходится выслушивать критику от
# начальства.
# Напишите для него программу-напоминалку. В самом начале программа
# спрашивает, сколько раз ему напомнить, а затем нужное количество раз
# выводит: «Вы хотели не забыть о чём-то».
count = int(input('Сколько раз тебе надо напомнить? '))
total = 0
while total < count:
    print('Вы хотели не забыть о чём-то')
    total += 1