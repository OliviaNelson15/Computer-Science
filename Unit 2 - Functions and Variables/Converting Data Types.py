# Start by copying this code block into a new file called dataconversion.py in your unit 2 folder. This is an ungraded activity.

# Successfully convert all of the following variables to another type and print the result
# If the conversion prints without errors, you did the conversion correctly

a = 115;     numstr = 115   #int -> string
num_str = str(115)

b = 3.14;   num_float = 3.14 #float -> string
float_str = str(num_float)

c = "68";   num_str = "68"        #string -> int
num = int(num_str)

d = "True";   bool_str = "True"      #string -> boolean
bool_val = bool(bool_str)

e = True;      bool_val = True #boolean -> string
bool_str = str(bool_val)

f = False;      bool_val = False   #boolean -> string
bool_str = str(bool_val)

g = '10110111';    binary_num = '10110111' #byte -> int
num = int(binary_num, 2)

h = "2.54";      float_str = "2.54"  #string -> float
num = float(float_str)

i = 100;     num = 100 #int -> float
num_float = float(num)

j = 10.0;    num_float = 10.0 #float -> int
num = int(num_float)

k = 254;     num = 254  #int -> byte
binary_num = bin(num)

print(all)