# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.
#
# counter = 0
# with open('text777.txt', 'r') as file:
#     for line in file:
#         counter += 1
#         line_words = line.split()
#         print(line, line_words, 'Длина строки:', len(line_words))
#     print('Всего строк: ', counter)

#----------------------------------------------------------------------------------------------------------------

with open('text777.txt', 'r') as f:
    my_line = f.readlines()
    print(my_line)
    for index, value in enumerate(my_line):
        number_of_words = len(value.split())
        print(f'Строка {index + 1} содержит {number_of_words}')