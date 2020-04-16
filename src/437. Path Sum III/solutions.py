# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        self.res = 0
        cache = {0: 1}
        self.dfs(root, sum, 0, cache)
        return self.res

    def dfs(self, root, target, currentSum, cache):
        if not root:
            return
        currentSum += root.val
        oldPathSum = currentSum - target
        self.res += cache.get(oldPathSum, 0)
        cache[currentSum] = cache.get(currentSum, 0) + 1
        self.dfs(root.left, target, currentSum, cache)
        self.dfs(root.right, target, currentSum, cache)
        cache[currentSum] -= 1
