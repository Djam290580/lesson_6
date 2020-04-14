class Myclass:
    """"Class with classmethod and staticmethod"""

    def __init__(self, par):
        self.par = par

    @classmethod
    def my_cl(cls, param):
        print(cls, param, Myclass(88).par)



    @staticmethod
    def my_met(p_1, p_2):
        return f'Hi - {p_1 + p_2}'

    def my_met_norm(self, p_2):
        return Myclass.my_met(self.param, p_2)

print(Myclass.__doc__) # Строка документации класса
print()
print(Myclass.__name__) # Имя класса
print()
print(Myclass.__module__) # Имя модуля
print()
print(Myclass.__bases__) # Кортеж с базовыми классами
print()
print(Myclass.__dict__) # Словарь с атрибутами класса



