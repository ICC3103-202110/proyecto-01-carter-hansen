from player import Player
from deck import Deck
import random
from time import sleep
class Coup() :
    def __init__(self, number) :
        players = ["empty"] #Put an elment in there so that players[1] is the player1 and so on.
        self.__number_players = number + 1  #Because of the empty element
        player_plays = ["empty"]
        i = 1
        self.deck = Deck() #No need to make it private
        while i<= number :
            influences = []
            plays = []

            card1 = self.deck.give_card()
            influences.append(card1)
            plays.append(card1.attack())

            card2 = self.deck.give_card()
            influences.append(card2)
            plays.append(card2.attack())

            player_plays.append(plays)

            player_i = Player(n = i, coin  = 2, influence = influences)
            players.append(player_i)

            i+=1
        self.__allplays = ["Impuesto","Asesinato","Extorsión","Cambio", "AyudaExtranjera","Ingresos"]
        self.__general_plays = ["AyudaExtranjera", "Ingresos"]
        self.__plays = player_plays
        self.__players = players
        self.__log = []
        self.__NUMBERS = ['1','2','3','4','5','6']
        
    @property
    def players(self):
        return self.__players

    @property
    def plays(self) :
        return self.__plays
    def plays_setter(self, player) :
        new_plays = []
        for card in self.players[player].influence :
            if card == "empty" :
                pass
            new_plays.append(card.attack())
        self.__plays[player] = new_plays

    @property
    def number_players(self) :
        return self.__number_players

    @property
    def general_plays(self) :
        return self.__general_plays

    @property
    def log(self) :
        return self.__log

    def log_changer(self, phrase) :
        if phrase == " ":
            self.__log = []
        else:
            self.__log.append(phrase)
    @property
    def allplays(self):
        return self.__allplays

    @property
    def NUMBERS(self) :
        return self.__NUMBERS

    def turn(self, i) :
        print("\n")
        if self.players[i].status == 1 :
            print("El jugador %d ya perdió. Siguiente turno"%(i))
            return 0    
        elif self.do_coup(i) == 1 :
            return True
        else :
            turn_plays = [["empty"]]
            print("Estas son tus posibles acciones :")
            for j in self.general_plays :
                turn_plays.append(j)
            for j in self.plays[i] :
                turn_plays.append(j)
            flag = 0
            while flag == 0:
                self.show_plays(turn_plays)
                action = input("¿Cuál de estas acciones deseas realizar?\n")
                action = action.capitalize()
                for j in (self.allplays) :
                    if (action == j) or (action in self.NUMBERS) :
                        if action in self.NUMBERS :
                            action = self.allplays[int(action)-1]

                        print("J%d está por realizar la acción %s"%(i, action))
                        sleep(2)
                        if action == "Asesinato"  :
                            if self.players[i].coin < 3 :
                                print("No tienes las monedas para realizar un asesinato.")
                                sleep(2)
                                self.turn(i)

                        if action in self.general_plays :   
                            print("Elegiste una acción general, por lo que no es desafiable")

                        challenger = None
                        if action not in self.general_plays :
                            challenger = self.find_challenger(i)
                        if self.challenge(i, action, challenger) == 1 :
                            if (action =="Ingresos") or (action == "Cambio" ) or (action == "Impuesto") :
                                print("Elegiste una acción que no es contraatacable")
                            counterattacker = None
                            if (action !="Ingresos") and (action != "Cambio") and (action != "Impuesto") :
                                counterattacker = self.find_counterattacker(i)
                            counter = self.counters(action)
                            if self.counterattack(counterattacker, counter, i, action) == 0 :
                                pi = "J" + str(i)
                                if action == "Asesinato" :
                                    self.checkplay(i, action)
                                    killed = 0
                                    flag = 0
                                    while flag == 0 :
                                        killed = input("¿A que jugador deseas robarle 2 monedas?(Ej : J1)")
                                        for p in self.players :
                                            if p == "empty" :
                                                pass
                                            else :
                                                if p.name != i and p.name == int(killed[1]):
                                                    if self.player_lost(p.name) == 1 :
                                                        print("Este jugador ya perdió, por lo que no puedes 'matar' ninguna de sus influencias\nElige otro jugador.Elige otro.") 
                                                    else : 
                                                        log = self.assassin(i, p.name)
                                                        flag = 1
                                    phrase = pi + log
                                    self.log_changer(phrase)
                                    return True

                                elif (action =="AyudaExtranjera" ) or (action=="Ingresos") or (action == "Impuesto" ) :
                                    self.checkplay(i, action) 
                                    return True

                                elif action == "Extorsión" :
                                    stolen = 0
                                    flag = 0
                                    while flag == 0 :
                                        stolen = input("¿A que jugador deseas robarle 2 monedas?(Ej : J1)")
                                        for p in self.players :
                                            if p == "empty" :
                                                pass
                                            else :
                                                if p.name != i and p.name == int(stolen[1]):
                                                    if p.coin >= 2 :
                                                        s = 2
                                                        p.coin_setter(-2) 
                                                        self.players[i].coin_setter(+2)
                                                        log = " uso extorsion en "+stolen+" y gano "+str(s)+" monedas."
                                                        phrase = pi + log
                                                        self.log_changer(phrase)
                                                        return True
                                                    elif p.coin == 1 :
                                                        s = 1
                                                        p.coin_setter(-1) 
                                                        self.players[i].coin_setter(+1)
                                                        log = " uso extorsion en "+stolen+" y gano "+str(s)+" monedas."
                                                        phrase = pi + log
                                                        self.log_changer(phrase)
                                                        return True
                                                    else :
                                                        s = 0
                                                        print("El jugador %d no tiene monedas\nComo no hay nada para robar, no recibes monedas"%(p.name))
                                                        log = " uso extorsion en "+stolen+" y gano "+str(s)+" monedas."
                                                        phrase = pi + log
                                                        self.log_changer(phrase)
                                                        return True
                                
                                elif action == "Cambio" : 
                                    log = self.exchange(i)
                                    phrase = pi + log
                                    self.log_changer(phrase)
                                    return True 
                            else :
                                # self.counterattack(counterattacker, counter) == 1 
                                #which means counterattack was successful
                                if action == "Asesinato" or action == '2' :
                                    self.checkplay(i, action) #This makes player pay the coins anyway
                                return 0
                        else :
                            #Challenge was successful, so the turn ends (player already turned around a card)
                            return 0    
                if action in self.allplays or action in self.NUMBERS:
                    (print("No puedes realizar esta acción ahora mismo.\n"))
                else :
                    print("%s no es una acción"%(action))

                sleep(2)

    def checkplay(self, player, a):
        if a == "Ingresos" or a == '6':            
            self.players[player].coin_setter(1)
            log = " used Income and got 1 coin"
            
        elif a == "AyudaExtranjera" or a == '5':
            self.players[player].coin_setter(2)
            log = " uso ayuda extranjera y gano 2 monedas"
           
        elif a == "Asesinato" or a == '2':
            self.players[player].coin_setter(-3)
            log = " uso asesinato y pago 3 monedas"
            
        elif a == "Impuesto" or a == '1':
            self.players[player].coin_setter(3)
            log = " uso impuesto y gano 3 monedas"

        pi = "J"+str(player)
        phrase = pi + log
        self.log_changer(phrase)
        return 1

    def check_influences(self, player) : 
        #Returns how many cards a player has left. Its useful for printing the state of the game
        i = 0
        for card in self.players[player].influence :
            if card.status == 0 :
                i += 1
        return i

    def print_turn(self, i) :
            for j in self.players :
                cards = []
                if j == "empty":
                    pass
                else: 
                    n = j.name
                    number = (self.check_influences(n))
                    if n == i :
                        if self.player_lost(n) == 1 :
                            print("J"+str(i)+" ya perdio!" )
                        else :
                            c = input("¿Quieres ver tus cartas?(si, no) : \n")
                            if c == "si" or c =="Si" or c == "SI" or c == "sí":
                                if self.players[n].influence[0].status == 1 :
                                    print("J%d tiene %d carta boca abajo (%s (expuesta), %s) y %d monedas"%(n, number, self.players[n].influence[0].name, self.players[n].influence[1].name, self.players[n].coin))
                                elif self.players[n].influence[1].status == 1 :
                                    print("J%d tiene %d cartas boca abajo (%s, %s(expuesta)) y %d monedas"%(n, number, self.players[n].influence[0].name, self.players[n].influence[1].name, self.players[n].coin))
                                else :
                                    print("J%d tiene %d cartas boca abajo (%s, %s) y %d monedas"%(n, number, self.players[n].influence[0].name, self.players[n].influence[1].name, self.players[n].coin))

                            
                            else :
                                print("J%d tiene %d cartas boca abajo y %d monedas"%(n, number, self.players[n].coin))
                    else :
                        if self.player_lost(n) == 1 :
                            print("J%d ya perdio!"%(n))
                        else :
                            for x in range(len(self.players[n].influence)) :
                                if self.players[n].influence[x].status == 1 :
                                    position = x
                                    name = self.players[n].influence[x].name
                                    data = (position, name)
                                    cards.append(data)
                            
                            if len(cards) == 0 :
                                print("J%d tiene %d cartas boca abajo y %d monedas"%(n, number, self.players[n].coin))
                            elif cards[0][0] == 0 :
                                print("J%d tiene %d cartas escondidas (%s a sido revelada) y %d monedas"%(n, number, self.players[n].influence[0].name, self.players[n].coin))
                            elif cards[0][0] == 1 :
                                print("J%d tiene %d cartas escondidas (%s a sido revelada) y %d monedas"%(n, number, self.players[n].influence[1].name, self.players[n].coin))
                            else :
                                print("J%d tiene %d cartas escondidas (%s, %s han sido reveladas) y %d monedas"%(i, number, self.players[n].influence[0].name, self.players[n].influence[1].name, self.players[n].coin))
                    sleep(1.25)
    
    def plays_updater(self, player) :
        for i in (self.players[player].influence) :
                for j in self.plays[player] :
                    if i.status == 1 and i.attack() == j:
                        self.plays[player].remove(j)

    def show_plays(self, turn_plays) :
        x = 1
        for i in self.allplays :
            if i in turn_plays :
                print("%d. %s"%(x, i))
                x += 1
            else :
                print("%d. %s (bluff)"%(x, i))
                x += 1

    def show_cards(self, player) :
        print("Las cartas del jugador %d son :"%(player))
        for i in self.players[player].influence :
            if i.status == 0 :
                print(i.name)

    def find_counterattacker(self, player) :
        counterattackers = []
        for i in range(len(self.players)) :
            if i == player or i == 0 :
                pass
            elif self.players[i].status == 0 :
                counteratt = input("Jugador %d ¿Deseas contraatacar la acción del jugador %d? (si, no)\n" % (i, player))
                if counteratt == "si" or counteratt == "Si" :
                    counterattackers.append(i)

        if len(counterattackers) == 0 :
            print("No hay contraatacantes")
            sleep(2)
            return None

        x = random.randint(0, len(counterattackers)-1)
        counterattacker = counterattackers[x]
        print("El jugador %d ha decidido contraatacar al jugador %d"%(counterattacker, player))
        sleep(2)
        return counterattacker

    def counterattack(self, counterattacker, counter, countered, action) :
        if counterattacker == None:
            return 0
        if counter == None :
            return 0
        print("\nPara el contraataque del jugador %d :"%(counterattacker))
        sleep(2)
        challenger = self.find_challenger(counterattacker)
        if challenger == None :
            if action in self.NUMBERS :       #Shouldn't happen, but sounds like good practice to check anyways
                action = self.allplays[int(action)-1]
            print("Contraataque exitoso")
            sleep(2)
            phrase = "J%d uso la accion %s, pero J%d lo contraataco"%(countered, action, counterattacker)
            self.log_changer(phrase)
            return 1
        else :
            print("\n")
            print("J%d desafía el contraataque"%challenger)
            sleep(2)
            for i in self.players[counterattacker].influence :
                if i.counter_attack() == counter :
                    self.player_gets_new_card(counterattacker, counter)
                    print("Desafío fallido\n")
                    sleep(2)
                    phrase = "J%d fue desafiado por J%d por la accion %s pero fallo"%(counterattacker, challenger, counter)
                    self.log_changer(phrase)
                    print("El jugador %d debe elegir que carta dar vuelta" % (challenger))
                    flag = 0
                    while flag == 0 :
                        self.show_cards(challenger)
                        card = input("¿Cuál de tus cartas deseas dar vuelta? (Ingresa su nombre)\n")
                        card = card.capitalize()
                        for i in (self.players[challenger].influence) :
                            if i.name == card and i.status == 0:
                                i.status_setter(1)
                                phrase = "J%d perdio la influencia %s"%(challenger,i.name)
                                self.log_changer(phrase)
                                if self.player_lost(challenger) == 1 :
                                    phrase = "J%d ya perdio!"%(challenger)
                                    self.log_changer(phrase)
                                    return 1
                                self.plays_updater(challenger)
                                return 1
                        print("No tienes la carta",card)
                        sleep(2)

            print("Desafío exitoso")
            print("El jugador %d debe elegir que carta dar vuelta" % (counterattacker))
            phrase = "J%d fue desafiado J%d por la accion %s y gano"%(counterattacker, challenger, counter)
            self.log_changer(phrase)
            flag = 0
            while flag == 0 :
                self.show_cards(counterattacker)
                card = input("¿Cuál de tus cartas deseas dar vuelta? (Ingresa su nombre)\n")
                card = card.capitalize()
                for i in (self.players[counterattacker].influence) :
                    if i.name == card :
                        i.status_setter(1)
                        phrase = "J%d perdio la carta %s"%(counterattacker,i.name)
                        self.log_changer(phrase)
                        if self.player_lost(counterattacker) == 1 :
                                return 1
                        self.plays_updater(counterattacker)
                        return 0
                print("No tienes la carta",card)
                sleep(2)

    def counters(self, play) :
        counter = 0
        if play == "Asesinato" or play == '2' :
            counter = "BloquearAsesinato"

        elif play == "AyudaExtranjera" or play == '5':
            counter = "BloquearAyudaExtranjera"

        elif play == "Extorsión" or play == '3':
            counter = "BloquearExtorsión"

        if counter != 0 :
            return counter
        else : 
            return None

    def player_gets_new_card(self, player, action) :
        if action in self.NUMBERS :                 #Again, it shouldn't happen, but we'll check just in case
            action = self.allplays[int(action) - 1]
        card1 = self.players[player].influence[0]
        card2 = self.players[player].influence[1] 
        if card1.attack() == action or card1.counter_attack() == action :
            self.deck.put_back_cards(card1.i)

            new_card1 = self.deck.give_card()
            
            self.players[player].influence_setter(new_card1, card2)
            self.plays_setter(player)
            return 0

        elif card2.attack() == action or card2.counter_attack() == action :
            self.deck.put_back_cards(card2.i)
            
            new_card2 = self.deck.give_card()

            self.players[player].influence_setter(card1, new_card2)
            self.plays_setter(player)
            return 0

    def find_challenger(self, player) :
        challengers = []
        for i in range(len(self.players)) :
            if i == player or i == 0 :
                pass
            elif self.players[i].status == 0 :
                challenge = input("Jugador %d ¿Deseas desafiar la acción del jugador %d?\n" % (i, player))
                if challenge == "si" or challenge == "Si" :
                    challengers.append(i)
        if len(challengers) == 0 :
            print("No hay desafiantes")
            sleep(2)
            return None
        x = random.randint(0, len(challengers)-1)
        challenger = challengers[x]
        print("El jugador %d ha desafiado al jugador %d"%(challenger, player))
        sleep(2)
        return challenger
        
    def challenge(self, player, action, challenger) :
        if challenger == None :
            return 1
        print("\n")
        for j in self.plays[player] :
            if j == action or action in self.NUMBERS:  
                if action in self.NUMBERS :                #Shouldn't happen, but seems like good practice to check anyways
                    action = self.allplays[int(action)-1]        
                self.player_gets_new_card(player, action)
                self.plays_setter(player)
                print("Desafío fallido")

                print("El jugador %d debe elegir que carta dar vuelta" % (challenger))
                phrase = "J%d fue desafiado por J%d por la accion %s pero fallo"%(player, challenger, action)
                self.log_changer(phrase)
                flag = 0
                while flag == 0 :
                    self.show_cards(challenger)
                    card = input("¿Cuál de tus cartas deseas dar vuelta?(Ingresa su nombre)\n")
                    card = card.capitalize()
                    for i in (self.players[challenger].influence) :
                        if i.name == card and i.status == 0:
                            i.status_setter(1)
                            phrase = "J%d perdio la carta %s"%(challenger,i.name)
                            self.log_changer(phrase)
                            if self.player_lost(challenger) == 1 :
                                return 1
                            self.plays_updater(challenger)
                            return 1
                    print("No tienes la carta",card)
                    sleep(2)

        print("Desafío exitoso")
        print("El jugador %d debe elegir que carta dar vuelta" % (player))
        phrase = "J%d fue desafiado por J%d por la accion %s y gano"%(player, challenger, action)
        self.log_changer(phrase)
        flag = 0
        while flag == 0 :
            self.show_cards(player)
            card = input("¿Cuál de tus cartas deseas dar vuelta?(Ingresa su nombre)\n")
            card = card.capitalize()
            for i in (self.players[player].influence) :
                if i.name == card :
                    i.status_setter(1)
                    phrase = "J%d perdio la carta %s"%(player,i.name)
                    self.log_changer(phrase)
                    if self.player_lost(player) == 1 :
                        phrase = "J%d quedo fuera del juego!"%(player)
                        self.log_changer(phrase)
                        return 1
                    self.plays_updater(player)
                    return 0
            print("No tienes la carta",card)
            sleep(2)

    def do_coup(self, player) :
            if self.players[player].coin < 10 :
                return 0
            print("Tienes 10 monedas! un golpe esta en proceso!.")
            self.players[player].coin_setter(-7)
            n = 0
            flag = 0
            while flag == 0 :
                n = (input("A que jugador quieres hacer el golpe? (Ej : J1)"))
                for p in self.players :
                    if p == "empty" :
                        pass
                    else :
                        if p.name != player and p.name == int(n[1]):
                            if self.player_lost(p.name) == 1 :
                                print("No puedes haer un golpe a un jugador que perdio.") 
                            else : 
                                flag = 1       
            phrase = "J%d sufrio un golpe a manos de %d!"%(n, player)
            self.log_changer(phrase)
            print("Has sido víctima de un golpe, por lo que tendrás que dar vuelta una carta")
            print("Estas son tus cartas :")
            flag = 0
            while flag == 0:
                self.show_cards(n)
                card = input("\n¿Cuál de tus cartas deseas dar vuelta? (Ingresa su nombre):\n")
                for i in (self.players[n].influence) :
                    if i.name == card :
                        i.status_setter(1)
                        phrase = "J%d perdio la carta %s"%(n,i.name)
                        self.log_changer(phrase)
                        self.plays_updater(n)
                        return 1
                print("No tienes la carta",card)
                sleep(2)
               
    def player_lost(self, player) :
        for card in self.players[player].influence :
            if card.status == 0 :
                return 0        #Still has at least one card left
        self.players[player].status_setter(1)
        return 1 #Player has lost.

    def game_end(self) :
        won = []
        for i in self.players :
            if i =="empty" :
                pass
            else :
                if i.status == 0 :
                    won.append(i.name)

        if len(won) == 1 :
            winner = won[0]
            return print("El juego se ha acabado.\nEl jugador %d es el ganador!!"% (winner))

        return False

    def assassin(self, attacker, attacked) :
        print("El J%d ha sido víctima de un asesinato  J%d. J%d debe elegir que carta dar vuelta" % (attacked, attacker, attacked))
        flag = 0
        while flag == 0 :
            self.show_cards(attacked)
            card = input("¿Cuál de tus cartas deseas dar vuelta?\n")
            card = card.capitalize()
            for i in (self.players[attacked].influence) :
                if i.name == card :
                    print("%s ha muerto"%(i.name))
                    i.status_setter(1)
                    self.plays_updater(attacked)
                    return "uso asesinar en J"+str(attacked)
            print("No tienes la carta",card)
            sleep(2)      

    def exchange(self, player) :
        all_cards = []
        card1 = self.players[player].influence[0]
        if card1.status == 0:
            all_cards.append(card1)
        card2 = self.players[player].influence[1]
        if card2.status == 0 :
            all_cards.append(card2)

        card3 = self.deck.give_card()
        all_cards.append(card3)

        card4 = self.deck.give_card()
        all_cards.append(card4)
        print("Acabas de sacar las dos primeras cartas del mazo")
        print(len(all_cards))
        for card in range(len(all_cards)) :

                if card+1 == (len(all_cards)-1) or card+1 == len(all_cards) :
                    print("%d. %s (nueva)"%(card+1, all_cards[card].name) )
                else :
                    print("%d. %s"%(card+1, all_cards[card].name) )
        while True :
            flag = 0
            while flag == 0 :
                x1= (input("Elige primera carta que quieres guardar :\n"))
                if x1 in self.NUMBERS : 
                    x1 = int(x1) - 1
                    if x1 >= 0 and x1 < len(all_cards) :
                        c1 = all_cards[x1]
                        print(c1.name,"guardado exitosamente")
                        break
                elif x1 not in self.NUMBERS :
                    x1 = x1.capitalize()
                    for element in all_cards :
                        if x1 == element.name  :
                            c1 = element
                            print(c1.name,"guardado exitosamente")
                            break
                    flag = 1
                if flag != 1:
                    print("Input inválido")
            if len(all_cards) == 4 :
                flag = 0
                while flag == 0 :
                    x2 = (input("Elige la segunda carta que quieres guardar :\n"))
                    if x2 in self.NUMBERS : 
                        x2 = int(x2) -1
                        if x2 >= 0 and x2 < len(all_cards) :
                            c2 = all_cards[x2]
                            print(c2.name,"guardado exitosamente")
                            break
                    elif x2 not in self.NUMBERS :
                        for element in all_cards :
                            x2 = x2.capitalize()
                            if x2 == element.name  :
                                c2 = element
                                print(c2.name,"guardado exitosamente")
                                break
                            flag = 1
                    if flag != 1:
                        print("Input inválido")
            else :
                c2 = 0
            
            self.players[player].influence_setter(c1, c2)
            self.plays_setter(player)
            if len(self.players[player].influence) == 2 :
                return " uso la carta embajador y cambio sus cartas"
            else :
                print("Ha habido un error. Necesito que ingreses tus cartas denevo")
