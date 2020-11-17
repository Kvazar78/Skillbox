# Усложнение: напишите программу так, чтобы офицер начинал спрашивать
# не с последнего солдата в шеренге, а с четвертого с конца. Если
# солдат в шеренге слишком мало, офицер не спрашивает никого
totalSoldiers = int(input('Сколько солдат в шеренге? '))
totalRules = int(input('Сколько правил в уставе? '))
totalPushUp = 0
if totalSoldiers < 4:
    print('Что-то вас мало!')
else:
    for soldier in range(totalSoldiers - 4, 0, -4):
        print(f'Номер солдата в шеренге {soldier}')
        soldierRules = int(input('Солдат, сколько правил в уставе? '))
        if totalRules != soldierRules:
            pushUp = 10 * soldier
            print(f'Упал-отжался {pushUp} раз!')
            totalPushUp += pushUp
print(f'Общее количство отжиманий составило - {totalPushUp}')