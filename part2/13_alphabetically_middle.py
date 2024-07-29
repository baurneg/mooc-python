# Please write a program which asks the user for three letters. 
# The program should then print out whichever of the three letters 
# would be in the middle if the letters were in alphabetical order.

# You may assume the letters will be either all uppercase, or all 
# lowercase.

# Some examples of expected behaviour:

# Sample output
# 1st letter: x
# 2nd letter: c
# 3rd letter: p
# The letter in the middle is p

# Sample output
# 1st letter: C
# 2nd letter: B
# 3rd letter: A
# The letter in the middle is B

letter_1 = input("1st letter: ")
letter_2 = input("2nd letter: ")
letter_3 = input("3rd letter: ")
if letter_1 > letter_2 > letter_3 or letter_1 < letter_2 < letter_3 :
  print("The letter in the middle is ", letter_2)
elif letter_2 > letter_1 > letter_3 and letter_2 > letter_3 > letter_1:
  print("The letter in the middle is ", letter_3)
elif letter_2 < letter_3 < letter_1 and letter_2 < letter_1 < letter_3:
  print("The letter in the middle is ", letter_1)


