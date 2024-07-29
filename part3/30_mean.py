# Please write a function named mean, which takes three integer arguments. 
# The function should print out the arithmetic mean of the three arguments.

# mean(5, 3, 1)
# mean(10, 1, 1)
# Sample output
# 3.0
# 4.0

def mean(x, y, z):
    mean_value = (x + y + z)/3
    print(mean_value)
# Testing the function
# if __name__ == "__main__":
mean(1, 2, 3)