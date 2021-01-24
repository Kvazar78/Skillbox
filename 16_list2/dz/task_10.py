count_num = int(input('Кол-во чисел: '))
sequence = []
sequence_reverse = []

for _ in range(count_num):
    sequence.append(int(input('Число: ')))

for i in range(len(sequence)- 1, -1, -1):
    sequence_reverse.append(sequence[i])

for i in range(len(sequence)- 1, -1, -1):
    if i == 0:
        break
    elif sequence[i] != sequence[i - 1]:
        sequence_reverse.remove(sequence_reverse[0])
        break
    elif sequence[i] == sequence_reverse[0]:
        sequence_reverse.remove(sequence_reverse[0])

print('\nПоследовательность:', sequence)
print('Нужно приписать чисел:',len(sequence_reverse))
print('Сами числа:', end=' ')
for i in sequence_reverse:
    print(i, end=' ')

