# Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

time = int(input('Введите количество секунд: '))
hour = time // 3600
minutes = int((time - hour * 3600) / 60)
seconds = time - (hour * 3600 + minutes * 60)
print(hour)
print(minutes)
print(seconds)
print('%02d:%02d:%02d' % (hour, minutes, seconds))

