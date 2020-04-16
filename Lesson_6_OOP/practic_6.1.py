class Auto:
    auto_count = 0  # Глобальная переменная, атрибут класса

    def __init__(self, auto_name,auto_model, auto_year ):
        self.auto_name = auto_name
        self.auto_model = auto_model
        self.auto_year = auto_year
        Auto.auto_count += 1
        print(Auto.auto_count)

    def on_start(self, speed): # локальная перменная, доступна только внутри фнукции
        if speed > 80:
            print('Slow pleese')
        print(f'Go - {self.auto_name}!.Speed = {speed}!')

    def on_stop(self):
        print(f'Stop!')

auto_1 = Auto('Lada', 'Niva', '2019')
print(auto_1.auto_name)
auto_1.on_start(90)

auto_2 = Auto('Mazda', '3', '2019')
print(auto_2.auto_name)
auto_2.on_stop()

auto_3 = Auto('Mazda', '3', '2019')
print(auto_3.auto_name)
auto_3.on_stop()