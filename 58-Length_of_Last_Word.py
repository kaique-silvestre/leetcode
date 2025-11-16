# 58. Length of Last Word
"""
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.
"""
testcase01 = "Hello World"
testcase02 = "   fly me   to   the moon  "
testcase03 = "luffy is still joyboy"

# In the leetcode page of resulutions there are a lot
# of incredibles ways to resolve this
# That was the simples way to do it

# I thought that i would have problems with the empty spaces
# it seems that python resolve it, I do not think i will have
# this privilege in other programming languages  

def lengthOfLastWord(s: str) -> int:
    s = s.split()
    length = len(s)
    return len(s[length-1])

print(lengthOfLastWord(testcase01)) # 5
print(lengthOfLastWord(testcase02)) # 4
print(lengthOfLastWord(testcase03)) # 6
