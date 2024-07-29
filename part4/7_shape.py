# Please write a function named shape, which takes four arguments. 
# The first two parameters specify a triangle, as above, and the 
# character used to draw it. The first parameter also specifies 
# the width of a rectangle, while the third parameter specifies 
# its height. The fourth parameter specifies the filler character 
# of the rectangle. The function prints first the triangle, and 
# then the rectangle below it.

# The function should call the function line from the exercise 
# above for the actual printing out. Copy your solution to that 
# exercise above the code for this exercise. Please don't change 
# anything in the line function.

# Some examples:

# shape(5, "X", 3, "*")
# print()
# shape(2, "o", 4, "+")
# print()
# shape(3, ".", 0, ",")
# Sample output
# X
# XX
# XXX
# XXXX
# XXXXX
# *****
# *****
# *****

# o
# oo
# ++
# ++
# ++
# ++

# .
# ..
# ...
def line(integer, string):
  if string == "":
    string = "*"
  if len(string) > 1:
    print((string[0]) * integer)
  else:
    print(integer * string)
    
def shape(tri_height, tri_character, rec_height, rec_character):
  start = 1
  for i in range(start, tri_height + 1):
    line(start, tri_character)
    start += 1
  for i in range(rec_height):
    line(tri_height, rec_character)

    
shape(5, "X", 3, "*")
print()
shape(2, "o", 4, "+")
print()
shape(3, ".", 0, ",")