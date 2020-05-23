# BFS
def hasPathSum(self, root: TreeNode, sum: int) -> bool:
    if not root: return False
    s = [(root, sum)]
    while s:
        node, t = s.pop()
        t -= node.val
        if not node.left and not node.right and t == 0:
            return True
        if node.left: s.append((node.left, t))
        if node.right: s.append((node.right, t))
    return False


# DFS
def hasPathSum(self, root: TreeNode, sum: int) -> bool:
    if not root:
        return False
    sum -= root.val
    if not root.left and not root.right:
        return sum == 0
    return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)
