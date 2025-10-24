"""
LeetCode Problem #169: Majority Element

Problem Statement:
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n/2⌋ times. 
You may assume that the majority element always exists in the array.

Note:
- The algorithm should run in O(n) time and O(1) space.
"""

class Solution(object):
    def majorityElement(self, nums):
        count = 0
        candidate = None
        
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
            
        return candidate

Time Complexity: O(n)
Space Complexity: O(1)
