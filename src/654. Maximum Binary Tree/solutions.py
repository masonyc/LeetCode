# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if not nums: return None
        rv = max(nums)
        rootIndex = nums.index(rv)
        root = TreeNode(rv)
        root.left = self.constructMaximumBinaryTree(nums[:rootIndex])
        root.right = self.constructMaximumBinaryTree(nums[rootIndex + 1:])
        return root

