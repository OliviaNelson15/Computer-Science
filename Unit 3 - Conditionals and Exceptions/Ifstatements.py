#If statements evaluate boolean exprerssions
#Make desisions about which code to run next
#Taje a temperature
#Print "<Temperature is hot" if the temperature is >= 80
#Otherwise, print "<Temperature> is not hot"
temperature =input("Hey, you. What? No, I'm talking to that tree. YES, YOU! What is the temperature?\n>")
temperature = int(temperature)
#if, boolean expression, :
#Sort of like a function, no parenthasis
if temperature >= 80:           #If the bool evaluates to True, go inside
    print("The temperature is " +  str(temperature) + "degrees.")
    print(str(temperature) + "Is it hot outside?")

if temperature < 80:
    print(str(temperature) + "degrees is not hot, and neither is your mom")

else: #Else takes NO condition and only runs if the "if" above is false. AKA, "Otherwise"
    print("UR MOM")

#Complete the activity
#Create a program that asks for a password
#Print "ACCESS GRANTED" if the password is correct
#Print "ACCESS DENIED" if the password is wrong
#The password is skibidi68