import random
num = random.choice(xrange(1000, 9999)) 
#print num
# below function generates the list from entered number by user or computer generated number from rand function
def num_list(num):
    i = 0
    num1 = []
    while i < 4:
        j = num%10 
        num1.insert(0,j)
        num = num/10 
        i += 1
        #print num1    
     return num1
rand_num = num_list(num)
#print rand_num
#num1[:] = []
#print num1
attempt = 0
while True:
    user = int(raw_input("Guess the 4 digit number generated by computer and win prizes \n you have 5 attemps to guess correct number.Enter your choice now:"))
    user1 = num_list(user)
    print user1
    print rand_num
    cow = 0
    bull = 0
    j = 0
    for n in rand_num:
        if n == user1[j]:
        #print n
            cow += 1
            j += 1
        elif n in user1:
        #print n           
            bull += 1         
            j += 1
        else:
            j += 1
     print "you got", cow, "cow and", bull, "bull"
     attempt += 1
     if cow == 4:
         print "you gussed right after", attempt, "attempts"
         break
