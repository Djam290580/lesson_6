# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod,
# должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.
import datetime

class Date():
    def __init__(self, year_month_day):
        self.year_month_day = str(year_month_day)

    @classmethod
    def int_f(cls, year_month_day):
        par_1 = [int(i) for i in year_month_day.split('-')]
        return par_1
        #-------------------------------
        # a = year_month_day.split('-')
        # for i in range(len(a)):
        #     a[i] = int(a[i])
        # return a
        #---------------------------------
        # par_1 = []
        # par_2 = year_month_day.split('-')
        # for i in par_2:
        #     par_1.append(i)
        # return int(par_1[0]), int(par_1[1]), int(par_1[2])

    @staticmethod
    def valid(year, month, day):
        try:
            data = datetime.date(year, month, day)
        except ValueError:
            print('ValueError is out of range!!!')
        except TypeError:
            print('Enter an integer!!!')
        except NameError:
            print('Name is not defined')
        else:
            return data

    def __str__(self):
        return f'Текущая дата: {self.year_month_day}'
        # return f'Текущая дата {Date.int_f(self.year_month_day)}'


data = Date('2000-3-25')
print(data)
# print(data.valid(2000, 3, 20))
print(Date.int_f('2000-3-25'))
print(type(Date.int_f('2000-3-25')))

#-------------------------------------Вариант решения----------------------------------------------------------------

# class Data:
#     def __init__(self, day_month_year):
#         # self.day = day
#         # self.month = month
#         # self.year = year
#         self.day_month_year = str(day_month_year)
#
#     @classmethod
#     def extract(cls, day_month_year):
#         my_date = []
#
#         for i in day_month_year.split():
#             if i != '-': my_date.append(i)
#
#         return int(my_date[0]), int(my_date[1]), int(my_date[2])
#
#     @staticmethod
#     def valid(day, month, year):
#
#         if 1 <= day <= 31:
#             if 1 <= month <= 12:
#                 if 2019 >= year >= 0:
#                     return f'All right'
#                 else:
#                     return f'Неправильный год'
#             else:
#                 return f'Неправильный месяц'
#         else:
#             return f'Неправильный день'
#
#     def __str__(self):
#         return f'Текущая дата {Data.extract(self.day_month_year)}'
#
#
# today = Data('11 - 1 - 2001')
# print(today)
# print(Data.valid(11, 11, 2022))
# print(today.valid(11, 13, 2011))
# print(Data.extract('11 - 11 - 2011'))
# print(today.extract('11 - 11 - 2020'))
# print(Data.valid(1, 11, 2000))
#

