# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

with open('text_4.txt', 'w') as my_file:
    my_file.writelines(['One - 1\n', 'Two - 2\n', 'Three - 3\n', 'Four - 4\n'])

rus_list = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
new_file = []
with open('text_4.txt', 'r') as my_file:
    line = my_file.read().split('\n')
    print(line)
    with open('text_44.txt', 'a') as my_file:
        for i in line:
            i = i.split(' - ')
            print(i)
        new_file.append(rus_list[i[0]] + ' - ' + i[1])
        print(new_file)

# rus = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
# new_file = []
# with open('file_4.txt', 'r') as file_obj:
#     #content = file_obj.read().split('\n')
#     for i in file_obj:
#         i = i.split(' ', 1)
#         new_file.append(rus[i[0]] + '  ' + i[1])
#     print(new_file)
#
# with open('file_4_new.txt', 'w') as file_obj_2:
#     file_obj_2.writelines(new_file)
