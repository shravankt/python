l1 = ['x','0','0']
l2 = ['0','0','0']
l3 = ['0','0','0']
game = [l1,l2,l3]
choice = ['x','o']

def winner(board1):
    for i in range(3):
        if board1[i][0] == board1[i][1] == board1[i][2] == str(choice[0]):
            #return ('Winner is player:' +str(1))
            print "Winner is player:", choice[0]
            return True
        elif board1[0][i] == board1[1][i] == board1[2][i] == str(choice[0]):
            #return ('Winner is player:' +str(1))
            print "Winner is player:", choice[0]
            return True
        if board1[i][0] == board1[i][1] == board1[i][2] == str(choice[1]):
            #return ('Winner is player:' +str(2))
            print "Winner is player:", choice[1]
            return True
        elif board1[0][i] == board1[1][i] == board1[2][i] == str(choice[1]):
            #return ('Winner is player:' +str(2))
            print "Winner is player:", choice[1]
            return True
        if board1[0][0] == board1[1][1] == board1[2][2] == str(choice[0]):
            #return ('Winner is player:' +str(1))
            print "Winner is player:", choice[0]
            return True
        elif board1[0][0] == board1[1][1] == board1[2][2] == str(choice[1]):
            #return ('Winner is player:' +str(2))
            print "Winner is player:", choice[1]
            return True
        if board1[2][0] == board1[1][1] == board1[0][2] == str(choice[0]):
            #return ('Winner is player:' +str(1))
            print "Winner is player:", choice[0]
            return True
        elif board1[2][0] == board1[1][1] == board1[0][2] == str(choice[1]):
            #return ('Winner is player:' +str(2))
            print "Winner is player:", choice[1]
            return True
    else:
        print "it's a DRAW"
        return False
def check_value(ui):
    for i in range(3):
        for j in range(3):
            if game[i][j] == ui[0][1]:
                return ("Common!! Please Enter your choice for row,col that is empty or filled with zero '0'")
                break
            else:
                return True

print "Basic Rule of the Game:\n 1. Player 1 to use x and player 2 to use o\n 2. put your input in row,col i.e. 1,1 to put number in first box"
#time.sleep(5)
print "Let's start:\n", (".\n".join(str(i) for i in game))
print winner(game)
loop = True
while loop:
    p1s = raw_input("User1 Enter your choice:").split(",")
    p1i = map(int, p1s)
    #print check_value('x')
    if game[p1i[0]-1][p1i[1]-1] == 'x' or game[p1i[0]-1][p1i[1]-1] == 'o':
        print "Common!! Please Enter a valid choice for row,col that is empty or filled with zero '0'"
    else:
        game[p1i[0]-1][p1i[1]-1] = 'x'
    print (".\n".join(str(i) for i in game))
    if winner(game) == True:
        break
    else:
        p2s = raw_input("User2 Enter your choice:").split(",")
        p2i = map(int, p2s)
        if game[p2i[0]-1][p2i[1]-1] == 'o' or game[p2i[0]-1][p2i[1]-1] == 'x':
            print "Common!! Please Enter a valid choice for row,col that is empty or filled with zero '0'"
        else:
            game[p2i[0]-1][p2i[1]-1] = 'o'
        print (".\n".join(str(i) for i in game))
        if winner(game) == True:
            break
        else:
            continue
