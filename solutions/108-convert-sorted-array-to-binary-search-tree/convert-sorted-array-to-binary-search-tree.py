# -*- coding:utf-8 -*-


# Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
#
# For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
#
# Example:
#
#
# Given the sorted array: [-10,-3,0,5,9],
#
# One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:
#
#       0
#      / \
#    -3   9
#    /   /
#  -10  5
#
#


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if nums==[]:
            return None
        l=len(nums)
        if l%2==0:
            splitIndex=l/2
        else:
            splitIndex=(l-1)/2
        root=TreeNode(nums[splitIndex])
        root.left=Solution.sortedArrayToBST(self, nums[:splitIndex])
        root.right=Solution.sortedArrayToBST(self, nums[splitIndex+1:])
        return root
