# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import List


class Solution:
    def buildTree(self,
                  preorder: List[int],
                  inorder: List[int]) -> TreeNode:
        self.indexDict, self.preorder = {}, preorder
        for i in range(len(inorder)):
            self.indexDict[inorder[i]] = i
        return self.recursive(0, 0, len(inorder) - 1)

    def recursive(self, preroot, start, end):
        if start > end:
            return None  # out of index
        root = TreeNode(self.preorder[preroot])
        i = self.indexDict[root.val]
        root.left = self.recursive(preroot + 1, start, i - 1)
        root.right = self.recursive(i - start + preroot + 1, i + 1, end)
        return root
