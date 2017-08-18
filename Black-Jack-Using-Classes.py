import random
class Player(object):
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
            self.Losses += 1
        if x == 'Busts':
            self.Busts += 1
    def summary(self):
        print "Here is your Current Summary:\n CURRENT BALANCE:",self.bank,"\n TOTAL WINS:",self.Wins,"\n TOTAL LOSSES:",self.Losses,"\n Total Busts:",self.Busts
        
class Deck(object):
    full_deck = []
    used_deck = []
    hand_card = []
    dealer_card = []
    faces = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
    color = ['Club','Spade','Heart','Diamond']
    def __init__(self,):
        pass
    def My_deck(self):
        self.full_deck = [[x,y] for x in self.faces for y in self.color]
        random.shuffle(self.full_deck)
        return self.full_deck
    #print full_deck 
    def used_cards(self,(i,j)):
        self.used_deck.append([i,j])
        return self.used_deck
    def remaining_cards(self,(i,j)):
        self.full_deck.remove([i,j])
        return self.full_deck
    def my_hand(self):
        for i in range(2):
            self.hand_card.append(self.full_deck[i])
            self.used_deck.append(self.full_deck[i])
            self.full_deck.remove(self.full_deck[i])
            #print len(self.full_deck)
            return self.hand_card
    def dealer_hand(self):
        for i in range(2):
            self.dealer_card.append(self.full_deck[i])
            self.used_deck.append(self.full_deck[i])
            self.full_deck.remove(self.full_deck[i])
            return self.dealer_card
    def stand(self):
        return self.hand_card
    def hit_user(self):
        self.hand_card.append(self.full_deck[0])
        self.used_deck.append(self.full_deck[0])
        self.full_deck.remove(self.full_deck[0])
        return self.hand_card
    def hit_dealer(self):
        self.dealer_card.append(self.full_deck[0])
        self.used_deck.append(self.full_deck[0])
        self.full_deck.remove(self.full_deck[0])
        return self.dealer_card
    ## Below is the function to convert the J,Q,K and A to corresponding number value
def converter(fvalue_list):
        lngth = len(fvalue_list)
        for i in range(lngth):
            if fvalue_list[i][0] == 'Jack':
                fvalue_list[i][0] = 11
            elif fvalue_list[i][0] == 'Queen':
                fvalue_list[i][0] = 12
            elif fvalue_list[i][0] == 'King':
                fvalue_list[i][0] = 13
            elif fvalue_list[i][0] == 'Ace':
                fvalue_list[i][0] = 1
            else:
                fvalue_list[i][0] = fvalue_list[i][0]
def Wannaplay():
    userinput = raw_input("you want to continue to play:Y/N:")
    if userinput.upper() in YES:
        pass
    else:
        print "Thanks for playing. See you soon."
        pass
Running = True
print "Welcome to The Game of BLACK-JACK"
bank = int(raw_input("How much money in Dollers you want to loan from bank:\n"))
p1 = Player(bank)
d1 = Deck()
d1.My_deck()
#dd = Deck()
while Running:
    print "Let's Begin the Game"
    p1.bet_ammount()
    utemp = d1.my_hand()
    print "Your hand is:", utemp
    converter(utemp)
    if (utemp[0][0] + utemp[1][0]) > 21:
        p1.game_count('Busts')
        print "You got busted.lets play again"
        p1.loss_balance()
        break
        #print "Dealer's hand is:", d1.dealer_hand()    dtemp = d1.dealer_hand()    
        #Show first card of Dealer to the user and check if he has a black jack i.e. 21 ..if yes then user looses if he is not    # having black jack too and if not then game continues    #print dtemp
    print "First hand of dealer is:", dtemp[0]
    converter(dtemp)
    if (dtemp[0][0] + dtemp[1][0]) == 21 and (utemp[0][0] + utemp[1][0]) == 21:
        print "Dealer got:", dtemp
        print "Both got black jack, so let's call it a even and start a new game."
        break
    elif (dtemp[0][0] + dtemp[1][0]) == 21:
        print "Dealer got:", dtemp
        print "Dealer Wins as he got the black jack.Better luck next time"
        p1.game_count('Looses')
        p1.loss_balance()
        break
    else:
        chaal = raw_input("You want to Stand or Hit:")
        if chaal.upper() in 'STAND':
            print "Dealer got:", dtemp
            if (dtemp[0][0] + dtemp[1][0]) > (utemp[0][0] + utemp[1][0]):
                p1.game_count('Losses')
                print "Dealer Wins and you loose"
                p1.loss_balance()
                break
            elif (dtemp[0][0] + dtemp[1][0]) == (utemp[0][0] + utemp[1][0]):
                print "Both got same hand, so let's call it a even and start a new game."
                #continue
                break
            else:
                p1.game_count('Wins')
                print "Congrats you Wins"
                p1.win_balance()
                break
        if chaal.upper() in 'HIT':
            utemp = d1.hit_user()
            print "Your hand is:", utemp
            converter(utemp)
            if (utemp[0][0] + utemp[1][0] + utemp[2][0]) > 21:
                p1.game_count('Busts')
                print "You got busted.lets play again"
                p1.loss_balance()
                break
            dtemp = d1.hit_dealer()
            print "Dealer got:", dtemp
            converter(dtemp)
            if (dtemp[0][0] + dtemp[1][0] + dtemp[2][0]) > 21:
                print "Delear Got busted and you Wins"
                p1.game_count('Wins')
                p1.win_balance()
                break
            elif (dtemp[0][0] + dtemp[1][0] + dtemp[2][0]) == (utemp[0][0] + utemp[1][0] + utemp[2][0]):
                print "None Wins both have same hands"
                break
            elif (dtemp[0][0] + dtemp[1][0] + dtemp[2][0]) < (utemp[0][0] + utemp[1][0] + utemp[2][0]):
                print "Congrats You wins"
                p1.win_balance()
                p1.game_count('Wins')
                break
            elif (dtemp[0][0] + dtemp[1][0] + dtemp[2][0]) > (utemp[0][0] + utemp[1][0] + utemp[2][0]):
                print "Delear Wins this time"
                p1.game_count('Losses')
                p1.loss_balance()
                break
                #d1.used_cards(d1.my_hand[0])    #print len(d1.My_deck())    #print d1.used_deck    #
    p1.summary()    
    #print d1.full_deck    #print len(d1.full_deck)    #print "Dealer has "    #breakp1.summary()        #    print d1.My_deck()#h1 = Hand()#print d1.full_deck #print d1.stand()#print d1.my_hand()#print d1.hit((3,'heart'))#print d1.my_hand()#print d1.used_cards((2,'Club'))#print d1.remaining_cards((2,'Club'))#print d1.used_cards(('Ace','Diamond'))#print d1.remaining_cards(('Ace','Diamond'))#p1 = Player(100)
#p1.win_balance()#p1.loss_balance()#p1.Wins#p1.game_count('Wins')#p1.game_count('Wins')#
