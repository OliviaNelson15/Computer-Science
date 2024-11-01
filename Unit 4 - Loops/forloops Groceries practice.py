#PRACTICE: Create a list of groceries
#Contains Milk, Eggs, Bread, Butter, and Apples
#Ask for user input on an item they purchased
#If the item was on the list, print (",item> crossed off the list!")
#Remove that item from the list.
#You will need to use a for loop to search for that item.
#You will need an 'if' statement in the for loop to check.

groceries = ["milk", "eggs", "butter", "apples", "bread"]

purchaseditem = input("What item did you purchase? Please use all lowercase letters!")

for grocery in groceries:
    if grocery == purchaseditem:
        print(grocery + " checked off the list!")
        groceries.remove(grocery)

print(groceries)


#Create a list of five random numbers from 0-100
#Use a for loop to find the sum of those numbers.

numbers = [5, 6, 7, 8, 9]
for num in numbers:
    print(sum(numbers))