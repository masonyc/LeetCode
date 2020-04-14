class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def recursive(root, tail):
            if not root: return tail
            res = recursive(root.left, root)
            root.left = None
            root.right = recursive(root.right, tail)
            return res

        return recursive(root, None)
