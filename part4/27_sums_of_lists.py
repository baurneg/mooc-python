# Please write a function named list_sum which takes two lists of 
# integers as arguments. The function returns a new list which 
# contains the sums of the items at each index in the two original 
# lists. You may assume both lists have the same number of items.

# An example of the function at work:

# a = [1, 2, 3]
# b = [7, 8, 9]
# print(list_sum(a, b)) # [8, 10, 12]


def list_sum(a, b):
    new_list = []
    index = 0
    while index < len(a):
        sum = (a[index] + b[index])
        index += 1
        new_list.append(sum)
    return new_list
        
    
if __name__ == "__main__":
    
    a = [1, 2, 3]
    b = [7, 8, 9]
    print(list_sum(a, b))