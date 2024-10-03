def data_three():
    w = input("Write a random word.")
    print(type(int(w)))
    s = input("Good, now write an integer.")
    print(type(int(s)))
    e = input("Lastly, write a float.")
    print(str(s) + "+" + str(e) + "=" + str(s+e))
    print(str(s+e) + "+" + (w) + "=" + str(s+e+w))
