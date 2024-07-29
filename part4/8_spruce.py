# Please write a function named spruce, which takes one argument. 
# The function prints out the text a spruce!, and the a spruce tree, 
# the size of which is specified by the argument.

# Calling spruce(3) should print out

# Sample output
# a spruce!
#   *
# ***
# *****
#   *
# Calling spruce(5) should print out

# Sample output
# a spruce!
#     *
#   ***
#   *****
# *******
# *********
#     *
# NB: to the left of the spruce there should be exactly the right 
# amount of whitespace. If the shape of the spruce looks correct, 
# but the left edge of the tree is not touching the left edge of 
# the text area in the terminal, the tests will not accept the solution.

def spruce(size):
  print("a spruce!")
  start = 0
  space = size
  while start <= size and space > 0:
    
    print((space - 1) * " " + "*" + "*" * start + "*" * start)
    space -= 1
    start += 1
  print((size - 1) * " " + "*")


spruce(5)
print()
spruce(3)
    
# def spruce(height):
#     print("a spruce!")
#     i = 1
#     while i <= height:
#         empty = height - i
#         stars = 2 * i - 1
#         print(" " * empty + "*" * stars)
#         i += 1
#     print(" " * (height - 1) + "*")