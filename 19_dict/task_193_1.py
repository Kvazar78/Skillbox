# Член семьи
#
# Дана структура, которая содержит описание одного из членов семьи (имя, фамилия, хобби, сколько лет и дети):
#
# family_member = {
#     "name": "Jane",
#     "surname": "Doe",
#     "hobbies": ["running", "sky diving", "singing"],
#     "age": 35,
#     "children": [
#         {
#             "name": "Alice",
#             "age": 6
#         },
#         {
#             "name": "Bob",
#             "age": 8
#         }
#     ]
# }
#
# Напишите программу, которая реализует такую структуру: имя, фамилия, хобби, количество лет и дети.
# Затем с помощью метода get и установки значения по умолчанию проверьте, есть ли ребёнок с именем Bob.
# Затем так же проверьте ребёнка с именем Rob. Если такого ребёнка нет, то получите значение Noname.
# family_member = {
#     "name": "Jane",
#     "surname": "Doe",
#     "hobbies": ["running", "sky diving", "singing"],
#     "age": 35,
#     "children": [
#         {
#             "name": "Alice",
#             "age": 6
#         },
#         {
#             "name": "Bob",
#             "age": 8
#         }
#     ]
# }
family_member = dict()
family_member['name'] = 'Jane'
family_member['surname'] = 'Doe'
family_member['hobbies'] = ['running', 'sky diving', 'singing']
family_member['age'] = 35
family_member['children'] = []

print(family_member)