template_dict = '''
'html': {{
    'head': {{
        'title': 'Куплю/продам {0} недорого'
    }},
    'body': {{
        'h2': 'У нас самая низкая цена на {0}',
        'div': 'Купить',
        'p': 'Продать'
    }}
}}'''


def site_gen(template_dict, name, list_sites=[]):
     list_sites.append(template_dict.format(name))
     for site in list_sites:
        print(site)


value = int(input('Сколько сайтов: '))

for i in range(1, value + 1):
    name = input('\nВведите название продукта для нового сайта: ')
    print('Сайт для', name, ':')
    site_gen(template_dict, name)