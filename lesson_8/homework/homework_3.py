# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

n = input('Введите число: ')
n_sum1 = int(n)
n_sum2 = int(n + n)
n_sum3 = int(n + n + n)
print(n_sum2)
print(n_sum3)
result = n_sum1 + n_sum2 + n_sum3
print(result)
