#This programs allows the user to measure the Category of a hurricane
#based on wind speed (MPH)

answer = input("What is the wind speed? (MPH)")
answer = int(answer)
if answer < 74:
    print("Tropical storm")
    answer=int(answer)
elif answer < 96:
    print("Category 1")
    answer=int(answer)
elif answer < 111:
    print("Category 2")
    answer=int(answer)
elif answer < 130:
    print("Category 3")
    answer=int(answer)
elif answer < 157:
    print("Category 4")
    answer=int(answer)
elif answer >= 157:
    print("Category 5")
    answer=int(answer)

