'''
Given an array of ints, return True if the array contains a 2 next to a 2 somewhere.


has22([1, 2, 2]) → True
has22([1, 2, 1, 2]) → False
has22([2, 1, 2]) → False
'''

def has22(array_int):
    for i in range(len(array_int)-1):
        if (array_int[i] == 2 and array_int[i + 1] == 2):
            return True
    return False


print(has22([1, 2, 2]))
print(has22([1, 2, 1, 2]))
print(has22([2, 1, 2]))