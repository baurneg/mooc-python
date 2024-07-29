# Please write a program which asks the user for words. 
# If the user types in a word for the second time, the 
# program should print out the number of different words 
# typed in, and exit.

# Sample output
# Word: once
# Word: upon
# Word: a
# Word: time
# Word: upon
# You typed in 4 different words
sentence = []
while True:
  word = input("Word: ")
  sentence.append(word)
  if len(sentence) != len(set(sentence)):
    print(f"You typed in {len(sentence) - 1} different words")
    break