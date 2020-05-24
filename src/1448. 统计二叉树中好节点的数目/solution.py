# DFS
# Time N
# Space N
def goodNodes(self, root: TreeNode) -> int:
    ans = 0

    def dfs(p, node):
        nonlocal ans
        if node:
            if node.val >= p:
                ans += 1
            nextv = max(node.val, p)
            dfs(nextv, node.left)
            dfs(nextv, node.right)

    dfs(-inf, root)
    return ans
