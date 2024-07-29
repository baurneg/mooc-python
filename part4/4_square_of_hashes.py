# Please write a function named square_of_hashes, which draws a square of 
# hash characters. The function takes one argument, which determines the 
# length of the side of the square.

# The function should call the function line from the exercise above for 
# the actual printing out. Copy your solution to that exercise above the 
# code for this exercise. Please don't change anything in the line function.

# Some examples:

# square_of_hashes(5)
# print()
# square_of_hashes(3)
# Sample output
# #####
# #####
# #####
# #####
# #####

# ###
# ###
# ###
def line(integer, string):
  if string == "":
    string = "*"
  if len(string) > 1:
    print((string[0]) * integer)
  else:
    print(integer * string)


def square_of_hashes(number):
  for i in range(number):
    line(number, "#")

  
square_of_hashes(5)
print()
square_of_hashes(3)