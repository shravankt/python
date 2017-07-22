import time
l1 = [0,0,0]
l2 = [0,0,0]
l3 = [0,0,0]
game = [l1,l2,l3]
choice = ['x','o']

def winner(board1):
    for i in range(3):
        if board1[i][0] == board1[i][1] == board1[i][2] == str(choice[0]):
            return ('Winner is player:' +str(1))
        elif board1[0][i] == board1[1][i] == board1[2][i] == str(choice[0]):
            return ('Winner is player:' +str(1))
        if board1[i][0] == board1[i][1] == board1[i][2] == str(choice[1]):
            return ('Winner is player:' +str(2))
        elif board1[0][i] == board1[1][i] == board1[2][i] == str(choice[1]):
            return ('Winner is player:' +str(2))
        if board1[0][0] == board1[1][1] == board1[2][2] == str(choice[0]):
            return ('Winner is player:' +str(1))
        elif board1[0][0] == board1[1][1] == board1[2][2] == str(choice[1]):
            return ('Winner is player:' +str(2))
        if board1[2][0] == board1[1][1] == board1[0][2] == str(choice[0]):
            return ('Winner is player:' +str(1))
        elif board1[2][0] == board1[1][1] == board1[0][2] == str(choice[1]):
            return ('Winner is player:' +str(2))
    else:
        return ("it's a DRAW")
def check_value(ui):
    for i in range(3):
        for j in range(3):
            if game[i][j] == ui:
                return ("Common!! Please Enter your choice for row,col that is empty or filled with zero '0'")

print "Basic Rule of the Game:\n 1. Player 1 to use x and player 2 to use o\n 2. put your input in row,col i.e. 1,1 to put number in first box"
#time.sleep(5)
print "Let's start:\n", (".\n".join(str(i) for i in game))
print winner(game)
loop = True
while loop:
    p1 = raw_input("Enter your choice:").split(",")
    p1 = map(int, p1)
    #print p1
    i1 = p1[0]
    i2 = p1[1]
    #print i1
    #print i2
    game[i1].insert(i2,'x')
    #print check_value(p1)
    print game
