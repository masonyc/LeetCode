class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root: return
        if root.val == val:
            return root
        return (self.searchBST(root.left, val)
                if val < root.val else self.searchBST(root.right, val))
