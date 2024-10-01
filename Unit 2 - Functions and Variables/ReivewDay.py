print("Hello, World!")          #"Hello, World!" is the parameter.
input("Please enter you username\n")  #\n is called an escape character.
                                    #\n starts a new line. (Linebreak)
#input is never required for programs to work.
#variables
#Syntax is the way you write the code. Example: <Name> # <value>

x=5


#Some conversation functions


str()
float()
int()
bin()
bool()
#Parameters () are the values that the function needs to run.


#Snake naming convention - all lowercase, underscore for spaces.
#CONCISE: Short yet descriptive

username = "UrMom123"  #Define
fav_animal = "fox"    #Define
total_apples = 2    #Define

total_apples = 5        #This was a reassignment, which means taking a variable, (such as total_apples,) and reassigning it's value. I changed it. It went from 2 to 5, as you can see.


percent_Complete = 23.52   #Define Boolean (True/False)
is_cool = True     #Define Boolean (True/False)
first_letter = 'c'

total_apples = 4   #Reassign

#Arithmentic operators
#   +   -   *   /   **    %   //

print(4+4)      #>8
print("4" + "4")    #>44
print("cat" + "Dog")  #catDog
print("cat" * 3)    #Catcatcat
print("cat" + 3)        #Error: Cannot use for string and int

#Make some working programs
#1. add two numbers using input

x = input("What is x?\n>")  #Input always returns in a string...
y = input("What is y?\n>")  #... Even if you type in a number.
y = int(y)                  #Convert from string to int
print(x+y)

#2: Converts celcius to farenheight
temp_celcius = 40
temp_celcius
temp_farenheight = (temp_celcius * 1.8) + 32
print(temp_celcius + " degrees C equals " + temp_farenheight + " degrees F ")

#Functions are a lot like variables. They have names, they can be recalled from memory by calling their name, and  store information.

def potato():       #Def keyword + name + () + :
    print("potato")     #Lines indented underneath the variables are "inside" the function.

#Functions are not run when theyare defined. They must be called by their name to run.
potato()       #Every function call needs open and closed parenthesis...
               #...Even if it has no parameters.
def jump(how_high):
    print("You jumped" + str(how_high) + " inches!")

jump(14)

def make_a_word(a, b, c, d, e, f, g, h, i, j, k,):
    print(a + b + c + d + e + f + g + h + i + j + k)

make_a_word("Z", "a", "c", "k", "O", "s")


#Functions can have many lines
def top_ten_games():
    print("1. Elden Ring")
    print("2. Shadow of the Colossus")
    print("3. Minecraft")
    print("4. Diablo 3")
    print("5. Gran Turismo 7")
    print("6. Overwatch")
    print("7. Rachet & Clank: Up Your Arsenal")
    print("8 World of Warcraft")
    print("9. Path of Exile")
    print("10. Enter the Dungeon")


#Scope: Global and Local Variables!!
#Scope refers to the context in which the variable was defined.
#GLOBAL- defnined at NO indentation level.
#LOCAL- defined inside of a function

#Global variables can be used ANYWHERE.
todd = "cool guy"  #This is a global variable. No indentation level.

def my_function():
    smith = "not cool guy"      #This is a local variable (defined in a function). They only exist in the scope they were defined in.
    todd = "strange guy"        #Local variable even though it has the same name.
    print(todd)                 #Prints the LOCAL variable "todd".
    #When you call a variable in a function, it searches local variables first, and THEN local variables.

#If you want to reassign a global variable inside of a function:
todd = "cool guy"
def my_function():
    global todd                      #In this function, when I call todd, I'm refferring to global todd, not local todd. "Todd" got reassighned.Reassighn todd - global. #Print todd- global.

    
    todd = "strange guy"
    print(todd)

#Return functions
    #Functions can also return values
    #The value that is returned  is sent back to where the function was called.
    #This is very similar to how a variable works.
    #The function does its work and returns to answer back.

def add2(x,y):
    return x + y

print



