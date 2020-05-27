def sumNumbers(self, root: TreeNode) -> int:
    def dfs(node: TreeNode, total: int):
        if not node:
            return 0
        if not node.left and not node.right:
            return total * 10 + node.val
        return (dfs(node.left, total * 10 + node.val) +
                dfs(node.right, total * 10 + node.val))

    return dfs(root, 0)
