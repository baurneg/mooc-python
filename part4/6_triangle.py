# Please write a function named triangle, which draws a triangle 
# of hashes, and takes one argument. The triangle should be as 
# tall and as wide as the value of the argument.

# The function should call the function line from the exercise 
# above for the actual printing out. Copy your solution to that 
# exercise above the code for this exercise. Please don't change 
# anything in the line function.

# Some examples:

# triangle(6)
# print()
# triangle(3)
# Sample output
# #
# ##
# ###
# ####
# #####
# ######

# #
# ##
# ###

def line(integer, string):
  if string == "":
    string = "*"
  if len(string) > 1:
    print((string[0]) * integer)
  else:
    print(integer * string)

def triangle(integer):
  start = 1
  for i in range(start, integer + 1):
    line(start, "#")
    start += 1

triangle(6)
print()
triangle(3)