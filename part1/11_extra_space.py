# The program should print out exactly the following:

# Sample output
# my name is Tim Tester, I am 20 years old

# my skills are
# - python (beginner)
# - java (veteran)
# - programming (semiprofessional)

# I am looking for a job with a salary of 2000-3000 euros per month
name = "Tim Tester"
age = 20
skill1 = "python"
level1 = "beginner"
skill2 = "java"
level2 = "veteran"
skill3 = "programming"
level3 = "semiprofessional"
lower = 2000
upper = 3000

print(f"my name is {name}, I am {age} years old")
print()
print(f"my skills are")
print()
print(f"- {skill1} ({level1})")
print(f"- {skill2} ({level2})")
print(f"- {skill3} ({level3})")
print(f"I am looking for a job with a salary of {lower}-{upper} euros per month")