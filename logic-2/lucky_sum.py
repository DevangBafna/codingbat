'''
Given 3 int values, a b c, return their sum. However, if one of the values is 13 then it does not count towards the sum and values to its right do not count. So for example, if b is 13, then both b and c do not count.

lucky_sum(1, 2, 3) → 6
lucky_sum(1, 2, 13) → 3
lucky_sum(1, 13, 3) → 1
'''

def lucky_sum(int1, int2, int3):
    if int1 == 13:
        sum = 0
        return sum
    if int2 == 13:
        sum = int1
        return sum
    if int3 == 13:
        sum = int1 + int2
        return sum
    return int1 + int2 + int3

print(lucky_sum(1, 2, 3))
print(lucky_sum(1, 2, 13))
print(lucky_sum(1, 13, 3))