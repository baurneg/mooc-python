# Please write a function named most_common_character, 
# which takes a string argument. The function returns 
# the character which has the most occurrences within 
# the string. If there are many characters with equally 
# many occurrences, the one which appears first in the 
# string should be returned.

# An example of expected behaviour:

# first_string = "abcdbde"
# print(most_common_character(first_string))

# second_string = "exemplaryelementary"
# print(most_common_character(second_string))

#def most_common_character(word):
#second_string = "exemplaryelementary"
#print(most_common_character(second_string))

word = "exemplaryelementary"
most_common = word[0]
for character in word:
  if word.count(character) > word.count(most_common):
    most_common = character
