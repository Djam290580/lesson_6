import os


# os.rename('test444.txt', 'test555.txt')  # переименовываем файл с помощью os.rename

# os.remove('test555.txt') # удаляем файл с помощью os.remove
content = os.listdir()
print(content)


# out_f = open("out_file.txt", "w")
# str_list = ['stroka_1\n', 'stroka_2\n', 'stroka_3\n']
# out_f.writelines(str_list)
# out_f.close()
