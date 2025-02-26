# Please write a function named same_chars, which takes one 
# string and two integers as arguments. The integers refer 
# to indexes within the string. The function should return 
# True if the two characters at the indexes specified are 
# the same. Otherwise, and especially if either of the indexes 
# falls outside the scope of the string, the function returns False.

# Some examples of how the function is used:

# # same characters m and m
# print(same_chars("programmer", 6, 7)) # True

# # different characters p and r
# print(same_chars("programmer", 0, 4)) # False

# # the second index is not within the string
# print(same_chars("programmer", 0, 12)) # False

def same_chars(string, num1, num2):
    if (num2 < 0 or num2 >= len(string)) or (num1 < 0 or num1 >= len(string)):
        return False
    return string[num1] == string[num2]

if __name__ == "__main__":
    print(same_chars("coder", 1, 2))  # False
    print(same_chars("programmer", 6, 7))  # True
    print(same_chars("programmer", 0, 4))  # True
    print(same_chars("programmer", 0, 12))  # False
    print(same_chars("abc", 0, 3))  # False