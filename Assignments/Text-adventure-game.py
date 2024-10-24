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
        print("Wow, some detective you are. Suddenly, you see a bakery down the street that was closed. The bakery is usually open at this time. You decide to go and investigate.")
        breadstore()
    elif choice == "2":
        print("The teens tell you that the Bandit had apparently beem spotted in the area a few hours go. According to them, he had robbed another bakery down the street. You decide to go to the bakery to investigate.")
        breadstore()
    else:
        print("Invalid response. Please try again.")
        Eavesdropping()

def breadstore():
    print("You enter the bakery. There is a man at the counter with a terrified and shocked expression. You ask him what happened. 'Didn't you hear?' He said, 'The Bread-stealing bandit robbed my store. Not only that, but he turns his victims into bread! I'm Lucky to be alive!' Do you:")
    print("1. Attempt to comfort the man\n")
    print("2. Call the man a wimp\n")

    choice = input(">")
    if choice == "1":
        print("You get the man to calm down and then ask him some questions. He says that even though the bandit's face was covered and he was wearing all black, he could still see his piercing yellow eyes that seemed to stare into his soul. (YES, the bandit's eyes are yellow. Just go with it.)")
        uglyhat()
    elif choice == "2":
        print("You call the man a wimp and tell him to man up. He gets mad and throws a bread knife at you. He yells at you to leave the store and never come back. Congrats, you dumb detective! Now you didn't get the answers you need, and the Bandit was never caught. Game over. Try again.")
        BreadySetGo()
    else:
        print("Invalid response. Please try again.")
        breadstore()

def uglyhat():
    print("You ask around to see if anyone had seen someone with yellow eyes. A lady tells you that she saw some weirdo in the mirror store wearing the most hideous had known to man and admiring his reflection. She couldn't really see his face, but, but she did notice his strange yellow eyes. Do you:")
    print("1. Head over to the hat store down the street\n")
    print("2. Go to the mirror store\n")

    choice = input(">")
    if choice == "1":
        print("You walk down the street to the hat store and ask the owner if anyone with yellow eyes had bought a hat recently. She says yes and explains that a guy with yellow eyes and dark brown hair had stopped by an hour or two ago.")
        checkingthecameras1()
    elif choice == "2":
        print("You go to the mirror store and ask the owner if they say a guy wearing an ugly hat came in. He says yes and explains that he had stopped by an hour or two ago.")
        checkingthecameras2()
    else:
        print("Invalid response. Please try again.")
        uglyhat()

def checkingthecameras1():
    print("You decide the check the cameras. You see the Bandit talking to someone and then handing him a slip of paper. You immediately recognize the guy recieving the paper as one of the Bandit's old associates. He had escaped from prison recently. When the two exit the store, you notice that the man had accidentally dropped the peice of paper. You go to the section of the store they had been in and find the peice of paper. You pick it up and realize that there is an address written on it. Do you:")
    print("1. Go straight to the address\n")
    print("2. Go outside to see if anyone had seen where they had went\n")

    choice = input(">")
    if choice == "1":
        print("You go to the address. However, the Bandit is waiting for you. The second you open the door, he jumps out and stabs you. You're toast. (Literally.) Try again!")
        BreadySetGo()
    elif choice == "2":
        print("You go outside and a mysterious woman walks up to you. She is wearing sunglasses and has long, blond hair. She tells you that she knows excactly where the Bandit is, and she can take you to him.")
        mysteriouslady()
    else:
        print("Invalid response. Please try again.")
        checkingthecameras1()

def checkingthecameras2():   #The mirror store version.
    print("You decide the check the cameras and see ")



BreadySetGo()