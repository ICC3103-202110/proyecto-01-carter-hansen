from cards import Cards

class Contessa(Cards) :
    def __init__(self, name = "Contessa", i = 4, status = 0):
        super(Contessa, self).__init__(name, i, status)

    def attack(self) :
        return "No"
    def counter_attack(self):
        return "BloquearAsesinato"
