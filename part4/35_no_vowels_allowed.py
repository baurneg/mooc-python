# Please write a function named no_vowels, which takes 
# a string argument. The function returns a new string, 
# which should be the same as the original but with all 
# vowels removed.

# You can assume the string will contain only characters 
# from the lowercase English alphabet a...z.

# An example of expected behaviour:

# my_string = "this is an example"
# print(no_vowels(my_string))

# Sample output

# ths s n xmpl

def no_vowels(my_string: str)
    new_string = ""
    for character in my_string:
        if character == "a" or character == "e" or character == "i" or character == "o" or character == "u":
            continue
        else:
            new_string += character
            return new_string

if __name__ == "__main__":

    my_string = "this is an example"
    print(no_vowels(my_string))