from cards import Cards

class Captain(Cards) :
    def __init__(self, name = "Captain", i = 3, status = 0):
        super(Captain, self).__init__(name, i,status)

    def attack(self) :
        return "Extorsión"
    def counter_attack(self):
        return "BloquearExtorsión"

