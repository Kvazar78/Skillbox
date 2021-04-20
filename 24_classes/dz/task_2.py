# Студенты
#
# Реализуйте модель с именем Student, содержащую поля: «ФИ», «Номер группы», «Успеваемость» (список из пяти элементов).

import random


class Student:
    
    def __init__(self, name):
        self.name = name
        self.group = random.randint(1, 4)
        self.lst_rating = [random.randint(2, 5) for _ in range(5)]
        self.average_score = sum(self.lst_rating) / len(self.lst_rating)
    
# Затем создайте список из десяти студентов и отсортируйте его по возрастанию среднего балла. Выведите результат на экран.
std_lst = []

for _ in range(3):
    name = input('Введи имя студента: ')
    std_lst.append(Student(name))

no_sorted_dict = {i_item.name: i_item.average_score for i_item in std_lst}
sorted_key = sorted(no_sorted_dict, key=no_sorted_dict.get)
sorted_list = [i_name for i_name in {i_key: no_sorted_dict[i_key] for i_key in sorted_key}]
print(sorted_list)
