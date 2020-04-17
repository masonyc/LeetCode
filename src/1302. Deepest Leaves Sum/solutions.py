# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        if not root:
            return 0
        cur_lvl, ans = [root], 0
        while cur_lvl:
            next_lvl = []
            ans = 0
            for node in cur_lvl:
                if node.left:
                    next_lvl.append(node.left)
                if node.right:
                    next_lvl.append(node.right)
                if not node.left and not node.right:
                    ans += node.val
            cur_lvl = next_lvl
        return ans
