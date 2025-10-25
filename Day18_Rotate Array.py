"""
LeetCode Problem #189: Rotate Array

Problem Statement:
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

Note:
- Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
- Could you do it in-place with O(1) extra space?
"""

class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        k = k % n  
        
        self.reverse(nums, 0, n-1)
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, n-1)
    
    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

Time Complexity: O(n)
Space Complexity: O(1)
