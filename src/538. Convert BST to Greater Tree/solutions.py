# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        if not root: return None

        def dfs(node: TreeNode, prev: int):
            if not node: return prev
            val = dfs(node.right, prev)
            node.val += val
            return dfs(node.left, node.val)

        dfs(root, 0)
        return root
