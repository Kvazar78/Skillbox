# Машина 3
#
# Вам предстоит снова немного видоизменить класс Toyota из прошлого урока. На всякий случай вот описание класса.
#
# Четыре атрибута:
#
#     цвет машины (например, красный),
#     цена (один миллион),
#     максимальная скорость (200),
#     текущая скорость (ноль).
#
# Два метода:
#
#     Отображение информации об объекте класса.
#     Метод, который позволяет устанавливать текущую скорость машины.
#
# Теперь все четыре атрибута должны инициализироваться при создании экземпляра класса (то есть передаваться в init).
# Реализуйте такое изменение класса.

class Toyota:

    def __init__(self, color, price, max_speed, cur_speed=0):
        self.color = color
        self.price = price
        self.max_speed = max_speed
        self.cur_speed = cur_speed

    def info(self):
        print('Color: {}\nPrice: {}\nMax speed: {}\nCurrent speed: {}\n'.
              format(
                self.color, self.price, self.max_speed, self.cur_speed)
        )

    def set_cur_speed(self, current_speed):
        self.cur_speed = current_speed
        print('Текущая скорость изменена на', self.cur_speed)


car1 = Toyota('blue', 150000, 220, 14)
car1.info()