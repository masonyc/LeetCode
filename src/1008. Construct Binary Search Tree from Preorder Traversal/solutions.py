# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


 class Solution:
      def __init__(self):
         self.i=0
      def bstFromPreorder(self,preorder:List[int],upperBound:float = float("inf"))->TreeNode:
          if self.i == len(preorder) or preorder[self.i] > upperBound:
              return None
          root = TreeNode(preorder[self.i])
          self.i+=1
          root.left = self.bstFromPreorder(preorder,root.val)
          root.right = self.bstFromPreorder(preorder,upperBound)
          return root
#     def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        # if not preorder: return None
        # root = TreeNode(preorder[0])
        # left = list(filter(lambda x: x < root.val, preorder))
        # right = list(filter(lambda x: x > root.val, preorder))
        # root.left = self.bstFromPreorder(left)
        # root.right = self.bstFromPreorder(right)
        # return root
