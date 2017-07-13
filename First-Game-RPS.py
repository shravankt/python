from random import randint
import random
print "Let's play Rock,Paper,Scissor "
while True:   
    player2 = raw_input("input your choice:")
    option = ["Rock", "Paper", "Scissor"]
    player1 = option[random.randint(0,2)]
    #print player1
    if player1 == "Rock" and player2 == "Paper":
        print "Computer got:", player1
        print "Congratulations you win!!!"
        break
    elif player1 == "Scissor" and player2 == "Paper":
        print "Computer got:", player1
        print "COmputer Wins and you loose. Better luck next time"
        break
    elif player1 == "Paper" and player2 == "Rock":
        print "Computer got:", player1
        print "COmputer Wins and you loose. Better luck next time"
        break
    elif player1 == "Scissor" and player2 == "Rock":
        print "Computer got:", player1
        print "Congratulations you win!!!"
        break
    elif player1 == "Rock" and player2 == "Scissor":
        print "Computer got:", player1
        print "COmputer Wins and you loose. Better luck next time"
        break
    elif player1 == "Paper" and player2 == "Scissor":
        print "Computer got:", player1
        print "Congratulations you win!!!"
        break
    elif player1 == player2:
        print "Computer input:", player1, "\n and your input is:", player2
        print "It's a tie. Play again"
        continue
    else:
        input = raw_input("you want ot continue y/n:")
        if input == "y":
            continue
        else:
            print "Thanks for playing. see you again"
            break
