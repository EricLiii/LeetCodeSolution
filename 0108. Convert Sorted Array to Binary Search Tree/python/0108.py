# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution_1:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        mid=len(nums)//2
        root=TreeNode(nums[mid])
        if mid-1>=0:
            root.left=self.sortedArrayToBST(nums[:mid])
        if mid+1<len(nums):
            root.right=self.sortedArrayToBST(nums[mid+1:])

        return root
        
class Solution_2:
"""
Author: Zefeng

Runtime: 76 ms, faster than 82.20% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.
Memory Usage: 16.3 MB, less than 6.45% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.

递归. 记这个，更简洁.
"""
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root
