
class MyClass:
    def __init__(self, param_1, param_2):
        self.param_1 = param_1
        self.param_2 = param_2

    def __add__(self, other):
        return MyClass(self.param_1 + other.param_1, self.param_2 + other.param_2)

    def __str__(self):
        return f'Object with param {self.param_1, self.param_2}'

m_1 = MyClass(78, 45)
m_2 = MyClass(88, 44)
m_3 = MyClass(10, 20)

print(m_1 + m_2 + m_3)



