temlate_dict = {
    'html': {
        'head': {
            'title': 'Куплю/продам {0} недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на {0}',
            'div': 'Купить',
            'p': 'Продать'
        }
    }
}

for section in temlate_dict:
    if isinstance(section, dict):
        for item in section:
            print(item)