import random

class Card(): #Create cards
    def __init__(self, suit, face, value):
        self.suit = suit
        self.face = face
        self.val = value
        
    def __str__(self):
        return self.face + 'of' + self.suit, 'value: ' + str(self.val)
        
class DeckOfCards(): #Create a deck of cards
    def __init__(self, deck=[]):
        self.deck = deck
        self.suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
        self.faces = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        self.values = [2,3,4,5,6,7,8,9,10,10,10,10,11]
        self.play_idx = 0
        
        for suit in self.suits: #append a value to the cards
            i=0
            for i in range(len(self.faces)):
                self.deck.append(Card(suit, self.faces[i], self.values[i]))
            
        # for suit in suits:
        #     for face in faces:
        #         self.deck.append(Card(suit, face))
        
    def shuffleDeck(self): #Shuffle the Cards
        random.shuffle(self.deck)
        
    def printDeck(self): #Print the Entire Deck of Cards
        for card in self.deck:
            print(card.face, 'of', card.suit, end = ',')
            
    def getCard(self): #Draw cards by increasing play_idx by 1
        self.play_idx += 1
        return self.play_idx - 1
            
cards = []
player_hand = []
dealer_hand = []

deck = DeckOfCards(cards)
deck.printDeck()
deck.shuffleDeck()
print('----------------')
deck.printDeck

player_score = 0
dealer_score = 0

while len(player_hand)< 2:
    player_card = random.choice(deck)
    player_hand.append(player_card)
    
    player_score += player_card.val

    print("Your hand: ")
    #figure out how to print a single card
    print("Your Score is ", player_score)
    
    input()
    
    dealer_card = random.choice(deck)
    dealer_hand.append(dealer_card)
    
    dealer_score += dealer_card.val
    
    print("Dealer's hand:")
    if len(dealer_hand) == 1:
        #print single cards
        print("Dealer's Score: ", dealer_score)
    else:
        #print both cards
        print("Dealer's Score ", dealer_score - dealer_hand[-1].val)
        
    input()
    
    if player_score == 21:
        print("PLAYER HAS A BLACKJACK!!!!")
        print("PLAYER WINS!!!!")
        quit()
        
        
    
    
# deck = DeckOfCards(cards)
# deck.printDeck()
# deck.shuffleDeck()
#print('----------------')
# deck.printDeck

deck1 = DeckOfCards()
deck1.shuffleDeck 
deck1.printDeck()

# from deckofcards import *  how to import everything from one file
