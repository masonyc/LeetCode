# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root: return
        if root.val == key:
            if root.left:
                left_most_right = root.left  #设左边的node
                while left_most_right.right:  #当node有右子树时
                    left_most_right = left_most_right.right
                left_most_right.right = root.right  #左边的右子树走完了，开始加root的右子节点到最后
                return root.left
            else:
                return root.right

        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            root.left = self.deleteNode(root.left, key)
        return root
