# 66. Plus one
"""
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.
"""

testcase01 = [1, 2, 3]
testcase02 = [4, 3, 2, 1]
testcase03 = [9]

# I saw most people doing a reverse loop
# And checking if the value was 9
# if it was they would turn it to 0 and carry 1 to the next number
# It just seemed easier to me to transform the value to int and add 1 

# Iniatilly I though my way would cost more ms to the computer 
# but acordding to leetcode it was 0ms like the other ones 

def plusOne(digits: list[int]) -> list[int]:
    var = ''
    for item in digits:
        var += str(item)
    var = str(int(var) + 1)
    var = [int(number) for number in var]
    return var

print(plusOne(testcase01)) # [1, 2, 4]
print(plusOne(testcase02)) # [4, 3, 2, 2]
print(plusOne(testcase03)) # [1, 0]
