# Please write a function named length_of_longest, 
# which takes a list of strings as its argument. 
# The function returns the length of the longest string.

# my_list = ["first", "second", "fourth", "eleventh"]

# result = length_of_longest(my_list)
# print(result)
# my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

# result = length_of_longest(my_list)
# print(result)
# Sample output
# 8
# 7

def length_of_longest(my_list):
  my_list.sort(key = len, reverse = True)
  return (len(my_list[0]))

my_list = ["first", "second", "fourth", "eleventh"]  
result = length_of_longest(my_list)
print(result)

my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

result = length_of_longest(my_list)
print(result)
