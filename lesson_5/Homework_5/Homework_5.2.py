# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

my_f = open('test1.txt', 'w')
lines = ['stroka_1\n', 'stroka_2\n', 'stroka_3\n']
my_f.writelines(lines)
my_f = open('test1.txt', 'r')
content = my_f.read()
print(f'Содержимое файла: \n{content}')

my_f = open('test1.txt', 'r')
content = my_f.readlines()
for i in range(len(content)):
    print(f'Общее кличество символов {i + 1}- строки {len(content[i])}')
print()

my_f = open('test1.txt', 'r')
content = my_f.readlines()
print(f'Количество строк в файле - {len(content)}')
print()

my_f = open('test1.txt', 'r')
content = my_f.read()
content = content.split()
print(content)
print(f'Общее количество слов - {len(content)}')

my_f.close()
