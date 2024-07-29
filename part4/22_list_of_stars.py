# Please write a function named list_of_stars, 
# which takes a list of integers as its argument. 
# The function should print out lines of star characters. 
# The numbers in the list specify how many stars each line 
# should contain.

# For example, with the function call 
# list_of_stars([3, 7, 1, 1, 2]) the following should be 
# printed out:

# Sample output
# ***
# *******
# *
# *
# **

def list_of_stars(list):
  index = 0
  for i in range(0, len(list)):
    print("*" * list[index])
    index += 1
list_of_stars([3, 7, 1, 1, 2])
  
