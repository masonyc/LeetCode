# DFS
def deepestLeavesSum(self, root: TreeNode) -> int:
    self.depth = 0
    self.total = 0

    def dfs(node: TreeNode, lvl: int):
        if node:
            if lvl > self.depth:
                self.depth = lvl
                self.total = node.val
            elif lvl == self.depth:
                self.total += node.val
            dfs(node.left, lvl + 1)
            dfs(node.right, lvl + 1)

    dfs(root, 0)
    return self.total


# BFS
def deepestLeavesSum(self, root: TreeNode) -> int:
    if not root:
        return 0
    s = [root]
    while s:
        temp, total = [], 0
        for node in s:
            if not node.left and not node.right: total += node.val
            if node.left: temp.append(node.left)
            if node.right: temp.append(node.right)
        if not len(temp): return total
        s = temp
