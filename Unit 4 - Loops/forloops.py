#For Loops
#This is a BIG DEAL
#For loops allow the programmer to REPEAT, or what we call LOOP

#Write a program that prints the numbers 1-10.

#For <temp var> in <list>:

#range(0,10) = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range (0,10):      #0 is the START value, 10 is the STOP value.
    print(i)
    print("yo")

top_foods = ["Mac and cheese", "fried chicken", "Nachos"]
#AKA 'go through every food in top foods'
#Repeats everything in the for loop for each item in the list
#Where food equals the current item
for food in top_foods:
    print(food)


#PRACTICE: Create a list of groceries
#Contains Milk, Eggs, Bread, Butter, and Apples
#Ask for user input on an item they purchased
#If the item was on the list, print (",item> crossed off the list!")
#Remove that item from the list.
#You will need to use a for loop to search for that item.
#You will need an 'if' statement in the for loop to check.