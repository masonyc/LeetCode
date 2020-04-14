# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        def recursive(root, val):
            if not root: return True
            if root.val != val:
                return False
            return recursive(root.left, val) and recursive(root.right, val)

        return recursive(root, root.val)
