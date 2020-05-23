# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isBalanced_v2(self, root: TreeNode) -> bool:
        def dfs(node: TreeNode) -> int:
            if not node:
                return 0
            left = dfs(node.left)
            if left == -1: return -1
            right = dfs(node.right)
            if right == -1: return -1
            return max(left, right) + 1 if abs(left - right) <= 1 else -1

        return dfs(root) != -1

    def isBalanced_v1(self, root: TreeNode) -> bool:
        def dfs(node: TreeNode) -> int:
            if not node:
                return 0
            return max(dfs(node.left), dfs(node.right)) + 1

        if not root:
            return True
        return abs(dfs(root.left) -
                   dfs(root.right)) <= 1 and self.isBalanced_v1(
                       root.left) and self.isBalanced_v1(root.right)
