# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить параметры,
# общие для приведенных типов. В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

# Продолжить работу над первым заданием.
# Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
# можно использовать любую подходящую структуру, например словарь.

# Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
# изученных на уроках по ООП.

from pprint import pprint

class StoreMashines:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.my_store_print = []
        self.my_store_scan = []
        self.my_store_cop = []
        self.my_store_all = []

    def __str__(self):
        return f'Наименование:{self.name}, цена: {self.price}, количество: {self.quantity}'

    # @classmethod
    # @staticmethod
    def reception(self):
        pass

class Printer(StoreMashines):
    def __init__(self, name, price, quantity, specifications):
        super().__init__(name, price, quantity)
        self.specifications = specifications

    def __str__(self):
        return f'Наименование:{self.name}, цена: {self.price}, количество: {self.quantity}, вид: {self.specifications}'

    def __del__(self):
        return 'Delete object - class Printer'

    def reception(self):
        while True:
            try:
                unit = input('Введите наименование: ')
                unit_p = int(input('Введите цену за ед: '))
                unit_q = int(input('Введите количество: '))
                unit_a = input('Вид принтера: ')
                unique = {f'Модель устройства': {unit}, 'Цена за ед': unit_p, 'Количество': unit_q, 'Вид': unit_a}
                self.my_store_print.append((unique)) # добавляем словарь (unique) ---> в список my_store
                self.my_store_all.append((unique))
                print(f'Текущий список:\n {unique}')
            except ValueError:
                return f'Ошибка ввода данных!'
            print(f'Для выхода - Q, продолжение - Enter')
            q = input(f'---: ')
            if q == 'Q' or q == 'q':
                for i, item in enumerate(self.my_store_print, 1):
                    print(f'{i}) {item}')
                print('Весь склад:')
                print('-------------------------------------', end='')
                print('--------------------------------')
                for i, item in enumerate(self.my_store_all, 1):
                    pprint(f'{i}) {item}')
                return f'Выход'
                break
            else:
                continue


class Scanner(StoreMashines):
    def __init__(self, name, price, quantity, type):
        super().__init__(name, price, quantity)
        self.type = type

    def __del__(self):
        return 'Delete object - class Scanner'

    def __str__(self):
        return f'Наименование:{self.name}, цена: {self.price}, количество: {self.quantity}, описание: {self.type}'

    def reception(self):
        while True:
            try:
                unit = input('Введите наименование: ')
                unit_p = int(input('Введите цену за ед: '))
                unit_q = int(input('Введите количество: '))
                unit_a = input('Вид: ')
                unique = {f'Модель устройства': {unit}, 'Цена за ед': unit_p, 'Количество': unit_q, 'Вид': unit_a}
                self.my_store_scan.append(unique) # добавляем словарь (unique) ---> в список my_store
                self.my_store_all.append(unique)
                print(f'Текущий список:\n {unique}')
            except ValueError:
                return f'Ошибка ввода данных!'
            print(f'Для выхода - Q, продолжение - Enter')
            q = input(f'---: ')
            if q == 'Q' or q == 'q':
                for i, item in enumerate(self.my_store_scan, 1):
                    print(f'{i}) {item}')
                print('Весь склад:')
                print('-------------------------------------', end='')
                print('--------------------------------')
                for i, item in enumerate(self.my_store_all, 1):
                    pprint(f'{i}) {item}')
                return f'Выход'
                break
            else:
                continue



class Copier(StoreMashines):
    def __init__(self, name, price, quantity, varieties):
        super().__init__(name, price, quantity)
        self.varieties = varieties

    def __str__(self):
        return f'Наименование:{self.name}, цена: {self.price}, количество: {self.quantity}, описание: {self.varieties}'

    def __del__(self):
        return 'Delete object - class Copier'

    def reception(self):
        while True:
            try:
                unit = input('Введите наименование: ')
                unit_p = int(input('Введите цену за ед: '))
                unit_q = int(input('Введите количество: '))
                unit_a = input('Вид: ')
                unique = {f'Модель устройства': {unit}, 'Цена за ед': unit_p, 'Количество': unit_q, 'Вид': unit_a}
                self.my_store_cop.append(unique) # добавляем словарь (unique) ---> в список my_store
                self.my_store_all.append(unique)
                print(f'Текущий список:\n {unique}')
            except ValueError:
                return f'Ошибка ввода данных!'
            print(f'Для выхода - Q, продолжение - Enter')
            q = input(f'---: ')
            if q == 'Q' or q == 'q':
                for i, item in enumerate(self.my_store_cop, 1):
                    print(f'{i}) {item}')
                print('Весь склад:')
                print('-------------------------------------', end='')
                print('--------------------------------')
                for i, item in enumerate(self.my_store_all, 1):
                    pprint(f'{i}) {item}')
                return f'Выход'
                break
            else:
                continue


unit_1 = Printer('HP', 1500, 10, 'Цветной')
print(unit_1)
print(unit_1.reception())
unit_2 = Scanner('Canon', 1200, 5, 10)
print(unit_2)
print(unit_2.reception())
unit_3 = Copier('Xerox', 1500, 1, 15)
print(unit_3)
pprint(unit_3.reception())
a_1 = StoreMashines('Print', 100, 10)
print(a_1)

