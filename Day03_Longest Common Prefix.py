"""
LeetCode 14. Longest Common Prefix
Link: https://leetcode.com/problems/longest-common-prefix/

Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string.

Example 1:
Input: ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: ["dog","racecar","car"]
Output: ""

Explanation:
Start with the first word as prefix.
Compare it with each other word, cutting letters from the end until all words start with it.
The remaining prefix is the longest common prefix.
"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        prefix = strs[0]
        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix
