# Please write a program which asks the user to type in a sentence. 
# The program then prints out the first letter of each word in the sentence, 
# each letter on a separate line.

# An example of expected behaviour:

# Sample output
# Please type in a sentence: Humpty Dumpty sat on a wall
# H
# D
# s
# o
# a
# w
sentence = input("Please type in a sentence: ")
words = sentence.split()
for word in words:
  print(word[0])

  
#Humpty Dumpty sat on a wall

# sentence = input("Please type in a sentence: ")
 
# # Add a space at the start, to make handling sentence easier
# sentence = " " + sentence
 
# # Searching for indexes which are preceded by spaces
# index = 1
# while index < len(sentence):
#     if sentence[index-1] == " " and sentence[index] != " ":
#         print(sentence[index])
#     index += 1