from random import shuffle
class Card(object):
    def __init__(self,suits,cardvalue):
        self.suits = suits
        self.cardvalue = cardvalue
    
        
        
class Deck(object):
    def __init__(self):
        self.numcards = []
    def shufflecards(self):
        shuffle(self.numcards)
    def create_Deck(self):
        suits=["spades","diamonds","hearts","clubs"]
        cardvalue=["Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]
        for i in range(0,4):
            for x in range(0,13):
                card1 = Card(suits[i],cardvalue[x])
                self.numcards.append(card1)
        return self
    def deal(self,user):
        print "We are Dealing now!!!"
        print "Each player gets 5 cards by default"
        totalCardsAvailable = len(self.numcards) 
        print "Total cards available:"
        print totalCardsAvailable
        # for i in range (totalCardsAvailable,totalCardsAvailable-6,-1):
        for i in range (0,6):
            print "self.numcards[i]: ", self.numcards[i]
            user.hand.append(self.numcards[i])
class Player(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.hand = []
    def drawfromdeck(self):
        return self
    def showcardsinhand(self):
        print "Cards in my hand"
        print self.hand
        return self.hand


a = Deck()
a.create_Deck()
player1 = Player("Phil","23")
player1.showcardsinhand()
a.shufflecards()
a.deal(player1)
player1.showcardsinhand()

            