from coup import Coup
from time import sleep
"""READ BEFORE USE"""
""""
coup.py tiene 17 'posibles problemas' porque la instancia str no tiene ciertos atributos. Sin embargo, cada uno de 
estos escenarios fueron revisados y se implementaron condiciones que los evitan, por lo que no deberían causar 
ningún problema al correr el progama. Estos 'errores' vienen dados por la forma en que guardamos a cada jugador, 
pues metemos un str vacío en aquella lista, de forma que los jugadores correspondan a su posición en la lista. 
Es decir, el jugador 1 esté en la posición 1,..., el jugador i esta en la posición i y así para cualquier número 'n'. 
Nos pareció mejor hacerlo de esta manera, pues es mucho más simple de entender y manejar cuando se está programando. 
Espero no sea ningún inconveniente :)
"""

def main() :
    print("Bienvenido a Coup!!")
    
    
    players = (input("Ingrese el número de jugadores (3 o 4) :\n"))

    if players != '3' and players != '4' :
        raise Exception("El juego sólo está diseñado para 3 o 4 jugadores")
    players = int(players)
    g = Coup(players)
    while True :
            if g.game_end() == False :
                t = 1
                while t <= players :
                    print("Turno del jugador %d"%(t))
                    sleep(2)
                    g.print_turn(t) #Doesn´t print the whole turn, it just prints the state of the game while the player t is playing
                    sleep(3)
                    g.turn(t) 
                    print("\n")
                    if t == players : #It means that turn is over, so we print the log of the turn
                        sleep(2)
                        print("\n\nSe acabó el turno")
                        sleep(2)
                        print("Registro de lo que sucedió :")
                        l = g.log
                        for phrase in l :
                            print(phrase)
                            sleep(2)
                        g.log_changer(phrase = " ")
                        print("\n\n\n")
                        sleep(2)

                    t += 1

            else :
                return 0




if __name__ == "__main__" :
    main()