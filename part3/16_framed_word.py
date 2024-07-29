# Please write a program which asks the user for a string and then 
# prints out a frame of * characters with the word in the centre. 
# The width of the frame should be 30 characters. You may assume the 
# input string will always fit inside the frame.

# If the length of the input string is an odd number, you may print 
# out the word in either of the two possible centre locations.

# Sample output
# Word: testing

# ******************************
# *          testing           *
# ******************************
# Sample output
# Word: python

# ******************************
# *           python           *
# ******************************

word = input("Word: ")
spaces = 28 - len(word)
if spaces % 2 != 0:
    print(30 * "*")
    print("*" + int(spaces/2) * " " + word + " " + int(spaces/2) * " " + "*")
    print(30 * "*")
else: 
    print(30 * "*")
    print("*" + int(spaces/2) * " " + word + int(spaces/2) * " " + "*")
    print(30 * "*")
    
    
# word = input("Word: ")
 
# print("*" * 30)
# spaces_at_start = (28 - len(word)) // 2
# spaces_at_end = spaces_at_start
 
# # If the word length is odd, one is added to the spaces at the end of the word
# # to get all 30 characters filled
# if len(word) % 2 != 0:
#     spaces_at_end += 1
 
# print("*" + spaces_at_start * " " + word + spaces_at_end * " " + "*")
# print("*" * 30)
 