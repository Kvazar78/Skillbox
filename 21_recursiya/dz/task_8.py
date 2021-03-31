def summ(data, total_list=None):
    total_list = total_list if total_list else []
    if isinstance(data, list):
        for i_elem in data:
            if isinstance(i_elem, list):
                summ(i_elem, total_list)
            else:
                total_list.append(i_elem)
    return total_list


def summ2(data):

    total_list = [summ2(i_elem) if isinstance(i_elem, list) else i_elem for i_elem in data]
    tot_list = total_list[:]
    return tot_list


nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]], [[11, 12, 13], [14, 15], [16, 17, 18]]]

input_data = [[1, 2, [3]], [1], 3]
print('Ответ', summ2(nice_list))