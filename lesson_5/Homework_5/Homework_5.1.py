# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

# title_file = input(f'Введите название файла: ')
# with open(f'{title_file}.txt', 'w') as my_file:
#     print("Файл. Имя: ", my_file.name)
#     line = input('Введите данные:\n')
#     while line:
#         my_file.write(f'{line}\n')
#         line = input('Введите данные:\n')
#         if not line:
#             break
#
# with open(f'{title_file}.txt', 'r') as my_file:
#     content = my_file.readlines()
#     print(content)
#
# with open(f'{title_file}.txt', 'r') as my_file:
#     for line in my_file:
#         print(line)
#
# with open(f'{title_file}.txt', 'r') as my_file:
#     while True:
#         content = my_file.read(1024)
#         print(content)
#         if not content:
#             break
#-------------------------------------------------------------------------------------------
# with open('text777.txt', 'w', encoding='utf-8') as my_file:
#     while True:
#         line = input('Input new string or empty string to done: ')
#         if not line: # если строка путая, цикл прекращается
#             break
#         # my_file.write(line + '\n')
#         print(line, file=my_file) # ввод строки в файл через print
#--------------------------------------------------------------------------------------------------
file = open('test.txt', 'w')

line = None
while line != '':
    line = input('Вводите строку: ')
    file.write(f'{line}\n') if line != '' else file.close()
# my_f = open('test.txt', 'w')
# line = input('Введите текст \n')
# while line:
#     my_f.writelines(line)
#     line = input('Введите текст \n')
#     if not line:
#         break



#-----------------------------------------------------------------

# try:
#     title_file = input(f'Введите название файла: ')
#     with open(f'{title_file}.txt', 'x+') as my_file:
#         print("Файл. Имя: ", my_file.name)
# except FileExistsError:
#     print('Такой файл уже существует!!!')
#
# with open(f'{title_file}.txt', 'a') as my_file:
#     text_1 = input('Введите данные:  \n')
# title_file = input(f'Введите название файла: ')
# with open(f'{title_file}.txt', 'w') as my_file:
#     print("Файл. Имя: ", my_file.name)
# with open(f'{title_file}.txt', 'a') as my_file:
#     text_1 = input('Введите данные:  \n')
# while True:
#     my_file.writelines(text_1)
#     text_1 = input('Введите данные:  \n')
#     if not text_1:
#         break
#
# print(f'{text_1}', file=my_file)
