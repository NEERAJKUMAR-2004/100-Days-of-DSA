"""
LeetCode Problem #88: Merge Sorted Array

Problem Statement:
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, 
representing the number of elements in nums1 and nums2 respectively. Merge nums2 into nums1 as one sorted array.

Note:
- The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
- nums1 has a length of m + n, where the first m elements denote the elements that should be merged, 
  and the last n elements are set to 0 and should be ignored.

"""

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1  # last element of nums1
        j = n - 1  # last element of nums2  
        k = m + n - 1  # last position of nums1
        
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

Time Complexity: O(m + n)
Space Complexity: O(1)
