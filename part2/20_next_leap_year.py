# Please write a program which asks the user for a year, 
# and prints out the next leap year.

# Sample output
# Year: 2023
# The next leap year after 2023 is 2024

# If the user inputs a year which is a leap year 
# (such as 2024), the program should print out the 
# following leap year:

# Sample output
# Year: 2024
# The next leap year after 2024 is 2028

year = int(input("Year: "))
count = 0
while True: 
#  leap_year = year % 4 == 0 and year % 100 != 0
  year += 1
  count += 1
  if year % 4 == 0 and (year % 400 == 0 or year % 100 != 0):
    print(f"The next leap year after {year - count} is {year}")
    break