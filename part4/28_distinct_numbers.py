# Please write a function named distinct_numbers, which takes 
# a list of integers as its argument. The function returns a new 
# list containing the numbers from the original list in order of 
# magnitude, and so that each distinct number is present only once.

# my_list = [3, 2, 2, 1, 3, 3, 1]
# print(distinct_numbers(my_list)) # [1, 2, 3]


my_list = [3, 2, 2, 1, 3, 3, 1]
another_list = [32, 32,42, 81, 13, 13, 134]
def distinct_numbers(my_list):
  unique = []
  for number in my_list:
    if number in unique:
      continue
    unique.append(number)
  print(sorted(unique))

distinct_numbers(my_list)
distinct_numbers(another_list)