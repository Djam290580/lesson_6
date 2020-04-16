# Возможна ситуация, когда у классов-родителей совпадают имена атрибутов и методов.
# В этом случае при обращении к такому атрибуту или методу через наследник оно будет адресовано
#  к атрибуту или методу того класса-родителя, который значится первым.


class Shape:
    def __init__(self, param_1, param_2):
        self.param_1 = param_1
        self.param_2 = param_2

    def get_params(self):
        return f"Параметры Shape: {self.param_1}, {self.param_2}"

class Material:
    def __init__(self, param_1, param_2):
        self.param_1 = param_1
        self.param_2 = param_2

    def get_params(self):
        return f"Параметры Material: {self.param_1}, {self.param_2}"


class Triangle(Shape, Material):
    def __init__(self, param_1, param_2):
        super().__init__(param_1, param_2)
        pass

t = Triangle(10, 20)
print(t.get_params())