"""
Given an array of integers "nums" and an integer "target", return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""
# After studying the exercise i have learned that that's the right answer to it. Great Logic, Beautiful.

def TwoSum(target, array):
    # dict{NumbertoSum: IndexOfTheNumber}
    IndexDict = dict()
    for index, num in enumerate(array):
        if num in IndexDict:
            return IndexDict[num], index
        result = target - num 
        IndexDict[result] = array.index(num)
    return "There's no such sum that's equal to the target"


l1 = [2, 2, 7, 15, 7, 11, 7]

print(TwoSum(9, l1))
