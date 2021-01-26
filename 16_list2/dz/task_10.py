def comparison(seq, seq_r, i_s):
    result = False
    i_sr = 0
    for num in range(i_s, len(sequence)):
        if seq[num] ==seq_r[i_sr]:
            i_sr += 1
            result = True
        else:
            result = False
            break
    return result


count_num = int(input('Кол-во чисел: '))
sequence = []
sequence_reverse = []

for _ in range(count_num):
    sequence.append(int(input('Число: ')))

for i in range(len(sequence)- 1, -1, -1):
    sequence_reverse.append(sequence[i])

print('\nПоследовательность:', end=' ')
for i in sequence:
    print(i, end=' ')
print()

if len(sequence) == 1:
    print('\nОдно число?')
else:
    iter = 0
    for i in range(len(sequence)):
        if comparison(sequence, sequence_reverse, i):
            break
        else:
            iter += 1
    print('\nНужно приписать чисел:', iter)
    print('Сами числа:', end=' ')
    for i in range((iter* (-1)), 0):
        print(sequence_reverse[i], end=' ')