# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        s = []
        prev = float('-inf')
        ans = float('inf')
        while root or s:
            while root:
                s.append(root)
                root = root.left
            left_most = s.pop()
            ans = min(ans, left_most.val - prev)
            prev = left_most.val
            root = left_most.right
        return ans
