game = [[1,2,1],
        [2,2,1],
        [1,2,2]]

def winner(list):
    for i in range(3):
        if list[i][0] == list[i][1] == list[i][2] == 1:
            return ('Winner is player:' +str(1))
        elif list[0][i] == list[1][i] == list[2][i] == 1:
            return ('Winner is player:' +str(1))
        if list[i][0] == list[i][1] == list[i][2] == 2:
            return ('Winner is player:' +str(2))
        elif list[0][i] == list[1][i] == list[2][i] == 2:
            return ('Winner is player:' +str(2))
        if list[0][0] == list[1][1] == list[2][2] == 1:
            return ('Winner is player:' +str(1))
        elif list[0][0] == list[1][1] == list[2][2] == 2:
            return ('Winner is player:' +str(2))
        if list[2][0] == list[1][1] == list[0][2] == 1:
            return ('Winner is player:' +str(1))
        elif list[2][0] == list[1][1] == list[0][2] == 2:
            return ('Winner is player:' +str(2))
        #else:
         #   return ("it's a tie")

print winner(game)
