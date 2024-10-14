# Exception handling
#Write a program that asks for 2 numbers and adds them.

#if = try
#elif = except
#else = except specific error type
#else = except

def divide_two_numbers():
    try:
        x = int(input("What is the first number?\n>"))
        y = int(input("What is the second number?\n>"))
        print(x / y)
        divide_two_numbers()

    except ValueError:
        print("Invalid entry...")
        divide_two_numbers()

    except ZeroDivisionError as e:
        print("Cannot divide by zero.")
        divide_two_numbers()

    except TypeError:
        print("Wrong arithmetic expression.")
        divide_two_numbers()

    finally:
        print()

divide_two_numbers()