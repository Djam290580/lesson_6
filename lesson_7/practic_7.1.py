
class MyClass:
    def __init__(self, param_1, param_2):
        self.param_1 = param_1
        self.param_2 = param_2

    def __str__(self):
        # return f'Object with param - {self.param_1} {self.param_2}!!!'
        return False
        # При обращ-ии к __str__, если мы возвращаем другой тип данных то будет ошибка
        # TypeError: __str__ returned non-string (type int)

    # def __del__(self):
    #     print(f"Удаляем объект {self.param} класса MyClass")


mc = MyClass('Hi', 'People')
# del mc  # если удалть объект mc, то при обращении к нем будет ошибка NameError: name 'mc' is not defined
print(mc)
print('Python')
# a = MyClass('abc')
# print(a.param)
