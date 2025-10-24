"""
LeetCode 1720 – Decode XORed Array
Link: https://leetcode.com/problems/decode-xored-array/

You are given an encoded array 'encoded' and an integer 'first'. 
encoded[i] = arr[i] XOR arr[i+1]. Return the original array 'arr'.
Solve manually without built-ins.
"""

class Solution(object):
    def decode(self, encoded, first):
        arr = [first]
        for i in range(len(encoded)):
            next_element = arr[i] ^ encoded[i]
            arr.append(next_element)
        return arr
