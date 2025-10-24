"""
LeetCode Problem #26: Remove Duplicates from Sorted Array

Problem Statement:
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. 
The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Note:
- Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
- The judge will test your solution with the provided test cases.
"""

class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0
            
        k = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[k] = nums[i]
                k += 1
        return k

Time Complexity: O(n)
Space Complexity: O(1)
