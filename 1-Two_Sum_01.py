"""
Given an array of integers "nums" and an integer "target", return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""

# That was my first try doing leetcode and it took me something like 2 hours to make the exercise

def TwoSum(nums, target):
    cont = 0 # It gonna lock index by index of the array while the loop for test all possibles sum with it 
    while cont < len(nums):
        for num in nums:
            if cont == nums.index(num): # It tests if the "cont" and the "num" are in the same index
                continue
            # print(f'{nums[cont]} + {num} = {nums[cont] + num}'); #Easier visualization of what's happening 
            result = nums[cont] + num
            if result == target:
                return sorted((nums.index(num), cont))
        cont += 1 # Go to the next index
    return "There's no sum in the list that's equal to the target"
   

ArrayList = [3, 4, 9, 6, 4]
print(TwoSum(ArrayList, 8))

"""
Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
"""
