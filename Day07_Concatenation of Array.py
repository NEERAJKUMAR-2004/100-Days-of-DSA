"""
LeetCode 1929. Concatenation of Array
Link: https://leetcode.com/problems/concatenation-of-array/

Given an integer array nums of length n, return an array ans of length 2n
where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n.

Example 1:
Input: nums = [1,2,1]
Output: [1,2,1,1,2,1]

Example 2:
Input: nums = [1,3,2,1]
Output: [1,3,2,1,1,3,2,1]
"""

class Solution(object):
    def getConcatenation(self, nums):
        n = len(nums)
        ans = [0] * (2 * n)
        for i in range(n):
            ans[i] = nums[i]
            ans[i + n] = nums[i]
        return ans
