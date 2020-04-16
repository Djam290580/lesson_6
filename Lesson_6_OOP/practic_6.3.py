class Transport:
    def __init__(self, auto_name, auto_model, auto_year=2020):
        self.auto_name = auto_name
        self.auto_model = auto_model
        self.auto_year = auto_year

    def on_start(self):
        print(f'Go - {self.auto_name}!')

    def on_stop(self):
        print('Stop!')


class Auto(Transport):
    def __init__(self, auto_name, auto_model, auto_year=2018, d=1.7):
        super().__init__(auto_name, auto_model, auto_year)
        # super() обращение к классу выше
        self.d = d

    def auto_method(self):
        print('Method class auto')

tr = Transport('Iveco', 'KTM')
print(tr.auto_name)
auto_1 = Auto('Renault', 'Logan')
auto_1.on_start()
auto_1.auto_method()
print(auto_1.auto_year)
print(auto_1.d)