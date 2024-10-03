#1
User_input1=input("Write a random word.")
User_input2=input("Write another random word.")
User_input3=input("Write one last random word.")
print(User_input1 + User_input2 + User_input3)


#2 add_three
def add():
    x = input("What is the first number?")
    print(type(int(x)))
    y = input("What is the second number?")
    print(type(int(y)))
    z = ("What is the third number?")
    print(type(int(z)))
    print(str(x) + "+" + str(y) + "+" + str(z) + "=" + str(x+y+z))

#3 data_three
def data_three():
    w = input("Write a random word.")
    print(w)
    print(type(int(w)))
    s = input("Good, now write an integer.")
    print(s)
    print(type(int(s)))
    e = input("Lastly, write a float.")
    print(s + "+" + e)
    print(str(s) + "+" + str(e) + "=" + str(s+e))
    print(str(s+e) + "+" + (w) + "=" + str(s+e+w))
    


