
with open('test444.txt', 'w') as my_file:
    print('Something', file=my_file)

# my_file = open('test777.txt')
# content = my_file.read()
# print(content)
# print('!!!!!!')
# content = my_file.read()
# print(content)
#------------------------------------------------
# with open('test777.txt') as my_file:
#     print(my_file.name)
#     print(my_file.closed)
#
# print(my_file.mode)
#
# #--------------------------------------------------------
# try:
#     with open('test777.txt', 'r+') as my_file:
#         my_file.write('Java\n')
#         content = my_file.read()
#         print(content)
# except IOError:
#     print('File not found')

#-----------------------------------------------------------
# try:
#     with open('test777.txt', 'a') as my_file:
#         my_file.write('Java\n')
# except IOError:
#     print('File not found')
#----------------------------------------------------------
# try:
#     with open('test777.txt', 'x') as my_file:
#         for  i in my_file:
#             print(i)
# except IOError:
#     print('File not found')
#-----------------------------------------------------------

# my_file.writelines(['Python', 'the', 'BEST p\n'])
# content = my_file.read()
# print(content)
# my_file.close()
