# -*- coding:utf-8 -*-


# Write a function that reverses a string. The input string is given as an array of characters char[].
#
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
#
# You may assume all the characters consist of printable ascii characters.
#
#  
#
#
# Example 1:
#
#
# Input: ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
#
#
#
# Example 2:
#
#
# Input: ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]
#
#
#
#


class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        reverse_s=[]
        length=len(s)
        for i in range(length):
            reverse_s.append(s[length-i-1])
        return ''.join(reverse_s)
            
