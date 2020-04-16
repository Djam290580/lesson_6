# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32

def calculation_1():
    wages = {}
    try:
        with open('text_3.txt', 'r', encoding='utf-8') as my_obj:
            for line in my_obj:
                i = line.split()
                wages[i[0]] = float(i[1])
            print('Меньше 20000 получают:')
            for name, wage in wages.items():
                if wage < 20000:
                    print(name)
            print(f'Средняя зарплата равна {sum(wages.values()) / len(wages)}')
    except IOError:
        print('Бухгалтер на больничном. Зарплаты не будет')
    except:
        print('Ошибка! Что то пошло не так ')

calculation_1()


    # line = line.split()
    # print(line)
    # print(i[1] for i[1] in line if float(i[1]) < 20000 else (less.append(i[0]) and s_sum.append(i[1]))
#
#
# print(f'Salary less 20 000 {less}. Average salary - {sum(map(float, s_sum)) / len(s_sum)}')


# with open('text_3.txt', 'r', encoding='utf-8') as my_obj:
#     s_sum = []
#     less = []
#     line = my_obj.read().split('\n')
#     print(line)
#     for i in line:
#         i = i.split()
#         print(i)
#         if float(i[1]) < 20000:
#             less.append(i[0])
#         s_sum.append(i[1])
#
# print(f'Salary less 20 000 {less}. Average salary - {sum(map(float, s_sum)) / len(s_sum)}')
