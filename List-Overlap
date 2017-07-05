import random
n1 = int(raw_input("Enter number to generate list1:"))
n2 = int(raw_input("Enter number to generate list2:"))
list1 = random.sample(xrange(0, 500), n1)
list2 = random.sample(xrange(0, 500), n2)
print "Your randomly generated lists are:"
print list1
print list2
new_l = []
if len(list1) >= len(list2):
    for i in list2:
        if i in list1 and i not in new_l:
            new_l.append(i)
    if len(new_l) > 0:
        print "common items from these 2 lists are:", new_l
    else:
        print "there are no common items in your list, good luck next time."
else:
    for i in list1:
        if i in list2 and i not in new_l:
            new_l.append(i)
    if len(new_l) > 0:
        print "common items from these 2 lists are:", new_l
    else:
        print "there are no common items in your list, good luck next time."
