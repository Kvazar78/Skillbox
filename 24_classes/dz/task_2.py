# Студенты
#
# Реализуйте модель с именем Student, содержащую поля: «ФИ», «Номер группы», «Успеваемость» (список из пяти элементов).
# Затем создайте список из десяти студентов и отсортируйте его по возрастанию среднего балла. Выведите результат на экран.
import random


class Student:

    def __init__(self, name, num_group):
        self.name = name
        self.group = num_group
        self.lst_rating = [random.randint(2, 5) for _ in range(5)]



class Sorting:

    def __init__(self):
        self.rating_dict = {for i_name in Student.lst_rating}