# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def sumEvenGrandparent(self,
                           root: TreeNode,
                           parent: int = 1,
                           grandparent: int = 1) -> int:
        # 第一和第二层会被跳过 因为 grandparent %2==0
        return (self.sumEvenGrandparent(root.left, root.val, parent) +
                self.sumEvenGrandparent(root.right, root.val, parent) +
                root.val * (1 - grandparent % 2) if root else 0)
