# 9. Palindrome Number
"""
Given an integer x, return true if x is a palindrome, and false otherwise.
"""
testcase01 = 121
testcase02 = -121
testcase03 = 10

def isPalindrome(x: int) -> bool:
    return True if str(x) == str(x)[::-1] else False

print(isPalindrome(testcase01)) # True
print(isPalindrome(testcase02)) # False 
print(isPalindrome(testcase03)) # False 
