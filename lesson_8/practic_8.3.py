class Myclass:
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

# Myclass.my_cl(88)
my_1 = Myclass(90)
my_1.my_cl(77)
print(my_1.my_met_norm(10))

