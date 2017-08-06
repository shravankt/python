import random
# open a file and store every word in list and then select random word from list
with open('words.txt', 'r') as book:
    wl = book.read()
    wl = wl.split()
    #print wl
w_index = random.randint(0,len(wl)-1)
#print wl[w_index]
w_random = wl[w_index]
#print w_random
letter_list = []
running = True
l_list = []
#l_list = l_list.append(letter for letter in w_random[0])
for letter in w_random:
    l_list.append(letter)
TRY = 0
#print l_list
print "Hint- your word has now", len(w_random), "letters"
#ui = raw_input("Guess a letter now:")
while running:
    ui = raw_input("Guess a letter now:")
    if ui in l_list:
        if ui not in letter_list:
            letter_list.append(ui)
              print "Your guess list is:", letter_list
              #ui = raw_input("Correct Guess.Guess the next letter now:")
              guessword = raw_input("can you guess the word:")
              #print guessword
              if guessword == w_random: 
                  print "Congrats You guessed it right"
                  break
              else: 
                  print "Your guess is wrong. please try again"
                  #elif ui in l_list:
        elif ui in letter_list:
            ui = raw_input("This letter was already gussed. try another one:")
            #continue
    elif ui not in l_list:
        print "Please guess the correct letter as this letter is not present in the computer generated word"
        #ui = raw_input("Guess your letter again:")
    TRY += 1
print "you took:", TRY, " attempts to guess it right"
