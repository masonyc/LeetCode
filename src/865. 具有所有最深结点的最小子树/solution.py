def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
    def dfs(node: TreeNode):
        if not node: return None, 0
        l, l_lvl = dfs(node.left)
        r, r_lvl = dfs(node.right)
        if l_lvl == r_lvl:
            return (node, l_lvl + 1)
        return (l, l_lvl + 1) if l_lvl > r_lvl else (r, r_lvl + 1)

    return dfs(root)[0]
