# Please write a function named 
# count_matching_elements(my_matrix: list, element: int), 
# which takes a two-dimensional array of integers and 
# a single integer value as its arguments. The function 
# then counts how many elements within the matrix match 
# the argument value.

# An example of how the function should work:

# m = [[1, 2, 1], [0, 3, 4], [1, 0, 0]]
# print(count_matching_elements(m, 1))
# Sample output
# 3
m = [[1, 2, 3], [2, 3, 1], [4, 5, 6]]
#def count_matching_elements(my_matrix: list, element: int):
count = 0
for row in m:
  for element in row:
    if element == 2:
      count += 1
    print(count)  
#      return count
#if __name__ == "__main__":
#  m = [[1, 2, 1], [0, 3, 4], [1, 0, 0]]
#  print(count_matching_elements(m, 1))