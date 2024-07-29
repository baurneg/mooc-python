# Please write a program which asks the user to choose between addition 
# and removal. Depending on the choice, the program adds an item to or 
# removes an item from the end of a list. The item that is added must 
# always be one greater than the last item in the list. The first item 
# to be added must be 1.

# The list is printed out in the beginning and after each operation. 
# Have a look at the example execution below:

# Sample output
# The list is now []
# a(d)d, (r)emove or e(x)it: d
# The list is now [1]
# a(d)d, (r)emove or e(x)it: d
# The list is now [1, 2]
# a(d)d, (r)emove or e(x)it: d
# The list is now [1, 2, 3]
# a(d)d, (r)emove or e(x)it: r
# The list is now [1, 2]
# a(d)d, (r)emove or e(x)it: d
# The list is now [1, 2, 3]
# a(d)d, (r)emove or e(x)it: x
# Bye!
number = 1
list = []
while True:
  print(f"The list is now {list}")
  action = input("a(d)d, (r)emove or e(x)it: ")
  if action.lower() == "x":
    print("Bye!")
    break
  if action.lower() == "d":
    list.append(number)
    number += 1
    
  if action.lower() == "r":
    list.pop(len(list) - 1)
    number = len(list) + 1
  
