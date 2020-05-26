def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
    def dfs(node: TreeNode):
        if not node: return None, 0
        L, LD = dfs(node.left)
        R, RD = dfs(node.right)
        if LD == RD:
            return node, LD + 1
        return (L, LD + 1) if LD > RD else (R, RD + 1)

    return dfs(root)[0]
