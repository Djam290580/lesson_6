# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

from random import randint

# title_file = input(f'Введите название файла: ')
# with open(f'{title_file}.txt', 'w') as my_file:
#     num = input('Введите числа через пробел: ')
#     my_file.writelines(num)
#     num_sum = num.split()
#     print(sum(map(int, num_sum)))

#---------------------------------------------------------------------------
# title_file = input(f'Введите название файла: ')
# sum_num = 0
# with open(f'{title_file}.txt', 'w') as my_f:
#     for i in range(10):
#         line = randint(1, 10)
#         sum_num += line
#         my_f.write(str(line) + ' ')
#         print(sum_num)

with open('text_55.txt', 'r') as my_f:
    # number_sum = my_f.read()
    number_sum = my_f.read().split()
    print(number_sum)
    # print(sum(map(int, number_sum.split())))
    print(sum(map(int, number_sum)))
