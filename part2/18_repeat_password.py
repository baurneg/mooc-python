# Please write a program which asks the user for a password. 
# The program should then ask the user to type in the password again. 
# If the user types in something else than the first password, the program 
# should keep on asking until the user types the first password again correctly.

# Have a look at the expected behaviour below:

# Sample output
# Password: sekred
# Repeat password: secret
# They do not match!
# Repeat password: cantremember
# They do not match!
# Repeat password: sekred
# User account created!

password = input("Password: ")
while True:
  if password == "sekret"
  password_check = input("Repeat password: ")
  if password == "sekret" and password == password_check:
    print("User account created!")
    break
  else: 
    print("Do not match!")