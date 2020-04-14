try:
    res = 100 / 0
# except(ошибок) может быть много
except ZeroDivisionError:
    print('O!')
# else выполняется когда все хорошо, else можно использовать для явного вывода - все хорошо
else:
    print(f'Res = {round(res, 2)}')
# finally выполняется по любому, независимо от того пошло все хорошо или плохо
finally:
    print('Game over')