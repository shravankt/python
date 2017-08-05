import random
import time
si = random.randint(0,101)
print "hey user Think of a integer of your choice between 0 to 100 \nlet's start now"
#print si
time.sleep(5)
running = True
attempt = 0
while running:
  print "You gussed No.", si
  answer = raw_input("Is it a correct guess or not: y/n:")
  if "y" in answer.lower():
      if attempt <= 3:
          print "i deserv some byte to guess it in", attempt, "tries"
      elif 3 < attempt <= 10:            print "Reasonable as it took", attempt, "tries not good enough"
      elif attempt > 10:            print "pretty bad for computer to take", attempt, "tries"
      break
  elif "n" in answer.lower():
      answer = raw_input("Is it lower or higher than what you thought of, lower or higher:")
          if "lo" in answer.lower():
              si += random.randint(1,4)
          elif "hi" in answer.lower():
              si -= random.randint(1,4)
  attempt += 1
