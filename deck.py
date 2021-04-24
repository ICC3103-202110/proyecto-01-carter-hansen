from Duke import Duke
from Assassin import Assassin
from Ambassador import Ambassador
from Captain import Captain
from Contessa import Contessa
import random
class Deck() :

    def __init__(self) :
        self.__len = 15
        j = 0
        k = 0
        not_deck = []
        while j< 5 :
            i = 0
            while i < 3 :
                if k == 0 :
                    not_deck.append(Duke())
                if k == 1 :
                    not_deck.append(Assassin())
                if k == 2 :
                    not_deck.append(Ambassador())
                if k == 3 :
                    not_deck.append(Captain())
                if k == 4 :
                    not_deck.append(Contessa())
                if i == 2 :
                    k += 1
                i += 1
            j += 1

        deck = []
        l = 15
        #Here we shuffle the deck
        while l > 0 :
            x = random.randint(0,l-1)
            l -= 1
            deck.append(not_deck[x])
            not_deck.pop(x)

        self.__deck = deck
      
    @property
    def len(self) :
        return self.__len
    #@len.setter
    def len_setter(self, i) :
        if self.len > 0 :
            if i== -1 :
                self.__len += i
            elif i== +1 :
                self.__len += i
            else :
                print("Sólo puedes quitar o agregar cartas al mazo de una a la vez")
        else :
            raise Exception("No puedes tener largo menor a cero")

    @property
    def deck(self) :
        return  self.__deck
    #@deck.setter
    def deck_setter(self, x, card) :
        new_deck = []
        if x != -1 :  #x = -1 means that you want to delete a card from the deck
            i = 0
            for i in range(len(self.deck)) :
                if i == x :
                    pass
                else : 
                    new_deck.append(self.deck[i])
            self.__deck = new_deck
            self.len_setter(-1)       
        else :
            if len(self.deck) <15 :
                i = 0
                for i in range(len(self.deck)) :
                    new_deck.append(self.deck[i])
                
                if card != 0 : #If someone wants to add a card back to the deck at the bottom of the deck
                    new_deck.append(card)
                #Else the deck is ready
                self.__deck = new_deck
                self.len_setter(+1)
            
            else :
                print("No pueden haber más de 15 cartas en el mazo")
                self.__deck = self.deck

    def give_card(self) :
        #Takes card from the deck
        #We take the card on position 0, because its the card "on top" of the deck
        card = self.deck[0]
        self.deck_setter(x = 0, card = 0)
        return card 

    def put_back_cards(self, i) :
        #Puts a card back in the deck (at the end of it)
        c = 0
        while c == 0 :
            if i == 0 :
                card = Duke()
                self.deck_setter(-1 ,card)
            elif i == 1:
                card = Assassin()
                self.deck_setter(-1 ,card)
            elif i == 2 :
                card = Ambassador()
                self.deck_setter(-1 ,card)
            elif i == 3 :
                card = Captain()
                self.deck_setter(-1 ,card)
            elif i == 4 :
                card = Contessa()
                self.deck_setter(-1 ,card)
            c = 1
        return 0 

    def shuffle(self) :
        new_deck = []
        l = self.len
        while l > 0 :
            x = random.randint(0,l-1)
            l -= 1
            new_deck.append(self.deck[x])
            self.deck_setter(x, card = 0)
        #Only in this scenario its ok to access the variable directly, because the deck is a new one after the added cards.
        self.__deck = new_deck






