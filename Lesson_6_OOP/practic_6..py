class Auto:
    # атрибуты класса
    auto_name = 'Lexus'
    auto_model = 'RX 350L'
    auto_year = '2020'

    # Метод класса, все взаимодействие проходит через self
    # И self является связующим звеном объекта (auto_1) с методом(т.е. с функцией)
    def on_start(self):
        print('Go')

    # Метод класса
    def on_stop(self):
        print('Stop!')

# auto_1---> является объектом класса ---> Auto()
# Теперь auto_1, как объект может использовать атрибуты и методы класса Auto()
auto_1 = Auto()
print(auto_1.auto_name)
auto_1.on_start()
auto_1.on_stop()

auto_2 = Auto('Mazda', '3', '2019')
print(auto_2.auto_name)
auto_2.on_stop()