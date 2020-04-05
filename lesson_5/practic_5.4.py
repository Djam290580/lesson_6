
with open("python.txt", "w") as f_obj:
    print("Необычная работа функции print", file=f_obj)


f_obj = open('python.txt')
content = f_obj.read()
print(content)