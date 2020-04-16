
#------------------------------------------Множественное наследование!!!----------------------------------------------

#------------------------------------------Несколько дочерних классов у одного родителя-------------------------------

# класс Transport
class Transport:
    def transport_method(self):
        print("Родительский метод класса Transport")


# класс Auto, наследующий Transport
class Auto(Transport):
    def auto_method(self):
        print("Дочерний метод класса Auto")


# класс Bus, наследующий Transport
class Bus(Transport):
    def bus_method(self):
        print("Дочерний метод класса Bus")

a = Auto()
a.transport_method()
b = Bus()
b.transport_method()

#------------------------------------------Несколько родителей у одного класса----------------------------------------

class Player:
    def player_method(self):
        print("Родительский метод класса Player")


class Navigator:
    def navigator_method(self):
        print("Родительский метод класса Navigator")


class MobilePhone(Player, Navigator):
    def mobile_phone_method(self):
        print("Дочерний метод класса MobilePhone")

m_p = MobilePhone()
m_p.player_method()
m_p.navigator_method()
