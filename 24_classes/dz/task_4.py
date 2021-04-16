class Parents:
    list_kids = []

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.list_kids.append(Children)

    def about_me(self):
        return f'Привет! Меня зовут {self.name}, мне {self.age} лет.'

    def calm_down(self):

    def feed(self):



class Children:
    calmness = {1: 'адекват', 0: 'неадекват'}
    hunger = {1: 'сытый', 0: 'голодный'}

    def __init__(self, chld_name, chld_age, chld_calmness, chld_hunger):
        self.chld_name = chld_name
        self.chld_age = chld_age
        self.chld_calmness = self.calmness[chld_calmness]
        self.chld_hunger = self.hunger[chld_hunger]




father_name = input('Vvedi imya mother: ')
mother_name = input('Vvedi imya father: ')
value_child = int(input('Kolichestvo detey: '))
for _ in range(value_child):
