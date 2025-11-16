# 1672. Richest Costumer Wealth
"""
You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the ith customer has in the jth bank. Return the wealth that the richest customer has.

A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.

"""

# Runtime: 0ms
# Memory: 17.8MB

testcase01 = [[1, 2, 3], [3, 2, 1]] 
testcase02 = [[1, 5], [7, 3], [3, 5]]
testcase03 = [[2, 8, 7], [7, 1, 3], [1, 9, 5]]  

def maximumWealth(accounts: list[list[int]]) -> int:
    # In the worst case (everything is 0) we return the first item
    richest_one = accounts[0][0]  
    for client in accounts: # It goes through all 2° dimensions arrays 
        richest_one = sum(client) if sum(client) > richest_one else richest_one 
    return richest_one



print(maximumWealth(testcase01))  # Output: 6
print(maximumWealth(testcase02))  # Output: 10
print(maximumWealth(testcase03))  # Output: 17

