file = open('/home/kvazar/work/task/group_1.txt', 'r')

summa = 0
diff_list = []
compose = 0

for i_line in file:
    info = i_line.split()
    summa += int(info[2])
    diff_list.append(int(info[2]))

diff_list.sort(reverse=True)
diff = diff_list[0]
for i in range(1, len(diff_list)):
    diff -= diff_list[i]

file_2 = open('/home/kvazar/work/task/group_2.txt', 'r')
compose_list = []

for i_line in file_2:
    info = i_line.split()
    compose_list.append(int(info[2]))

compose = compose_list[0]
for i_elem in compose_list:
    compose *= i_elem

print(compose_list)

print('Сумма очков первой группы:', summa)
print('Разница очков первой группы:', diff)
print('Произведение очков второй группы:', compose)
file.close()
file_2.close()