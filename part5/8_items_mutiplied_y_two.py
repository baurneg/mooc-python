# Please write a function named double_items(numbers: list), 
# which takes a list of integers as its argument.

# The function should return a new list, which contains all 
# values from the original list doubled. The function should 
# not change the original list.

# An example of the function at work:

# if __name__ == "__main__":
#     numbers = [2, 4, 5, 3, 11, -4]
#     numbers_doubled = double_items(numbers)
#     print("original:", numbers)
#     print("doubled:", numbers_doubled)
# Sample output
# original: [2, 4, 5, 3, 11, -4]
# doubled: [4, 8, 10, 6, 22, -8]

def double_items(numbers: list):
  new_list = []
  for number in numbers:
#    x = number * 2
    new_list.append(number * 2)
  return new_list

numbers = [2, 4, 5, 3, 11, -4]
numbers_doubled = double_items(numbers)
print("original:", numbers)
print("doubled:", numbers_doubled)