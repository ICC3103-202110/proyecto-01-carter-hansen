from abc import ABC, abstractmethod

class Cards(ABC) :
    
    def __init__(self, name, i, status) :
        self.__name = name
        self.__i = i                         #This will be an easier way to differenciate cards 
        self.__status = status        

    @property
    def name(self):
        return self.__name

    @property
    def i(self) :
        return self.__i

    @property
    def status(self):
        return self.__status

    def status_setter(self, new_status) :
        if new_status == 1 :
            self.__status = new_status
        else :
            self.__status = 0

    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def counter_attack(self):
        pass