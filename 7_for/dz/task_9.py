# В классе N человек. Каждый из них получил за урок по информатике оценку:
# 3, 4 или 5, двоек сегодня не было. Напишите программу, которая получает
# список оценок - N чисел - и выводит на экран сообщение о том, кого сегодня
# больше: отличников, хорошистов или троечников.
total_students = int(input('Введите количество учеников: '))
c_grade = 0
b_grade = 0
a_grade = 0
for student in range(1, total_students +1):
    rating = int(input(f'Введите оценку {student} ученика: '))
    if rating == 5:
        a_grade += 1
    elif rating == 4:
        b_grade += 1
    else:
        c_grade += 1
print(f'Отличников на сегодня {a_grade} человек')
print(f'Хорошистов на сегодня {b_grade} человек')
print(f'Троечников на сегодня {c_grade} человек')