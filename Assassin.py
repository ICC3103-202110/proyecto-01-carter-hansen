from cards import Cards

class Assassin(Cards) :
    def __init__(self, name = "Assassin", i = 1, status = 0):
        super(Assassin, self).__init__(name, i, status)

    def attack(self) :
        return "Asesinato"
    def counter_attack(self):
        return "No"