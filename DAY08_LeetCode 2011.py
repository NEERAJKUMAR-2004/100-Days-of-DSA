"""
LeetCode 2011. Final Value of Variable After Performing Operations
Link: https://leetcode.com/problems/final-value-of-variable-after-performing-operations/

There is a variable x that starts at 0, and there are operations like "++X", "X++", "--X", "X--".
Return the final value of x after performing all the operations.

Example:
Input: operations = ["--X","X++","X++"]
Output: 1
"""

class Solution(object):
    def finalValueAfterOperations(self, operations):
        x = 0
        for op in operations:
            if op == "++X" or op == "X++":
                x += 1
            else:
                x -= 1
        return x
