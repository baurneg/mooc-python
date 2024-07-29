# Please write a program which initialises a list with the 
# values [1, 2, 3, 4, 5]. Then the program should ask the 
# user for an index and a new value, replace the value at 
# the given index, and print the list again. This should 
# be looped over until the user gives -1 for the index. 
# You can assume all given index values will fall within 
# your list.

# An example execution of the program:

# Sample output
# Index: 0
# New value: 10
# [10, 2, 3, 4, 5]
# Index: 2
# New value: 250
# [10, 2, 250, 4, 5]
# Index: 4
# New value: -45
# [10, 2, 250, 4, -45]
# Index: -1

my_list = [1, 2, 3, 4, 5]
while True:
  index = int(input("Index: "))
  if index == -1:
    break
  new_value = int(input("New value: "))
  my_list[index] = new_value
  print(my_list)
  
# list = [1, 2, 3, 4, 5]
# while True:
#     index = int(input("Index: "))
#     if index == -1:
#         break
#     if index < 0 or index >= len(list):
#         print("Index is outside of the range of the list")
#         continue
#     value = int(input("New value: "))
#     list[index] = value
#     print(list)