#1. Importamos random para la selección ficticia de las cartas, tanto del jugador (player) como de la banca (dealer).

import random

#2. Creamos las variables para todas las cartas de la baraja de poker:
    #suits = los diferentes palos. Para los palos utilizamos su correspondiente unicode a efectos de visualización.
    #ranks = las diferentes cartas
    #cartas = asignamos a cada carta su correspondiente valor. Habrá que tener en cuenta que el AS puede valer 1 o 11.

suits = ('\U00002665', '\U00002666', '\U00002660', '\U00002663')
ranks = ('Dos', 'Tres', 'Cuatro', 'Cinco', 'Seis', 'Siete', 'Ocho', 'Nueve', 'Diez', 'Jota', 'Dama', 'Reina', 'As')
values = {'Dos':2, 'Tres':3, 'Cuatro':4, 'Cinco':5, 'Seis':6, 'Siete':7, 'Ocho':8, 'Nueve':9, 'Diez':10, 'Jota':10,
         'Dama':10, 'Reina':10, 'As':11}

#Utilizamos la variable True para controlar el juego. Mientras sea True, el juego sigue.
playing = True

#Empezamos con la creación de las clases.


#3. Creamos la clase Card/Carta que necesita dos atributos:
    #el método init/iniciar. Incluirá las variables palos y las cartas en si.
    #el método str para devolver las diferentes cartas que tiene cada participante unidas por un 'de'. Ejemplo: Diez de Diamantes.

class Card:
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return self.rank + ' de ' + self.suit

    
#4. Creamos la clase Deck/Baraja para guardar todas las cartas de la baraja a medida que se vayan mostrando. Tiene 4 atributos:
    #método init/iniciar la baraja:
        #empezará con una lista vacia a la que se irán añadiendo las cartas
    #método str para añadir las cartas cada vez que se pidan
        #empezara como una variable vacia
    #método shuffle que lo hace es barajar las cartas
    #método deal que lo hace es quitar una carta de la baraja y mostrarla al jugador que la pide, una a una.
    
class Deck:
    
    def __init__(self):
        self.deck = []  
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))
    
    def __str__(self):
        deck_comp = '' 
        for card in self.deck:
            deck_comp += '\n' + card.__str__() 
        return 'La baraja tiene ' + deck_comp
            
    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        single_card = self.deck.pop()
        return single_card

#5. Creamos la clase Hand/Mano para calcular el valor de las cartas que tiene cada jugador en su respectivo turno. Tiene 3 atributos:
    #método init/iniciar
        #las cartas empiezan como una lista vacia
        #el valor empieza con 0
        #el número de as empieza con 0
    #método add_card/añadir carta para sumar la cantidad cada vez que se muestre una carta y además sumar cuantas veces se ha mostrado el as
    #método adjust_for_ace para siempre mantenernos por debajo de 21. Por ejemplo, si el jugador tiene 19 y sale un as, en vez de 10, su valor sera de 1.

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
    
    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1
    
    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1
            
#6. Definimos la función de hit/pedir carta para añadir la carta que se pide.

def hit(deck,hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

#7. Definimos la función para hit or stand; que le pregunta al jugador si quiere seguir jugando/quiere otra carta o plantarse.
    #si decide optar por "o": le damos una carta
    #si decide optar por "p" se planta y le toca el turno a la banca de jugar.
    #si no, le decimos que no entiende lo que quiere decir y que introduzca una opción válida.

def hit_or_stand(deck,hand):
    global playing
    
    while True:
        x = input("\nQuieres otra carta o plantarte? Presiona 'o' o 'p': " )
        
        if x[0].lower() == 'o':
            hit(deck,hand)

        elif x[0].lower() == 'p':
            print("\nEl jugador se planta. Es el turno de la banca.")
            playing = False

        else:
            print("\nNo te he entendido. Escribe de nuevo 'o' o 'p': ")
            continue
        break

#8. Definimos la función para enseñar las cartas cuando empieza la partida y y además para que sea más fácil, imprimimos la suma de las cartas al jugador. De esta manera su decisión será más rápida.
    #Tenemos en cuenta que:
        #la primera carta de la banca nunca se enseña
        #las cartas del jugador siempre son visibles

def show_some(player,dealer):
    print("\nLas cartas de la banca son: ")
    print("carta oculta")
    print(' ', dealer.cards[1])
    print("\nTus cartas son: ", *player.cards, sep= '\n')
    print("La suma de tus cartas es = ", player.value)

#9. Definimos la función para enseñar todas las cartas una vez banca y jugador ya hayan acabado su jugada.

def show_all(player,dealer):
    print("\nLas cartas de la banca son: ", *dealer.cards, sep="\n")
    print("La suma de las cartas de la banca es =",dealer.value)
    print("\nTus cartas son : ", *player.cards, sep= '\n')
    print("La suma de tus cartas es = ", player.value)

#10. Definimos una función para cada uno de los escenarios posibles funciones para todos los escenarios posibles.
    #El jugador pierde porque se pasa de 21.
    #El jugador gana porque se ha plantado y la banca tiene menos valor que el jugador.
    #El jugador gana porque la banca se ha pasado.
    #El jugador pierde porque se ha plantado y la banca tiene más valor que el jugador.
    #Hay empate

def player_busts(player,dealer):
    print("\n¡Has PERDIDO! Te has pasado de 21.")

def player_wins(player,dealer):
    print("\n¡Has GANADO! La suma de la banca es menor que la tuya.")
    
def dealer_busts(player,dealer):
    print("\n¡Has GANADO! La banca se ha pasado de 21.")
    
def dealer_wins(player,dealer):
    print("\n¡Has PERDIDO! La suma de la banca es mayor que la tuya.")
    
def push(player,dealer):
    print("\nHay EMPATE.")    

    
#11. Una vez definidas las funciones, empezamos a definir el juego en si. 

while True:
    # Creamos el título del juego
    print("\n\nBienvenido al Blackjack.")
    
    # Creamos y barajamos la baraja.
    deck = Deck()
    deck.shuffle()
    
    # Damos las dos cartas a la banca y al jugador
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
      
    # Mostramos las cartas, del dealer solo una
    show_some(player_hand, dealer_hand)
    
    while playing:  
        
        # Preguntamos si quiere otra carta o plantarse
        hit_or_stand(deck, player_hand)
        
        # Mostramos la carta que se va dando al jugador cuando se le da otra.
        show_some(player_hand,dealer_hand) 
        
        # Si el jugador se pasa de 21, pierde y se acaba el juego
        if player_hand.value >21:
            player_busts(player_hand, dealer_hand)

            break

    # Si el jugador no se pasa de 21 y se planta, la banca juega hasta que tiene 17. Llegados a este punto, está obligada a plantarse.
    if player_hand.value <= 21:
        
        while dealer_hand.value <17:
            hit(deck, dealer_hand)
    
        # Mostramos todas las cartas una vez que la banca se haya plantado.
        show_all(player_hand,dealer_hand)
        
        # Aplicamos los diferentes escenarios ya explicados.
        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand)

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand)

        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand)

        else:
            push(player_hand,dealer_hand)
        

   
#12. Por último preguntamos si quiere al jugador si quiere volver a jugar o no. En caso de que no responda 's', se acaba el juego.

    new_game = input("\n¿Quieres jugar de nuevo? Presiona 's' o 'n': ")
    if new_game[0].lower() == 's':
        playing = True
        continue
    else:
        print('\n¡Nos vemos! ')

        break