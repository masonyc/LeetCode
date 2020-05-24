# DFS
def findBottomLeftValue(self, root: TreeNode) -> int:
    def dfs(node: TreeNode, level: int):
        nonlocal maxDepth
        nonlocal ans
        if not node:
            return
        if level > maxDepth:
            maxDepth = level
            ans = node.val
        dfs(node.left, level + 1)
        dfs(node.right, level + 1)

    maxDepth, ans = -1, 0
    dfs(root, 0)
    return ans


# BFS
# 时间复杂度：O(n)，遍历完所有的树结点。
# 空间复杂度：O(max(layer))，某层最大结点个数。
def findBottomLeftValue(self, root: TreeNode) -> int:
    if not root:
        return 0
    deq = deque([root])
    while deq:
        leftmost = deq[0].val
        for _ in range(len(deq)):
            node = deq.popleft()
            if node.left:
                deq.append(node.left)
            if node.right:
                deq.append(node.right)
    return leftmost
