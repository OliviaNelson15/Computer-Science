#Start with bubble sort
#Apparently it should be around 13 lines...
#Generate a list of numbers from 0-99, and print it before it's sorted

numbers = [34, 7, 23, 32, 5, 62]

def bubblesort(numbers):   #Take list as a parameter.
    #create a variable for the amount of steps we are taking. Start at 0
    steps = 0
    #Repeatedly check if list is sorted as long as there are list items
    for i in range(0, len(numbers) - 1):
        for j in range(0,len(nums)-1): #Iterate for every item in list
            if numbers[1] > numbers[i +1]:
                #Check if current list item is greater than next.
                numbers[i], numbers [i +1] = numbers{i+1}
            numbers[1] = numbers[i+1] #Swap values if needed.
            numbers[i+1] = a

            #Increase number of steps somewhere down here
            

        steps=0
        bubblesortsteps:

#...I'll just work on merge sort for now.

def mergesort(numbers):
    num1 = 34
    num2=7
    num3=23
    num4=32
    num5=5 #Lol
    num6=62

    for num in numbers:
        print(numbers)
        if num1 > num2:

numbers = [random.radiant]



# [9,3,5,2,6,7,3]
print(numbers)
#Set pivit as last #
#Find L
def quicksort(n):
    for i in range(0, len(n)):
    pivot = n[-1]
    for num in n:
        if num > pivot:
            iPos = i
            l = num
            break

    #Find r
    for i in range(len(n)-1, -1, -1):
        if n[1] < pivot:
            r = n [1]
            rPos = i
            break
#Now swap L and R values
    n[lPos], n[rPos] = n[rPos], n[lPos]

#Check if l index is greater than r index
    if lPos


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less_than_pivot = [x for x in arr[1:] if x <= pivot]
        greater_than_pivot = [x for x in arr[1:] if x > pivot]
        return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)
    
print(quicksort(numbers))