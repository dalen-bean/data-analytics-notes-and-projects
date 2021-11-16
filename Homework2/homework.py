import random

#Variables lists and Dictionaries

suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
faces = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
          '9': 9, '10': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}
          
playing =  True

#Classes

class Card():
    
    def __init__(self, suit, face):
        self.suit = suit
        self.face = face
        
    def __str__(self):
        return self.face + ' of ' + self.suit
        
        
class Deck():
    
    def __init__(self):
        self.deck = []
        
        for suit in suits: 
            for face in faces:
                self.deck.append(Card(suit, face))
            
    def __str__(self):
        deck1 = ''
        for card in self.deck:
            deck1 += "\n" + card.__str__()
        return "The deck has: " + deck1
        
    def shuffleDeck(self):
        random.shuffle(self.deck)
        
    def printDeck(self):
        for card in self.deck:
            print(card.face, 'of', card.suit, end = ',')
            
    def draw(self):
        one_card = self.deck.pop()
        return one_card
        
class PlayerHand:
    
    def __init__(self):
        self.cards = []
        self.value = 0
    
    def add_card(self, card):  
        self.cards.append(card)
        self.value += values[card.face]
      

#Game Functions

def hit(deck, hand):
    hand.add_card(deck.draw())

    
def hit_or_pass(deck, hand):   # hit or pass
    global playing

    while True:
        ask = input("\nEnter 'h' to hit or 'p' to pass: ")

        if ask[0].lower() == 'h':
            hit(deck, hand)
        elif ask[0].lower() == 'p':
            print("Player passes, Dealer is playing.")
            playing = False
        else:
            print("Please enter 'h' to hit or 'p' to pass: ")
            continue
        break
    
#Show your starting hand and dealers's first card 

def show_first_card(player, dealer):
    print("\nDealer's Hand: Hidden card, ", dealer.cards[1])
    print("\nYour Hand: ", *player.cards, sep='\n')
    print("You have ", player.value, "points.")

#Show everyone's cards 
    
def show_all(player, dealer): 
    print("\nDealer's Hand: ", *dealer.cards, sep='\n ')
    print("Dealer's Score =", dealer.value)
    print("\nYour Hand Hand: ", *player.cards, sep='\n ')
    print("Your Score =", player.value)

# Game endings    
def player_busts(player, dealer):
    print("You bust, Dealer Wins!")

def player_wins(player, dealer):
    print("You Win!")

def dealer_busts(player, dealer):
    print("Dealer busts, you win!")

def dealer_wins(player, dealer):
    print("Sorry, Dealer Wins")

def tie(player, dealer):
    print("Its a tie!")
 
# Playing BlackJack
    
while True:
    print("Welcome to BlackJack!")
    
    #Dealing Cards
    
    deck = Deck()
    # deck.printDeck()  #Print the original deck
    
    deck.shuffleDeck()
    # print("\nShuffle Deck------------")
    # deck.printDeck() #Print the shuffled deck
    
    player_hand = PlayerHand()
    player_hand.add_card(deck.draw())
    player_hand.add_card(deck.draw())
    
    dealer_hand = PlayerHand()
    dealer_hand.add_card(deck.draw())
    dealer_hand.add_card(deck.draw())

    show_first_card(player_hand, dealer_hand)
    
    #Game Logic
    
    while playing:
        
        hit_or_pass(deck, player_hand)
        show_first_card(player_hand, dealer_hand)
        
        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand)
            break
        
    if player_hand.value <= 21:
        
        while dealer_hand.value < 17:
            hit(deck, dealer_hand)
            
        show_all(player_hand, dealer_hand)
        
        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand)
        
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand)
        
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand)
        
        elif player_hand.value > 21:
            player_busts(player_hand, dealer_hand)
            
        elif dealer_hand.value == player_hand.value:
            tie(player_hand, dealer_hand)
    
    #Start a new game or exit the loop
            
    new_game = input("\nDo you want to play again Enter 'y' for yes or 'n' for no: ")
    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print("\nThanks for playing!")
        break