# Окружность
#
# На координатной плоскости рисуются окружности, у каждой окружности следующие параметры: координаты X и Y центра окружности и значение R ― это радиус окружности. По умолчанию центр находится в (0, 0), а радиус равен 1.
#
# Реализуйте класс «Окружность», который инициализируется по этим параметрам. Круг также может:
#
#     Находить и возвращать свою площадь.
#     Находить и возвращать свой периметр.
#     Увеличиваться в K раз.
#     Определять, пересекается ли он с другой окружностью.
from math import pi, sqrt


class Circle:

    def __init__(self, x=0, y=0, r=1):
        self.x = x
        self.y = y
        self.r = r

    def _area(self):
        return pi * self.r ** 2

    def area_info(self):
        return f'Площадь круга равна: {round(self._area(), 2)}'

    def _perimeter(self):
        return 2 * pi * self.r

    def perimeter_info(self):
        return f'Периметр круга равен: {round(self._perimeter(), 2)}'

    def increase(self, k=1):
        area_k = self._area() * k
        r_k = sqrt(self._area() * 2 / pi)
        print(f'Площадь круга была {round(self._area(), 2)}, увеличившись в {k} раз станет - {round(area_k, 2)}\n \
Внимание: изменился радиус {round(r_k, 2)}')
        self.r = r_k

    def crossing(self):
        croos_flag = False
        d = sqrt(abs(cir1.x - cir2.x) ** 2 + abs(cir1.y - cir2.y) ** 2)
        if d <= cir1.r + cir2.r:
            croos_flag = True

        return croos_flag


circle_list = []

for i in range(1, 3):
    x = int(input(f'Введите Х координату {i} окружности: '))
    y = int(input(f'Введите Y координату {i} окружности: '))
    r = int(input(f'Введите радиус {i} окружности: '))
    circle_list.append(Circle(x, y, r))

cir1, cir2 = circle_list

print(cir1.perimeter_info())
print(cir2.area_info())


if cir1.crossing():
    print('Окружности пересекаются')
else:
    print('Окружности не пересекаются')


