'''
Given two int values, return their sum. Unless the two values are the same, then return double their sum.


sum_double(1, 2) → 3
sum_double(3, 2) → 5
sum_double(2, 2) → 8
'''

def sum_double(number1, number2):
    sum = number1 + number2
    if number1 == number2:
        sum = sum * 2
    return sum

print(sum_double(1, 2))
print(sum_double(3, 2))
print(sum_double(2, 2))