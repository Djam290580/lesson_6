class Auto:
    def __init__(self, auto_name, auto_model, auto_year):
        self.auto_name = auto_name
        self._auto_model = auto_model
        self.__auto_year = auto_year

    def on_start(self, speed):
        if speed > 80:  # локальная перменная
            print('Slow pleese')
        # print(f'Go - {self.auto_name}!.Speed = {speed}!')
        # print(f'Go - {self._auto_model}!.Speed = {speed}!')
        print(f'Go - {self.__auto_year}!.Speed = {speed}!')

    def __on_stop(self):
        print('Stop!')


auto_1 = Auto('Lada', 'Niva', '2000')
# print(auto_1.auto_name)
# auto_1._auto_model = 'Kalina'
# print(auto_1._auto_model)
# auto_1.Auto__auto_year = 1199
print(auto_1._Auto__auto_year)
auto_1.on_start(60)
auto_1._Auto__on_stop()

# auto_2 = Auto('Mazda', '3', '2019')
# print(auto_2.auto_name)
# auto_2.on_stop()
