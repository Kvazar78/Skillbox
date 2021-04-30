#  Координаты точки
#
# В одной из практик предыдущего модуля была задача на реализацию класса «Точка». Модернизируйте класс по следующему условию:
#  объект «Точка» на плоскости имеет координаты x и y; при создании новой точки могут передаваться пользовательские
#  значения координат, по умолчанию x = 0, y = 0.
#
# Реализуйте класс, который будет представлять эту точку, и напишите следующие методы:
#
#     Предоставление информации о точке (используйте магический метод str).
#     Геттер и сеттер для x.
#     Геттер и сеттер для y.
#
# Для сеттеров реализуйте проверку на корректность входных данных: координаты должны быть числом.
class Dot:

    __count_dot = 0

    def __init__(self, x=0, y=0):
        self.set_x(x)
        self.set_y(y)
        Dot.__count_dot += 1

    def __str__(self):
        return f'Координаты точки: x={self.get_x()}, y={self.get_y()}'

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def set_x(self, x):
        if isinstance(x, int):
            self.x = x
        else:
            raise Exception('Нужно ввести число')

    def set_y(self, y):
        if isinstance(y, int):
            self.y = y
        else:
            raise Exception('Нужно ввести число')

    def get_count(self):
        return self.__count_dot


dot_1 = Dot(4, 5)
dot_2 = Dot(6, 5)

print(dot_1)
