import random


    
class Card():
    def __init__(self, suit, face):
        self.suit = suit
        self.face = face
        
class DeckOfCards():
    def __init__(self, deck=[]):
        self.deck = deck
        
    def shuffleDeck(self):
        random.shuffle(self.deck)
        
    def printDeck(self):
        for card in self.deck:
            print(card.face, 'of', card.suit, end = ',')
            
    def deal_card(self, card):
        return Card()
        
            
suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
faces = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
value = [2,3,4,5,6,7,8,9,10,10,10,10,11]
play_idx = 0

cards = []
for suit in suits:
    for face in faces:
        cards.append(Card(suit, face))
        
deck = DeckOfCards(cards)

deck.printDeck()
deck.shuffleDeck()
print('----------------')
deck.printDeck()

#Game function

# score = 0
# dealer_score = random.randint(16, 32)

# for face in faces:
#     welcomeMessage = input("Press 'Enter' to play or type 'pass' to pass: ")
#     if welcomeMessage == "":
#         x = float(random.choice(faces))
#         print ((x), "of", random.choice(suits)) # get rid of float on x and write if x = 'king' x=10 ...
#         if score < 21:
#             print('your have', x + score, "points" )
#             if score > 21 : 
#                 print('better luck next time')
            
#     elif score > 21:
#         print ('better luck next time.')
#         break 
    
#     elif welcomeMessage == "pass":
#         print("Your Score is ", score)
#         print ("Dealer's score is", dealer_score)
#         if dealer_score > 21:
#             print("You Win")
#         elif score >= dealer_score: #Fix the if statements to follow the black jack rules
#             print("You Win")
#         else: 
#             print("Dealer Wins")
#         break
#     score += x

# # print (random.choice(faces), "of", random.choice(suits))