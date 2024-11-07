#Guess the number. You have 10 attempts.

import random

correctnumber = random.randint(0,101)
guess = -1


while correctnumber != guess:

    try:
        guess = int(input("Guess a number between 1 and 100\n>"))
    except:
          print("Hmm... that's not right... try again.")
    if guess > correctnumber:
            print("Too high. Try again.")
        
    elif guess < correctnumber:
            print("Too low. Try again.")
    else:
            print("Congrats! You guessed the number! The correct number was" + correctnumber)

print("Nice job!")
