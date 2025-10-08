"""
LeetCode 977. Squares of a Sorted Array
Link: https://leetcode.com/problems/squares-of-a-sorted-array/

Given an integer array nums sorted in non-decreasing order, return an array 
of the squares of each number sorted in non-decreasing order.

Example 1:
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
"""

class Solution(object):
    def sortedSquares(self, nums):
        n = len(nums)
        result = [0] * n
        left, right = 0, n - 1
        pos = n - 1
        
        while left <= right:
            left_square = nums[left] * nums[left]
            right_square = nums[right] * nums[right]
            
            if left_square > right_square:
                result[pos] = left_square
                left += 1
            else:
                result[pos] = right_square
                right -= 1
            pos -= 1
            
        return result
