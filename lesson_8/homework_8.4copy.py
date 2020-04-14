# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить параметры,
# общие для приведенных типов. В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
from pprint import pprint


class StoreMashines:
    def __init__(self, title, price, quantity):
        self.title = title
        self.price = price
        self.quantity = quantity
        self.my_store = []
        self.store_print = []
        self.store_scanner = []
        self._store_copier = []
        # self.my_store_full = []
        self.my_unit = {'Модель устройства': self.title, 'Цена за ед': self.price, 'Количество': self.quantity}

    def __str__(self):
        return f'Наименование:{self.name}, цена: {self.price}, количество: {self.quantity}'

    # @classmethod
    # @staticmethod
    def reception(self):
        pass

class Printer(StoreMashines):

    def to_print(self, print_color):
         self.print_color = print_color
         return f'to print smth {self.print_color} times'

    def reception(self):
        while True:
            try:
                unit = input(f'Введите наименование: ')
                unit_p = int(input(f'Введите цену за ед: '))
                unit_q = int(input(f'Введите количество: '))
                unique = {'Модель устройства': unit, 'Цена за ед': unit_p, 'Количество': unit_q}
                self.my_unit.update(unique) # добавляем словарь (unique) ---> в словарь(my_unit),
                self._my_store.append((unique)) # добавляем словарь (my_unit) ---> в список my_store
                self.store_print.append(self._my_store)
                # self.my_store_full.append(self.store_print)
                print(f'Текущий список:\n {self._my_store}')
            except ValueError:
                return f'Ошибка ввода данных!'
            print(f'Для выхода - Q, продолжение - Enter')
            q = input(f'---: ')
            if q == 'Q' or q == 'q':
                # self.my_store_full.append(self.my_unit) # добавяем список (my_store) ---> в список my_store_full
                print('Весь склад:')
                print('-------------------------------------', end='')
                print('--------------------------------')
                for i, item in enumerate(self._my_store, 1):
                    print(f'{i}) {item}')
                pprint(f'Весь склад:\n {self._my_store}')
                return f'Выход'
                break
            else:
                continue

#
#
# class Scanner(StoreMashines):
#     def to_scan(self):
#         return f'to scan smth {self.numb} times'
#
#
# class Copier(StoreMashines):
#     def to_copier(self):
#         return f'to copier smth  {self.numb} times'
#

unit_1 = Printer('HP', 1500, 10)

# unit_2 = Scanner('Canon', 1200, 5, 10)
# unit_3 = Copier('Xerox', 1500, 1, 15)
print(unit_1.reception())
print(unit_1.to_print('Цветной'))
# print(unit_2.reception())
# print(unit_3.reception())
# print(unit_1.to_print())
# print(unit_3.to_copier())