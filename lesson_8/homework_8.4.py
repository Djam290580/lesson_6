# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить параметры,
# общие для приведенных типов. В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
class Storage():
    storage_count = 0

    def __init__(self):
        self.name = input(f'\033[1m\033[4mВведите наименование склада:')
        self.adress = input(f'Введите адрес:')
        # self.description_list = []
        self.all_store = []
        # self.description = {'Название': self.name, 'Адрес': self.adress}
        Storage.storage_count += 1
        print(Storage.storage_count)

    def __str__(self):
        return f'Название: {self.name}, Адрес: {self.adress}'

    #
# class Office_equipment(Storage):
#     def __init__(self, title, price, quantity):
#         super().__init__(self)
#         self.title = title
#         self.price = price
#         self.quantity = quantity
#         self.my_unit = []
#         # self.my_store = {'Наименование': self.title, 'Цена': self.price, 'Количество': self.quantity}
#
#     def storage_f(self, b=1):
#
#         self.all_store(b, self.my_unit)
#         b += 1
#         print(self.all_store)
    # def __str__(self):
    #     return f'{self.title}, цена:{self.price}, количество:{self.quantity}'

    # def store_fun(self, goods_number, b = 1):
    #     self.goods_number = goods_number
    #     self.b = b
    #     self.my_unit = []
    #     self.my_store = {}
    #     self.title = input(f'Введите наименование: ')
    #     self.price = int(input(f'Введите цену за ед: '))
    #     self.quantity = int(input(f'Введите количество: '))
    #     while self.b <= goods_number:
    #         self.my_store = {'Наименование': self.title, 'Цена': self.price, 'Количество': self.quantity}
    #         self.my_unit.append(self.my_store)
    #         b += 1


a_1 = Storage()
print(a_1)
a_2 = Storage()
print(a_2)
# b_1 = Office_equipment('Принтер', 100, 10)
# print(b_1)
# b_1 = Office_equipment()
# b_1.store_fun(3)

# class Printer(Office_equipment):
#     def __init__(self):
#
#
# class Copier(Office_equipment):
#     def __init__(self):
