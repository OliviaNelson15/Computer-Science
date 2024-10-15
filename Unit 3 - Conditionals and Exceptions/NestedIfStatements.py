#NEsted if statements
#
#

prime = True
cost = 20
age = 17
consent = False

if prime:
    if age >= 18:
        print("You are eligable for free shipping!")
    else:
        if consent:
            print("You are eligable for free shipping!")
        else:
            print("YOU SCALLYWAG, you are NOT eligable for free shipping!!")
elif cost >=25:
    if consent:
        print("You are eligable for free shipping!")
    elif consent:
        print("You are eligable for free shipping!")
    else:
        print("You are NMOT eligable for free shipping!")
    
else:
    print("You are NOT eligable for free shipping!")


#Do we need an umbrella 
raining=input("Is it raining today?")
if raining.lower() == "yes":
    outside = input("Are you going outside today?")

if outside.lower() -- "yes":
    print("Bring an umbrella")
    else:
    print("Don't bring an umbrella")
else:
print("Don't bring an umbrella")