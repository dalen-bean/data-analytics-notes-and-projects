#Create the deck of card
import random

class Card():
    def __init__(self, suit, face, value):
        self.suit = suit
        self.face = face
        self.val = value
        
    def __str__(self):
        return self.face + 'of' + self.suit, 'value: ' + str(self.val)
        
class DeckOfCards():
    def __init__(self, deck=[]):
        self.deck = deck
        self.suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
        self.faces = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        self.values = [2,3,4,5,6,7,8,9,10,10,10,10,11]
        self.play_idx = 0
        
        for suit in self.suits: #add a value to the card
            i=0
            for i in range(len(self.faces)):
                self.deck.append(Card(suit, self.faces[i], self.values[i]))
            
        def __str__(self):
            return self.face + 'of' + self.suit, 'value: ' + str(self.val)        
        
        
    def shuffleDeck(self):
        random.shuffle(self.deck)
        
    def printDeck(self):
        for card in self.deck:
            print(card.face, 'of', card.suit, end = ',')
            
    def getCard(self):
        self.play_idx += 1
        return self.play_idx - 1
        
    def draw(self):
            print (DeckOfCards([self.play_idx]))     
     
        
cards = []
user_card = []
user2_card = []

deck = DeckOfCards(cards)
deck.printDeck()
deck.shuffleDeck()
print('----------------')
deck.__str__()

deck.getCard()
deck.draw()

