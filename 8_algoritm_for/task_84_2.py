# У офицера сегодня очень плохое настроение: он выстроил всех солдат
# в шеренгу и, начиная с конца, начал спрашивать у каждого четвёртого
# солдата сколько правил прописано в воинском уставе. Количество правил
# с каждым разом меняется. Если солдат ответил неверно, то применяется
# закон под названием “упал-отжался”. Количество отжиманий считается как
# 10 умножить на порядковый номер солдата в шеренге. Напишите программу,
# которая посчитает сколько в сумме получится таких отжиманий.
#
# Усложнение: напишите программу так, чтобы офицер начинал спрашивать
# не с последнего солдата в шеренге, а с четвертого с конца. Если
# солдат в шеренге слишком мало, офицер не спрашивает никого
totalSoldiers = int(input('Сколько солдат в шеренге? '))
totalRules = int(input('Сколько правил в уставе? '))
totalPushUp = 0
for soldier in range(totalSoldiers, 0, -4):
    soldierRules = int(input('Солдат, сколько правил в уставе? '))
    if totalRules != soldierRules:
        pushUp = 10 * soldier
        print(f'Упал-отжался {pushUp} раз!')
        totalPushUp += pushUp
print(f'Общее количство отжиманий составило - {totalPushUp}')