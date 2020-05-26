# BFS
# Time N
# Space N
def rightSideView(self, root: TreeNode) -> List[int]:
    if not root:
        return []
    deq, ans = deque([root]), []
    while deq:
        count = 0
        for _ in range(deq):
            node = deq.popleft()
            if count == 0:
                ans.append(node)
                count += 1
            if node.right:
                deq.append(node.right)
            if node.left:
                deq.append(node.left)
    return ans


# DFS
# Time N
# Space N
def rightSideView(self, root: TreeNode) -> List[int]:
    ans = []

    def dfs(node, lvl):
        if not node: return
        nonlocal ans
        if lvl > len(ans):
            ans.append(node.val)
        dfs(node.right, lvl + 1)
        dfs(node.left, lvl + 1)

    dfs(root, 1)
    return ans
