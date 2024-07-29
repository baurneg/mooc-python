# Please write a function named hash_square(length), which takes an integer argument. 
# The function prints out a square of hash characters, and the argument specifies 
# the length of the side of the square.

# hash_square(3)
# print()
# hash_square(5)
# Sample output
# ###
# ###
# ###

# #####
# #####
# #####
# #####
# #####

def hash_square(length):
  for x in range(length):
    print("#"*length)
hash_square(3)
hash_square(20)


# def hash_square(size):
#     tows = size
#     while tows > 0:
#         print("#" * size)
#         tows -= 1
 
# if __name__ == "__main__":
#     hash_square(5)
 