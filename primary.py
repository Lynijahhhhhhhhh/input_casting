# author: Lynijahhhhhhhhhhhhhhhhh
# date: 07/08/2021

# -------------------- Section 1 -------------------- #

# Input | Saving String Responses to Variables

# Objectives:
#   1. Name in Reverse
#       a. Prompts input from the user in the form of a first name and last name.
#           Save these values to variables first_name and last_name.
#       b. Print the first and last names in reverse order.
#
# ----- EXAMPLE OUTPUT ----- #
#   >> first name... elia
#   >> last name... deppe
#   deppe, elia
#
# ---- WRITE CODE BELOW ---- #
print("Name Section")
first_name= input("What is your first name? ")
last_name= input("What is your last name? ")
print(last_name,",",first_name)
print(" ")
#   2. Pyramid
#       a. Prompt input from the user in the form of a single character. Save to a variable named symbol.
#       b. Using the symbol, create a pyramid like you see in the example output. (Think, how can you make
#           duplicates of text symbol?)
#
# ----- EXAMPLE OUTPUT ----- #
#   >> $
#
#   $
#   $$
#   $$$
#   $$
#   $
#
# ---- WRITE CODE BELOW ---- #
print("Symbols")
symbol=input("Enter ya favorite symbol character! ")
print(symbol*1 + " "*2)
print(symbol*2 + " "*1)
print(symbol*3 + " "*0)
print(symbol*2 + " "*1)
print(symbol*1 + " "*2)
print(" ")


#   3. Parallelogram
#       a. Prompt input from the user in the form of a single character. Save to a variable named symbol.
#       b. Using the symbol, create a pyramid like you see in the example output. (Think, how can you make
#           duplicates of text symbol?)
#
# ----- EXAMPLE OUTPUT ----- #
#   >> @
#
#   @
#   @@
#   @@@
#   @@@@
#    @@@
#     @@
#      @
#
# ---- WRITE CODE BELOW ---- #
print("Symbol Pyramid")
symbol=input("Enter ya favorite symbol character! ")
print(" "*3 + symbol*1)
print(" "*3 + symbol*2)
print(" "*3 + symbol*3)
print(" "*3 + symbol*4)
print(" "*4 + symbol*3)
print(" "*5 + symbol*2)
print(" "*6 + symbol*1)
print(" ")

# -------------------- Section 2 -------------------- #

# Casting | Getting Integers and Floats from the User

# Objectives:
#   1. Comparison
#       a. Prompt the user to enter a number, and save it to a variable named num1. DO NOT CAST IT.
#       b. Prompt the user to enter a number, and save it to a variable named num2. CAST IT TO AN INTEGER.
#       c. Prompt the user to enter a number, and save it to a variable named num3. CAST IT TO A FLOAT.
#       d. Print out each variable multiplied by 10.
#
# ----- EXAMPLE OUTPUT ----- #
#   >> num1... 45
#   >> num2... -132.45
#   >> num3... 2132.24
#
#   num1 (str)   | 45454545454545454545
#   num2 (int)   | -1320
#   num3 (float) | 21322.4
#
# ---- WRITE CODE BELOW ---- #
print("Number Casting")
num1=input("Enter a number: ")
num2=int(input("Enter a number: "))
num3=float(input("Enter a float: "))
print(num1*10)
print(num2*10)
print(num3*10)
print(" ")

# Objectives:
#   2. Diameter of a Circle
#       a. Prompt input from the user to enter a radius. Save this value to a
#           variable named num as an integer or float.
#       b. Compute the diameter, and print it to the user.
#           diameter = radius * 2
#
# ----- EXAMPLE OUTPUT ----- #
#   >> radius... 12.3
#
#   diameter = 24.6
#
# ---- WRITE CODE BELOW ---- #
print("Circle Diameter")
radius= int(input("Enter the radius of the circle: "))
print("The diameter of the circle is",radius*2)
print(" ")

# Objectives:
#   3. Area of a Circle
#       a. Define a function named area_circle(). Accept the parameters listed below.
#           Name   | Type(s)         | Description
#           radius | Integer / Float | The radius of the circle.
#
#           The function should compute the area of a circle, and print it to the terminal.
#               area = 3.14 * radius ** 2
#       b. Prompt input from the user to enter a radius. Save this value to a
#           variable named num as an integer or float.
#       c. Compute the radius by calling the function area_circle(), sending num as a parameter.
#
# ----- EXAMPLE OUTPUT ----- #
#   >> radius... 44.2
#
#   area of the circle: 6134.4296
#
# ---- WRITE CODE BELOW ---- #
print("Area of a circle")
def area_circle(radius):
    area = 3.14*radius**2
    print("The area of the circle is:",area)
num=float(input("Enter a radius: "))
area_circle(num)
print(" ")



# -------------------- Section 4 -------------------- #
#
# Create a conversation with a faux (fake) AI, using input and print().
# See the example in example.py
print("Hayyyyy let's talk!")
print(" ")
name= input("So what's your name? ")
print("Nice to meet ya",name,"I'm Lynijah <3")
print(" ")
age=int(input("Hmmm, how old are you? "))
print("Oh okay",age,"is a good age. I'm 15 :)")
print(" ")
interests=input("So what do you do for fun? ")
print("Thats whats up! i never met someone who likes to",interests,". well, actually thats a lie. my uncle... nevermind im getting off topic.")
print(" ")
favorite_num=int(input("So what is your favorite number? "))
print("Ohhhhhh you one of those",favorite_num,"people... *gives side eye*")
print(" ")
print("Would you look at the time! I got to go walk my goldfish! cyaaaa")
