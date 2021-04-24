from cards import Cards

class Ambassador(Cards) :
    def __init__(self, name = "Ambassador", i = 2, status = 0):
        super(Ambassador, self).__init__(name, i, status)

    def attack(self) :
        return "Cambio"
    def counter_attack(self):
        return "BloquearExtorsión"