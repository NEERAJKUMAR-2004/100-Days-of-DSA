"""
LeetCode 1512. Number of Good Pairs
Link: https://leetcode.com/problems/number-of-good-pairs/

Given an array of integers nums, return the number of good pairs.
A pair (i, j) is called good if nums[i] == nums[j] and i < j.

Example:
Input: nums = [1,2,3,1,1,3]
Output: 4
"""

class Solution(object):
    def numIdenticalPairs(self, nums):
        count = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    count += 1
        return count
