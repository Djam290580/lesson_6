# Exception обязательно указывать, т.е. OwnError является помком от Exception
class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt

inp_data = input('Only positive numbers -  ') # Задача отсечь все отрицательные значения и получать только положительные

# Блок try содержит инструкции, которые могут привести к возникновению исключения
#  а в блоке except реализован его перехват.
try:
    inp_data = int(inp_data)
    if inp_data < 0:
        raise OwnError('Negative number!!!') # Создается объект собственного класса исключения с помощью оператора raise
# except(ошибок) может быть много
except ValueError:
    print('Not string!!!')
except OwnError as err:  # err - это псевдоним!!!
    print(err)
# else выполняется когда все хорошо, else можно использовать для явного вывода - все хорошо
else:
    print(f'Res = {inp_data}')
# finally выполняется всегда, независимо от того пошло все хорошо или плохо
finally:
    print('Game over')