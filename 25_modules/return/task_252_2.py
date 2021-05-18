# Человек
#
# Реализуйте класс «Человек», который инициализируется именем (имя должно состоять только из букв) и возрастом (должен быть
# в диапазоне от 0 до 100), а внутри класса считается общее количество инициализированных объектов. Реализуйте сокрытие данных
# для всех атрибутов (как статических, так и динамических), а для изменения и получения данных объекта напишите специальные геттеры и сеттеры.
#
# При тестировании класса измените приватный атрибут (например, возраст) двумя способами: сеттером и «крайне не рекомендуемым»,
# который был показан в уроке.
class Person:
    __count_person = 0

    def __init__(self, name, age):
        self.set_name(name)
        self.set_age(age)
        self.__count_person += 1

    def set_name(self, name):
        if name.isalpha():
            self.__name = name
        else:
            raise Exception(f'В имени {name} присутствуют посторонние символы!')

    def set_age(self, age):
        if age in range(0, 100):
            self.__age = age
        else:
            raise Exception('Введен не правильный возраст!')

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def __str__(self):
        return f'Возраст {self.get_name()} составляет {self.get_age()} лет.'


tom = Person('Mikha1il', 42)

print(tom)