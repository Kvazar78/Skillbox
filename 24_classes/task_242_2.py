# Однотипные объекты
#
# В офис заказали небольшую партию из четырёх мониторов и трёх наушников. У монитора есть четыре характеристики:
# название производителя, матрица, разрешение и частота обновления экрана. Все четыре монитора отличаются только частотой.
#
# У наушников три характеристики: название производителя, чувствительность и наличие микрофона.
# Отличие только в наличии микрофона.
#
# Для внесения в базу программист начал писать такой код:

# monitor_name_1 = 'Samsung'
# monitor_matrix_1 = 'VA'
# monitor_res_1 = 'WQHD'
# monitor_freq_1 = 60
# monitor_name_2 = 'Samsung'
# monitor_matrix_2 = 'VA'
# monitor_res_2 = 'WQHD'
# monitor_freq_2 = 144
# monitor_name_3 = 'Samsung'
# monitor_matrix_3 = 'VA'
# monitor_res_3 = 'WQHD'
# monitor_freq_3 = 70
# monitor_name_4 = 'Samsung'
# monitor_matrix_4 = 'VA'
# monitor_res_4 = 'WQHD'
# monitor_freq_4 = 60
#
# headphones_name_1 = 'Sony'
# headphones_sensitivity_1 = 108
# headphones_micro_1 = False
# headphones_name_2 = 'Sony'
# headphones_sensitivity_2 = 108
# headphones_micro_2 = True
# headphones_name_3 = 'Sony'
# headphones_sensitivity_3 = 108
# headphones_micro_3 = True

# Поправьте программиста: перепишите код, используя классы и экземпляры классов.

class Monitor:
    monitor_name = 'Samsung'
    monitor_matrix = 'VA'
    monitor_res = 'WQHD'
    monitor_freq = 60

class Headphones:
    headphones_name = 'Sony'
    headphones_sensitivity = 108
    headphones_micro = True


monitor1, monitor2, monitor3, monitor4 = Monitor(), Monitor(), Monitor(), Monitor()
monitor2.monitor_freq = 144
monitor3.monitor_freq = 70
monitor4.monitor_freq = 60

headphones1, headphones2, headphones3 = Headphones(), Headphones(), Headphones()
headphones1.headphones_micro = False
