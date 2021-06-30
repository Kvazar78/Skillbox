temp = int(input('Сколько градусов не улице? '))
distance = 0

while temp > 15:
    distance += 20
    temp -= 2
    if temp < 15:
        print('Закончили, холодно!')
        break
    distance += 10

print(f'Пройдена дистанция {distance} метров')