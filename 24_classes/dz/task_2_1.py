import random


class Student:

    def __init__(self, name):
        self.name = name
        self.group = random.randint(1, 4)
        self.lst_rating = [random.randint(2, 5) for _ in range(5)]
        self.average_score = sum(self.lst_rating) / len(self.lst_rating)


class Sortedstudent:
    lst_stud = []

    def add_student(self, student):
        self.lst_stud.append(student)

    def sorted_lst(self):
        no_sorted_dict = {i_item.name: i_item.average_score for i_item in self.lst_stud}
        sorted_key = sorted(no_sorted_dict, key=no_sorted_dict.get)
        sorted_list = [i_name for i_name in {i_key: no_sorted_dict[i_key] for i_key in sorted_key}]
        return sorted_list


sorted_student = Sortedstudent()

for _ in range(3):
    name = input('Enter student name: ')
    sorted_student.add_student(Student(name))

print(sorted_student.sorted_lst())