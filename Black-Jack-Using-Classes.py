import randomclass Player(object):
    Wins = 0
    Losses = 0
    Busts = 0
    amount = 0
    def __init__(self,bank):
        self.bank = bank
    def bet_ammount(self):
        self.amount = int(raw_input("Enter amount you want to put as betting:"))
    def win_balance(self):
        self.bank += self.amount
        print "your current bank balance after this win is:", self.bank
    def loss_balance(self):
        self.bank -= self.amount
        print "your current bank balance after this loss is:", self.bank
    def game_count(self,x):
        if x == 'Wins':
            self.Wins += 1
        if x == 'Looses':
            self.Looses += 1
        if x == 'Busts':
            self.Busts += 1
    def summary(self):
        print "Here is your current summary:\n Current balance:",self.bank,"\n Total Wins:",self.Wins,"\n Total Losses:",self.Losses,"\n Total Busts:",self.Busts
        
        
class Deck(object):
    full_deck = []
    used_deck = []
    hand_card = []
    faces = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
    color = ['Club','Spade','Heart','Diamond']
    def __init__(self,):
        pass   
    def My_deck(self):
        self.full_deck = [(x,y) for x in self.faces for y in self.color]
        random.shuffle(self.full_deck)
        return self.full_deck
      #print full_deck
    def used_cards(self,(i,j)):
        self.used_deck.append((i,j))
        return self.used_deck
    def remaining_cards(self,(i,j)):
        self.full_deck.remove((i,j))
        return self.full_deck
    def my_hand(self):
        for i in range(2):
            self.hand_card.append(self.full_deck[i])
        return self.hand_card  
    def stand(self):
        return self.hand_card
    def hit(self,((i,j))):
        self.hand_card.append((i,j))
        return self.hand_card

      
Running = True
print "Welcome to the game of Black Jack"
bank = int(raw_input("How much money you want to loan from bank:\n"))
p1 = Player(bank)
pd = Deck()
dd = Deck()
while Running:
    print "Let's Begin the Game"
    p1.bet_ammount()
    print "Your hand is:", pd.my_hand()
    print pd.My_deck()
    print dd.My_deck()
    print "Dealer has "
    break
    #    print d1.My_deck()#h1 = Hand()#print d1.full_deck #print d1.stand()#print d1.my_hand()#print d1.hit((3,'heart'))#print d1.my_hand()#print d1.used_cards((2,'Club'))#print d1.remaining_cards((2,'Club'))#print d1.used_cards(('Ace','Diamond'))#print d1.remaining_cards(('Ace','Diamond'))#p1 = Player(100)
#p1.win_balance()#p1.loss_balance()#p1.Wins#p1.game_count('Wins')#p1.game_count('Wins')#p1.summary()
