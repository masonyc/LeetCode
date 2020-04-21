# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        self.res = 0

        def dfs(node):
            if not node: return 0
            left, right = dfs(node.left), dfs(node.right)
            self.res += abs(left) + abs(right)
            return node.val - 1 + left + right

        dfs(root)
        return self.res
