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

#1
def BreadySetGo():
    print("'Detective! People have been going missing, and a bunch of bakeries have been robbed of all their bread! All signs point towards the Bread-stealing Bandit... He's finally returned. We need you to find him and arrest him! Are you up to the task?'")
    print("1. Yes! Justice will be served!\n")
    print("2. Pfft, no way! Skill issue. Deal with it yourself.\n")

    choice = input(">")

    if choice == "1":
        thestreet()
    elif choice == "2":
        print("'What a shame... we were told you were the best. Clearly we were mistaken.' GAME OVER. You got fired, and your reputation was destroyed. Try again!")
        
    else:
        print("Invalid response. Please try again.")
        BreadySetGo()

#2
def thestreet():
    print("You walk out onto the street and see a sketchy guy walking towards you. He says he will help you if you give him some money. Do you:")
    print("1. Accept his offer and give him $200.\n")
    print("2. Say 'no thank you,' and walk away.\n")

    choice = input(">")
    if choice == "1":
        downtown()

    elif choice == "2":
        print("'What a shame... JUMP 'EM, BOYS!!!' Suddenly, you see a bunch of people running at you. They steal everything you have and then run off... You got jumped. Game over. Try again. Bready, set, go!")
    else:
        print("Invalid response. Please try again.")
        thestreet()



#3
def downtown():
    print("You give the shady-looking man $200. He chuckles to himself. 'Thanks, man...' and then he walks away. It seems you've been BAMBOOZLED... that's okay, though. The show must go on!")
    print("You can either chase the theif to try and get your money back, or you can stop for some lunch. What do you choose?:")
    print("1. Let's stop for some lunch. I'm hungry!\n")
    print("2. I'm not gonna let him baguette away with this!\n")

    choice = input(">")
    if choice == "1":
        Eavesdropping()
    elif choice == "2":
        print("You go after the theif, but he's long gone. You decide to walk further downtown to try to get more answers.")
    else:
        print("Invalid response. Please try again.")
        downtown()

#4
def Eavesdropping():
    print("You sit down at an outside table and wait for someone to take your order. You then overhear two teens talking about the Bread-stealing Bandit. Do you:")
    print("1. Ignore them. They're just a couple of stupid teens gossiping. Darn whippersnappers!\n")
    print("2. Walk up to them and ask a few questions. Any information is useful!\n")

    choice = input(">")
    if choice == "1":
        print("Wow, some detective you are. Suddenly, you see a bread store down the street that was closed. The store is usually open at this time. You decide to go and investigate.")
        breadstore()
    elif choice == "2":
        print("The teens tell you that the Bandit had apparently beem spotted in the area a few hours go. According to them, he had robbed another bakery down the street. You decide to go to the bakery to investigate.")
        breadstore()
    else:
        print("Invalid response. Please try again.")
        Eavesdropping()
BreadySetGo()