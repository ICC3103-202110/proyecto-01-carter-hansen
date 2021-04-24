from cards import Cards

class Duke(Cards) :
    def __init__(self, name = "Duke", i = 0, status = 0):
        super(Duke, self).__init__(name, i,status)

    def attack(self) :
        return "Impuesto"
    def counter_attack(self):
        return "BloquearAyudaExtranjera"


