# author: <name here>
# date: <date here>

# -------------------- Section 4 -------------------- #

# Input | ASCII Art


# Objectives:
#   1. Diamond
#       a. Define a function that accept the parameters listed below.
#           Name   | Type(s)         | Description
#           symbol | Integer / Float | The symbol used to create the diamond.
#
#           The function should print the chevron seen in the output below using the symbol.
#       b. Prompt input from the user in the form of a single character, save it to a variable.
#       c. Call the function you defined to create the diamond, sending the character as an argument.
#
#       HINT: Start with a smaller diamond! Then make it bigger once you figure out the pattern.
#
# ----- EXAMPLE OUTPUT ----- #
#   >> $
#
#           $
#          $$$
#         $$$$$
#        $$$$$$$
#       $$$$$$$$$
#      $$$$$$$$$$$
#     $$$$$$$$$$$$$
#      $$$$$$$$$$$
#       $$$$$$$$$
#        $$$$$$$
#         $$$$$
#          $$$
#           $
#
# ---- WRITE CODE BELOW ---- #
symbol=input("Enter a symbol: ")
def diamond(sym):
    print(" "*10 + symbol*1)
    print(" "*9 + symbol*3)
    print(" "*8 + symbol*5)
    print(" "*7 + symbol*7)
    print(" "*6 + symbol*9)
    print(" "*5 + symbol*11)
    print(" "*6 + symbol*9)
    print(" "*7 + symbol*7)
    print(" "*8 + symbol*5)
    print(" "*9 + symbol*3)
    print(" "*10 + symbol*1)
diamond(symbol)
print(" ")

#   2. Framed Diamond
#       a. Define a function that accept the parameters listed below.
#           Name   | Type(s)         | Description
#           symbol1 | Integer / Float | The symbol used to create the diamond.
#           symbol2 | Integer / Float | The symbol used to create the frame.
#
#           The function should print the chevron seen in the output below using the symbol.
#       b. Prompt input from the user in the form of a single character, save it to a variable.
#       c. Prompt input from the user in the form of a single character again, and save it to a second variable.
#       d. Call the function you defined to create the framed diamond, sending the characters as arguments.
#
#       HINT: Start with a smaller diamond! Then make it bigger once you figure out the pattern.
#
# ----- EXAMPLE OUTPUT ----- #
#   >> &
#   >> ~
#
#     ~~~~~~$~~~~~~
#     ~~~~~$$$~~~~~
#     ~~~~$$$$$~~~~
#     ~~~$$$$$$$~~~
#     ~~$$$$$$$$$~~
#     ~$$$$$$$$$$$~
#     $$$$$$$$$$$$$
#     ~$$$$$$$$$$$~
#     ~~$$$$$$$$$~~
#     ~~~$$$$$$$~~~
#     ~~~~$$$$$~~~~
#     ~~~~~$$$~~~~~
#     ~~~~~~$~~~~~~
#
# ---- WRITE CODE BELOW ---- #
print("Framed Diamond")
symbol1=input("Enter a symbol: ")
symbol2=input("Enter another symbol")
def diamond(a,b):
    print(symbol2*10 + symbol*1 + symbol2*10)
    print(symbol2*9 + symbol*3 + symbol2*9)
    print(symbol2*8 + symbol*5 + symbol2*8)
    print(symbol2*7 + symbol*7 + symbol2*7)
    print(symbol2*6 + symbol*9 + symbol2*6)
    print(symbol2*5 + symbol*11 + symbol2*5)
    print(symbol2*6 + symbol*9 + symbol2*6)
    print(symbol2*7 + symbol*7 + symbol2*7)
    print(symbol2*8 + symbol*5 + symbol2*8)
    print(symbol2*9 + symbol*3 + symbol2*9)
    print(symbol2*10 + symbol*1 + symbol2*10)
diamond(symbol1,symbol2)
print(" ")