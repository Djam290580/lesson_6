# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
# на ваше усмотрение.  Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов,
# и при его нарушении выводить соответствующее сообщение и завершать скрипт.

from time import sleep
import datetime
from itertools import cycle

# class TrafficLight:
#     __color = ['Красный', 'Желтый', 'Зеленый']
#
#     def running(self):
#         i = 0
#         while i != 3:
#             print(f'Светофор переключается \n {TrafficLight.__color[i]}')
#             if i == 0:
#                 sleep(7)
#             elif i == 1:
#                 sleep(2)
#             elif i == 2:
#                 sleep(7)
#             elif i == 1:
#                 sleep(2)
#             i += 1
#
# svetofor = TrafficLight()
# print(svetofor)
# print(type(svetofor))
# svetofor.running()

#---------------------------------2 Вариант----------------------------------

# class TrafficLight:
#     __color = ['Красный', 'Желтый', 'Зеленый']
#
#     def running(self):
#         while True:
#
#             print(f'Светофор переключается на\n {TrafficLight.__color[0]}')
#             sleep(7)
#
#             print(f'Светофор переключается на\n {TrafficLight.__color[1]}')
#             sleep(3)
#
#             print(f'Светофор переключается на\n {TrafficLight.__color[2]}')
#             sleep(7)
#
#             print(f'Светофор переключается на\n {TrafficLight.__color[1]}')
#             sleep(3)
#
#
# svetofor = TrafficLight()
# print(svetofor)
# print(type(svetofor))
# svetofor.running()

#------------------------------------------3 Вариант-------------------------------------------------------

# class TrafficLight:
#     __color = 'Черный'
#
#     def running(self):
#         while True:
#             print('TrafficLight is red now')
#             sleep(7)
#
#             print('TrafficLight is yellow now')
#             sleep(3)
#
#             print('TrafficLight is green now')
#             sleep(7)
#
#             print('TrafficLight is yellow now')
#             sleep(3)
#
#
# svetofor = TrafficLight()
# print(svetofor)
# print(type(svetofor))
# svetofor.running()

#-----------------------------------------------------4 Вариант c цветами------------------------------------
class TrafficLight:
    def __init__(self, go, wait, stop):
        self.__color = [go, wait, stop]

    def running(self):
        # Класс datetime.datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0, tzinfo=None)
        # - комбинация даты и времени.
        t = str(datetime.datetime.time(datetime.datetime.now()))
        print(t)
        # datetime.time() - объект времени (с отсечением даты)
        # datetime.now(tz=None) - объект datetime из текущей даты и времени
        correct_order = ['red', 'yellow', 'green']
        new_list = [i for i in self.__color if i == correct_order[self.__color.index(i)]]
        print(new_list)
        if len(new_list) < 3:
            print('Wrong order')
        else:
            self.__color.append('yellow')
            for i in cycle(self.__color):
                if i == 'yellow':
                    print(f'\033[33m{i}')
                    sleep(2)
                elif i == 'red':
                    print(f'\033[31m{i}')
                    sleep(7)
                else:
                    print(f'\033[32m{i}')
                    sleep(7)
                if 0 <= int(t[:2]) <= 5:
                    break

a = TrafficLight('red', 'yellow', 'green')
a.running()


