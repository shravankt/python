with open('prime.txt', 'r') as pf:
    pf = pf.read()
    pf = pf.split("\n")
    #print pf
with open('happy.txt', 'r') as hf:
    hf = hf.read()
    hf = hf.split("\n")
    #print hf
with open('overlap.txt', 'w') as olf:
    for num in pf:
        if num in hf:
            olf.write(num + "\n")
            #print olf
with open('overlap.txt', 'r') as olf1:
    olf1 = olf1.read()
    print olf1
