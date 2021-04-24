class Player() :
    
    def __init__(self, n, coin, influence) :
        self.__name = n
        self.__coin = coin
        self.__influence = influence
        self.__status = 0

    @property
    def name(self) :
        return self.__name

    @property
    def coin(self):
        return self.__coin
    #@coin.setter
    def coin_setter(self, value):
        self.__coin = self.coin + value

    @property
    def influence(self):
        return self.__influence

    def influence_setter(self, card1, card2) :
        new_influence = []
        if card2 != 0 :
            new_influence.append(card1)
            new_influence.append(card2)
            self.__influence =  new_influence
        else :
            new_influence.append(card1)
            self.__influence =  new_influence

    @property
    def status(self) :
        return self.__status
    def status_setter(self, new_status) :
        if new_status == 1 :
            self.__status = new_status
        else :
            self.__status = 0
        


        


