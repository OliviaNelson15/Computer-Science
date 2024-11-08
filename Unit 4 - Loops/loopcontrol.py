#Loop control statements allow you to change how loops operate.
#You can do things like quit the loop early, skip the current loop, and even: DO NOTHING :O
#Break, continue, and pass

#Break
#Exits a loop prematurely, before it was suppposed to end


#Example


bag_of_fruit = ["apple", "orange", "strawberry", "bug", "watermelon"]

for fruit in bag_of_fruit:

    if fruit == "bug":
        print("Eww, you found a bug in the bag!")
        break    #The "break" statement exits the loop immediately and continues
    else:
        print("You ate a " + fruit)



#Continue
#Skips the currrent loop
#It does not exit the entire loop, it just moves on to the next iteration

#Example
orders = [15, 30, 35, 33, 100, 3, 10, 22]

#Only apply discount for orders above $20

for order in orders:
    if order in orders:
        if order < 20:
            continue        #Skips the rest of the loop iteration and goes to the next iteration
    print(str(order) + " order discounted 5% to $" + str(order * 0.95))



#Pass
#Does absouletly nothing.
#It's usually used as a placeholder while writing code.

if True:
    pass

def enter_forest():
    pass

def swim_river():
    pass

def eat_icecream():
    pass