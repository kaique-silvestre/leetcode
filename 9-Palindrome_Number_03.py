# 9. Palindrome Number
"""
Given an integer x, return true if x is a palindrome, and false otherwise.
"""

# That's is the right way to do it using math
# Dividing a number by then will always cut off the last digit, returning the rest to us
# Getting mod 10 of a number will always have its last digit as result, returning it to us   

testcase01 = 121
testcase02 = -121
testcase03 = 10

def isPalindrome(num: int) -> bool:
  inverse = 0
  rest = num if num > 0 else 0

  while rest:
    digit = rest % 10
    rest = rest // 10
    inverse = inverse * 10 + digit
  return inverse == num


print(isPalindrome(testcase01)) # True
print(isPalindrome(testcase02)) # False 
print(isPalindrome(testcase03)) # False 