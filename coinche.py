import random

CARD_COLORS = ['C', 'D', 'H', 'S']
CARD_NUMBERS = ['7', '8', '9', 'J', 'Q', 'K', '10', 'A']
CARDS = ["C7", "C8", "C9", "CJ", "CQ", "CK", "C10", "CA",
 		 "D7", "D8", "D9", "DJ", "DQ", "DK", "D10", "DA", 
 		 "H7", "H8", "H9", "HJ", "HQ", "HK", "H10", "HA", 
 		 "S7", "S8", "S9", "SJ", "SQ", "SK", "S10", "SA"]

def randomCard():
	number = random.choice(CARD_NUMBERS)
	color = random.choice(CARD_COLORS)
	return number+color

def tester():
	p1 = Player("David")
	p2 = Player("IA1")
	p3 = Player("Thibaud")
	p4 = Player("IA2")
	g = Game([p1, p2, p3, p4])
	g.shuffleDeck()
	print("Deck : " + str(g.deck))
	print("New round, player " + p2.name + " is the dealer")
	g.newRound(1)
	print(p1.name + str(p1.hand))
	print(p2.name + str(p2.hand))
	print(p3.name + str(p3.hand))
	print(p4.name + str(p4.hand))
	print("bid : " + str(g.round.bid))
	g.round.makeABid(p3, p3.hand[0][0], 110)
	print(p3.name + " makes a bid")
	print("bid : " + str(g.round.bid))
	g.round.playCard(p3, 0)
	print(p3.name + " plays") 
	print("Trick : " + str(g.round.trick))
	print(p3.name + str(p3.hand))

class Game:
	"""Class defining a game"""

	def __init__(self, players):
		self.deck = CARDS
		self.score = [0, 0]
		self.players = players
		self.round = None

	def shuffleDeck(self):
		self.deck = random.sample(self.deck, k=len(self.deck))

	def cutDeck(self):
		n = int(random.uniform(1, len(self.deck)))
		self.deck = self.deck[n:len(self.deck)] + self.deck[0:n]

	def newRound(self, dealerIndex):
		self.round = Round(self.players, dealerIndex, self.deck)		

class Round:
	"""Class defining a round"""

	def __init__(self, players, dealerIndex, deck):
		"""players : list of player
		   dealerIndex : int corresponding to the dealer's position in the players list
		   deck : list of card corresponding to the deck"""
		self.dealerIndex = dealerIndex
		self.trick = []
		self.bid = ['?', '?', 0]

		for j in [3, 2, 3]: # Card dealing pattern : 3/3/3/3/2/2/2/2/3/3/3/3
			for i in range(1, 5):
				players[(self.dealerIndex+i)%len(players)].hand.extend(deck[0:j]) # Modulus to wrap around list
				del deck[0:j]

	def playCard(self, player, cardIndex):
		"""player : player that play a card
		   cardIndex : int corresponding to the card position in the player's hand"""

		self.trick.append(player.hand[cardIndex])
		del player.hand[cardIndex]

	def makeABid(self, player, color, bidValue):
		"""player : player that make a bid
		   color : card color for the bid
		   bidValue : int corresponding to the bid value"""

		self.bid = [player.name, color, bidValue]

class Player:
	"""Class defining a player"""

	def __init__(self, name):
		self.name = name
		self.hand = []
