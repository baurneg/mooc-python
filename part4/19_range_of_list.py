# Please write a function named range_of_list, which takes a list 
# of integers as an argument. The function returns the difference 
# between the smallest and the largest value in the list.

# my_list = [1, 2, 3, 4, 5]
# result = range_of_list(my_list))
# print("The range of the list is", result)
# Sample output
# The range of the list is 4

def range_of_list(my_list):
  return max(my_list) - min(my_list)

my_list = [1, 2, 3, 4, 5]
result = range_of_list(my_list)
print("The range of the list is", result)