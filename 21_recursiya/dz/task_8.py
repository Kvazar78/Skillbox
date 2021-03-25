def summ(data, total_list=[]):
    if isinstance(data, list):
        for i_elem in data:
            if isinstance(i_elem, list):
                summ(i_elem, total_list)
            else:
                total_list.append(i_elem)
        return total_list


nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]], [[11, 12, 13], [14, 15], [16, 17, 18]]]

input_data = [[1, 2, [3]], [1], 3]
print('Ответ', summ(nice_list))