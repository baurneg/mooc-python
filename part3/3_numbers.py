# Please write a program which asks the user for a number. 
# The program then prints out all integer numbers greater than 
# zero but smaller than the input.

# Sample output
# Upper limit: 5
# 1
# 2
# 3
# 4
number = 1
limit = int(input("Upper limit: "))
while number < limit:
  print(number)
  number += 1