# Please write a function named sum_of_positives, which takes 
# a list of integers as its argument. The function returns 
# the sum of the positive values in the list.

# my_list = [1, -2, 3, -4, 5]
# result = sum_of_positives(my_list)
# print("The result is", result)
# Sample output
# The result is 9

def sum_of_positives(my_list):
  positives_list = []
  sum = 0
  for number in my_list:
    if number > 0:
      positives_list.append(number)
  for i in positives_list:
    sum += i
  return sum

if __name__ == "__main__":
  my_list = [1, -2, 3, -4, 5]
  result = sum_of_positives(my_list)
  print("The result is", result)
