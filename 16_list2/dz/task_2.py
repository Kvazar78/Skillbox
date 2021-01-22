def list_gen(start, end, step):
    new_list = list(range(start, end + 1, step))
    return new_list

list_fisrtClass = list_gen(160, 176, 2)
list_secondClass = list_gen(162, 180, 3)

list_common = list_fisrtClass + list_secondClass

for i in range(len(list_common) - 1):
    for num in range(len(list_common) - i - 1):
        if list_common[num] > list_common[num + 1]:
            list_common[num], list_common[num + 1] = list_common[num + 1], list_common[num]

print('Отсортированный список', list_common)