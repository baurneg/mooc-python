# Please write a new version of the program in the previous exercise. 
# In addition to the result it should also print out the calculation 
# performed:

# Sample output
# Limit: 2
# The consecutive sum: 1 + 2 = 3

# Sample output
# Limit: 10
# The consecutive sum: 1 + 2 + 3 + 4 = 10

# Sample output
# Limit: 18
# The consecutive sum: 1 + 2 + 3 + 4 + 5 + 6 = 21

# You may assume the number typed in by the user is always equal 
# to 2 or higher.

limit = int(input("Limit: "))
sum = 0
number = 0
statement = "The consecutive sum: "
while sum < limit:
  sum += number
  number += 1
  statement += f"{number} + "
print(f"{statement} = {sum}")


# limit = int(input("Limit: "))
# total_sum = 0
# number = 0
# sum_sequence = ""
# while total_sum < limit:
#     number += 1
#     total_sum += number
#     if total_sum < limit:
#         sum_sequence += str(number) + " + "
#     else:
#         sum_sequence += str(number)

# print("The consecutive sum:", sum_sequence, "=", total_sum)