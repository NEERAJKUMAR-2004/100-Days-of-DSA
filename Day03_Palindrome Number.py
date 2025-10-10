"""
LeetCode 9. Palindrome Number
Link: https://leetcode.com/problems/palindrome-number/

Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:
Input: x = 121
Output: True

Example 2:
Input: x = -121
Output: False
Explanation: From left to right it reads -121. From right to left it becomes 121-. Not a palindrome.

Example 3:
Input: x = 10
Output: False
Explanation: Reads 01 from right to left. Not a palindrome.

Explanation:
If x is negative, return False.
Reverse the number and compare with the original.
If they are equal, the number is a palindrome.
"""

class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        original = x
        reversed_num = 0
        while x > 0:
            digit = x % 10
            reversed_num = reversed_num * 10 + digit
            x = x // 10
        return original == reversed_num
