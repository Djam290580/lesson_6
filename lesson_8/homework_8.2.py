# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


inp_data = input('Only positive numbers -  ')

try:
    res = 100 / int(inp_data)
    if int(inp_data) < 0:
        raise OwnError('Negative number!!!')

except ValueError:
    print('Not string!!!')

except ZeroDivisionError:
    print("You can't divide by zero!!!")

except OwnError as err:
    print(err)

else:
    print(f'Res = {round(res, 2)}')

finally:
    print('Game over')
