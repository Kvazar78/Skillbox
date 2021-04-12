# Машина 2
#
# Модернизируйте класс Toyota из прошлого урока. Атрибуты остаются такими же:
#
#     цвет машины (например, красный),
#     цена (один миллион),
#     максимальная скорость (200),
#     текущая скорость (ноль).
#
# Добавьте два метода класса:
#
#     Отображение информации об объекте класса.
#     Метод, который позволяет устанавливать текущую скорость машины.
#
# Проверьте работу этих методов.

class Toyota:
    color = 'red'
    price = 1000000
    max_speed = 200
    cur_speed = 0

    def info(self):
        print('Color: {}\nPrice: {}\nMax speed: {}\nCurrent speed: {}\n'.
              format(
                self.color, self.price, self.max_speed, self.cur_speed)
        )

    def set_cur_speed(self, current_speed):
        self.cur_speed = current_speed
        print('Текущая скорость изменена на', self.cur_speed)


car1 = Toyota()

car1.info()
car1.set_cur_speed(100)