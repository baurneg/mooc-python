# Please write a program which first asks the user for the number of 
# items to be added. Then the program should ask for the given number 
# of values, one by one, and add them to a list in the order they were 
# typed in. Finally, the list is printed out.

# An example of expected behaviour:

# Sample output
# How many items: 3
# Item 1: 10
# Item 2: 250
# Item 3: 34
# [10, 250, 34]


items = int(input("How many items: "))
count = 0
item = 0
item_list = []
while count < items:
  count += 1
  item = int(input(f"Item {count}: "))
  
  item_list.append(item)

print(item_list)


# numbers = int(input("How many items: "))
# list = []
 
# while len(list) < numbers:
#     number = int(input(f"Item {len(list) + 1}: "))
#     list.append(number)
 
# print(list)
 