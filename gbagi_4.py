print('''#############################################
# Name: Divine Gbagi
# Submission Date: 00/00/2020
# Minnesota State University Moorhead
# Class: CSIS 152
# Assignment 04
#############################################''')

"""
This is a Python sample code for Assignment 04
"""
print("##############################")
print("# Hello, CSIS students!")
print("##############################")

str1 = "abc"       # Declare a variable with a value, "abc"
str2 = "123.45"    # Declare a variable with a value, "123.45"
print("str1 =", str1, "\nstr2 =", str2)  # print str1, str2

str2_int =int(float(str2)) # Convert str2 to a number and store the number to str2_int
print(str2_int)        # print str2_int

a = 2              # Declare a variable with a value, 2
b = 19             # Declare a variable with a value, 19
c = str(a) + "." + str(b)  # Concatanate strings, a, ".", and b 
print(type(c))     # print c's type
print(c)           # print c

nineteenabc = 678.9        # Declare a variable with a value, 678.9

d = 180/(b-1)      # d is supposed to have a value, 10.0
print(d)           # print d

"""
Prompt the user to enter the number of oz and convert oz to ml (1 oz = 29.5735 ml)
"""
oz = int(input("What is the oz in ml? "))   # Prompt the user to enter a number, 4
ml = oz * 29.5735
print(ml, " degrees ml is", oz, " degrees oz")

"""
Prompt the user to enter the number of ml and convert oz to oz (1 oz = 29.5735 ml)
"""
ml = float(input("What is the ml in oz? "))   # Prompt the user to enter a number, 2.19
oz = ml / 29.5735
print(oz, " degrees oz is", ml, " degrees ml")
