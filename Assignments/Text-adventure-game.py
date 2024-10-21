#Create a text adventure game about the Bread-stealing Bandit.
#You are a detective that has beens sent to catch him. YOU MUST HAVE AT LEAST 20 ENCOUNTERS INSIDE OF FUNCTIONS!
#If the player fails / gets a bad ending, put a bread pun in there.
#(The Bread-stealing Bandit bakes his victims into bread.)
#List of bread puns:

#You got turned into toast. Butter luck next time!
#You got turned into bread... c'mon, try again! You can't let him baguette away with this!
#You got turned into bread... quit loafing around! Try again.
#You let your guard down... you're toast. Try again!
#Try again! Bready, set, go!

def BreadySetGo():
    print("Detective! People have been going missing, and a bunch of bread stores have been robbed of all their bread! All signs point towards the Bread-stealing bandit... He's finally returned. We need you to find him and arrest him! Are you up to the task?")
    x1 = int(input("1. Yes! Justice will be served!\n"))
    y1 = int(input("2. Pfft, no way! Skill issue. Deal with it yourself.\n"))

    choice = input("> ")

    if choice == x1:
        find_him=print("All right... be careful, and good luck!")
    elif choice == y1:
        refuse=print("What a shame... we were told you were the best. Clearly we were mistaken.")
    else:
        print("Invalid response. Please try again.")
        BreadySetGo()