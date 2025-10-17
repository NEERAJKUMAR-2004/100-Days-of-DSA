"""
LeetCode 1470 – Shuffle the Array
Link: https://leetcode.com/problems/shuffle-the-array/

Given an array 'nums' consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn], 
return the array in the form [x1,y1,x2,y2,...,xn,yn]. Solve manually without built-ins.
"""

class Solution(object):
    def shuffle(self, nums, n):
        result = []
        for i in range(n):
            result.append(nums[i])
            result.append(nums[i+n])
        return result
