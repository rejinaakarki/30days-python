#Number guessing game 
import random
target = random.randint(1,100)
guess = 0 #Guess start from 0
while guess != target:
    guess = int(input("Enter a number you guessed between(1,100):"))
    if guess < target:
     print("Too low!")

    elif guess > target:
     print("Too high!")

    else:
     print("Congratulations! You guessed the number.")
#no break 

import random 

target = random.randint(1,500)
while True:
  guess = int(input("Enter number to guess between(1,500):"))
  if target > guess:
    print("Guess Higher")
  elif target < guess:
    print("Guess Lower")
  else:
    print("Congratulations!You guess it right")
    break 
  #More insight on this
  #here we can give a fixed no. of attempt so the user would not keeps on guessing it for longer period
  #While giving fixe no. of attempt for i(attempt) in range() loop is used
  #we can also display a message if to 
  # let them know they are closer 
  # to the number to be guessed by calculating distance



    

