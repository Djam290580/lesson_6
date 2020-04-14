class Myclass:
    atr = 0
    def __init__(self, param):
        Myclass.param = param

    @staticmethod # существуют методы, вызываемые напрямую через имя класса (статические методы)
    # Понятие декоратора, т. е., функции, расширяющей поведение другой функции или метода класса
    # По сути обычная функция внутри класса, которая понятия не имеет что внутри находится
    # и статич. метод не может ни на что влиять, у нее нет (self), а также может быть переопределена в потомках
    def my_met():
        print(f'Hi - {Myclass.param}') # т.е. мы можем обращаться к атрибуту класса через класс Myclass.atr


# Myclass.my_met()
my_1 = Myclass('90')
my_1.my_met()
print()
my_2 = Myclass('111')
my_2.my_met()
print()
my_1.my_met()