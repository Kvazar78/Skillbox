#  Компания
#
# Реализуйте иерархию классов, описывающих служащих в компании. На самом верху иерархии — класс Person, который описывает
#  человека именем, фамилией и возрастом. Все атрибуты этого класса являются приватными.
#
# Далее идёт класс Employee и производные от него классы Manager, Agent и Worker.
#
# Класс «Работник» должен иметь метод расчёта заработной платы, переопределённый в каждом из производных классов. Заработная
#  плата Manager постоянна и равна 13000, заработная плата Agent определяется как оклад 5000 + 5% объёма продаж, который
#  хранится в специальном поле класса Agent, и заработная плата Worker определяется как 100 * число отработанных часов,
#  которое также хранится в отдельном поле.
#
# В основной программе создайте список из девяти объектов: первые три — Manager, следующие три — Agent и последние три — Worker.
#  Выведите на экран величину заработной платы всех девяти служащих.
class Person:

    def __init__(self, f_name, s_name, age):
        self.__firstname = f_name
        self.__surname = s_name
        self.__age = age

    def get_firstname(self):
        return self.__firstname

    def get_surname(self):
        return self.__surname


class Employee(Person):

    def __init__(self, f_name, s_name, age):
        super().__init__(f_name, s_name, age)

    def calc_salary(self):
        pass

    def __str__(self):
        return '{name} {surname} - зарплата {salary} рублей'.format(
            name=self.get_firstname(),
            surname=self.get_surname(),
            salary=self.calc_salary()
        )


class Manager(Employee):

    def __init__(self, f_name, s_name, age):
        super().__init__(f_name, s_name, age)

    def calc_salary(self):
        return 13000


class Agent(Employee):

    def __init__(self, f_name, s_name, age, vol_sales):
        super().__init__(f_name, s_name, age)
        self.__vol_sales = vol_sales

    def get_vol_sales(self):
        return self.__vol_sales

    def calc_salary(self):
        salary = 5000 + self.get_vol_sales() * 0.05
        return salary


class Worker(Employee):

    def __init__(self, f_name, s_name, age, hours_work):
        super().__init__(f_name, s_name, age)
        self.__hours = hours_work

    def get_hours(self):
        return self.__hours

    def calc_salary(self):
        salary = 100 * self.get_hours()
        return salary


man1 = Manager('Вова', 'Петров', 24)
man2 = Manager('Вася', 'Иванов', 25)
man3 = Manager('Рома', 'Сидоров', 27)
ag1 = Agent('Илья', 'Смирнов', 24, 56000)
ag2 = Agent('Александр', 'Раков', 25, 63500)
ag3 = Agent('Светлана', 'Козлова', 23, 80000)
wk1 = Worker('Петр', 'Рукожопов', 37, 300)
wk2 = Worker('Игорь', 'Зачетный', 43, 215)
wk3 = Worker('Олег', 'Джамшутов', 39, 400)

print(man1)
company = [man1, man2, man3, ag1, ag2, ag3, wk1, wk2, wk3]

for i_elem in company:
    print(i_elem)