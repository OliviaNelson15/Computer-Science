#There are a couple types of loops in Python.
#The for loop lets you iterate a list. (Great for looping a SET number of times)
#BUT. What if... we need to loop an UNCERTIAN number of times?
#ex. Entering your password...
#You could get it right the first time, it could take you a million tries, or anything in between.

realpass = 'urmom'
enteredpass = ""

attempts = 0

print("Your account will be locked after 5 tries.")

#A while loop continues looping UNTIL the condition is no longer true,
while realpass != enteredpass:  #Check if the entered password matches the real one.
    #Ask for pass
    entered_pass = input("Please enter the password\n>")
    attempts = attempts + 1
    #check if pass is correct
    if enteredpass == realpass:
        print("ACCESS GRANTED")
    else:
        print("ACCESS DENIED")
        print(str(attempts) + "attempts remaining.")
        print("Try again...")

#End password checking
print("Welcome!")


#Try this:
#UPDATE this while loop so that it PRINTS how many attempts you're on.
#Print number of attempts every loop

#With while loops, you gotta be careful for INFINITE LOOPS
#When you put your computer in rest mode, it has nightmares about infinite loops. /joke
#An infinate loop happens when you enter a while loop that can NEVER be escaped MUAHAHAHAHAHAH
#Example (do not click run...)

#count = 0
#while count < 10:
#    count += 1
#    print(count)

#print("All done!")


#Here's a REAL WORLD Example:
#"Type 'exit' to quit"

user_input = ""

    while user_input != "exit":
        user_input = input("Enter something (type 'exit' to quit)")
        print("You entered: " +)