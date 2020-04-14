class Myclass:
    def __init__(self, param):
        self.param = param

    @staticmethod
    def my_met(p_1, p_2):
        return f'Hi - {p_1 + p_2}'

    def my_met_norm(self, p_2):
        return Myclass.my_met(self.param, p_2)

# Myclass.my_met()
my_1 = Myclass(90)
print(my_1.my_met_norm(10))
