import datetime
nameage = []
name = raw_input("Enter your Name:")
age = raw_input("Enter your age:")
nameage.append(name)
nameage.append(age)
cyear = datetime.datetime.now().year
fyear = cyear + (100 - int(nameage[1]))
print ("Hi", nameage[0], ". you will become 100 years old in year:", fyear)
num = int(raw_input("ENter the number by how many times you want to repeat above message:"))
nameage.append(num)
i = 0
while i < nameage[2]:
    print "Hi", nameage[0], ". you will become 100 years old in year:", fyear
    i += 1
