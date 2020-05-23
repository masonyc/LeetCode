# DFS
def minDepth(self, root: TreeNode) -> int:
    def dfs(node: TreeNode, lvl: int) -> int:
        if not node:
            return inf
        if not node.left and not node.right:
            return lvl
        return min(dfs(node.left, lvl + 1), dfs(node.right, lvl + 1))

    if not root:
        return 0
    return dfs(root, 1)


# BFS
def minDepth(self, root: TreeNode) -> int:
    if not root:
        return 0
    s, lvl = [root], 1
    while s:
        temp = []
        for node in s:
            if not node.left and not node.right:
                return lvl
            if node.left: temp.append(node.left)
            if node.right: temp.append(node.right)
        lvl += 1
        s = temp
