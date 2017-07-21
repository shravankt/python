game = [[1,2,1],
        [2,2,1],
        [1,2,2]]

def winner(list):
    for i in range(3):
        if game[i][0] == game[i][1] == game[i][2] == 1:
            print "Player 1 is the winner"
        elif game[0][i] == game[1][i] == game[2][i] == 1:
            print "Player 1 is the winner"
        if game[i][0] == game[i][1] == game[i][2] == 2:
            print "Player 2 is the winner"
        elif game[0][i] == game[1][i] == game[2][i] == 2:
            print "Player 2 is the winner"
        if game[0][0] == game[1][1] == game[2][2] == 1:
            print "Player 1 is the winner"
        elif game[0][0] == game[1][1] == game[2][2] == 2:
            print "Player 2 is the winner"
        if game[2][0] == game[1][1] == game[0][2] == 1:
            print "Player 1 is the winner"
        elif game[2][0] == game[1][1] == game[0][2] == 2:
            print "Player 2 is the winner" 

print winner(game)
