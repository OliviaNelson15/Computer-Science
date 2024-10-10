x = 5
if x>0: # >< == >= <= !=
    print ("x is a positive number!")
elif x < 0:         #Always paired to an "if" statement.

else:       #Else statements are always paired w/ "if" statements
    print("x is a negative number!")

color = "red"           #ONLY ONE if
if color.lower()=="green":
    print("GO")

elif color.lower() == "red":           #No limit to how many elifs you can use
    print("STOP")

else:       #Only one ELSE
    print("STOP IF SAFE TO DO SO")

#elif stands for else/if

#Bro why do I even need elif statements?
#Can't I just use more "if"s?
#Well, HERE'S YOUR ANSWER:

x  = 10

if x > 5:
    print("x is greater than five")

if x>8:
    print("x is greater than 8")

######################################

if x > 5:
    print("x is greater than five")

elif x > 8:
    print("x is greater than eight")

#TWO IF STATEMENTS ARE NOT RELATED TO EACH OTHER IN ANY WAY. THAT'S WHY.
#IF YOU WERE TO USE BOTH, YOU WOULD NOT GET THE DESIRED RESULT.
#If and elif, however, ARE related. "Elif" has to go with an "if" statement.