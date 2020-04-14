# num_list = []
# par_1 = False
# while True:
#     number = input('Введите числа или "Q" для выхода:').split()
#     # num_list.append(number)
#     print(number)
#     for i in range(len(number())):
#         if number[i] == 'Q':
#             par_1 = True
#             break
#         else:
#             num_list

# def summary():
#     result = 0
#     while True:
#         print(f'Текущая сумма = {result}')
#         inputs_s = input('Введите строку чисел, через пробел для подсчета суммы (# - символ для завершения): ').split()
#         for value in inputs_s:
#             if value == '#':
#                 print(f'Окончательная сумма = {result}')
#                 break
#             try:
#                 result += float(value)
#             except ValueError:
#                 print(f'Значение {value} не было учетно при подсчете суммы - неверный тип')
#         else:
#             # Если символа заверешния программы не было, то продолжаем ввод данных
#             continue
#         # Сюда мы дойдем, если только встретим символ завершения программы
#         break
#     return f'Окончательная сумма = {result}'
#
# summary()
#
# result = []
# while True:
#     numbers = input('Введите числа для списка(# - символ для завершения):\n')
#     for value in numbers:
#         if value == '#':
#             print(f'Список сформирован: {result}')
#             break
#     # try:
#     #     if value.isdigit():
#     #         result.append(numbers)
#     #             # print(result)
#     # except ValueError:
#     #     print('ValueError')
# print(result)

from pprint import pprint

class StoreMashines:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        # self.numb = number_of_lists
        # self.my_store_full = []
        self.my_store = []
        # self.my_unit = {'Модель устройства': self.name, 'Цена за ед': self.price, 'Количество': self.quantity}

    def __str__(self):
        return f'Наименование:{self.name}, цена: {self.price}, количество: {self.quantity}'

    # @classmethod
    # @staticmethod
    def reception(self):
        while True:
            try:
                unit = input(f'Введите наименование: ')
                unit_p = int(input(f'Введите цену за ед: '))
                unit_q = int(input(f'Введите количество: '))
                unique = {'Модель устройства': unit, 'Цена за ед': unit_p, 'Количество': unit_q}
                # self.my_unit.update(unique) # добавляем словарь (unique) ---> в словарь(my_unit),
                self.my_store.append((unique)) # добавляем словарь (my_unit) ---> в список my_store
                # self.my_store_full.append(self.my_store)
                print(f'Текущий список:\n {self.my_store}')
            except:
                return f'Ошибка ввода данных!'
            print(f'Для выхода - Q, продолжение - Enter')
            q = input(f'---: ')
            if q == 'Q' or q == 'q':
                # self.my_store_full.append(self.my_unit) # добавяем список (my_store) ---> в список my_store_full
                print('Весь склад:')
                print('-------------------------------------', end='')
                print('--------------------------------')
                for i, item in enumerate(self.my_store, 1):
                    print(f'{i}) {item}')
                # pprint(f'Весь склад:\n {self.my_store_full}')
                return f'Выход'
                break
            else:
                continue


class Printer(StoreMashines):
     def to_print(self, ):
        return f'to print smth {self.numb} times'
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
print(unit_1)
# unit_2 = Scanner('Canon', 1200, 5, 10)
# unit_3 = Copier('Xerox', 1500, 1, 15)
print(unit_1.reception())
# print(unit_2.reception())
# print(unit_3.reception())
# print(unit_1.to_print())
# print(unit_3.to_copier())