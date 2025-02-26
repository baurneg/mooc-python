# Please write a program which asks the user for a positive integer number.
# The program then prints out a list of multiplication operations until 
# both operands reach the number given by the user. See the examples below 
# for details:

# Sample output
# Please type in a number: 2
# 1 x 1 = 1
# 1 x 2 = 2
# 2 x 1 = 2
# 2 x 2 = 4

# Sample output
# Please type in a number: 3
# 1 x 1 = 1
# 1 x 2 = 2
# 1 x 3 = 3
# 2 x 1 = 2
# 2 x 2 = 4
# 2 x 3 = 6
# 3 x 1 = 3
# 3 x 2 = 6
# 3 x 3 = 9

number = int(input("Please type in a number: "))

for i in range(1, number+1):
  for x in range(1, number+1):
    print(f"{i} x {x} = {i * x}")
    
    
# number = int(input("Please type in a number: "))
# counter1 = 1
# while counter1 <= number:
#     counter2 = 1
#     while counter2 <= number:
#         print(f"{counter1} x {counter2} = {counter1*counter2}")
#         counter2 += 1
#     counter1 += 1