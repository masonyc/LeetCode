# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        if not root: return None
        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)
        if root.val == target and root.left is root.right:
            return None
        return root
