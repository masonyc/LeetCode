# DFS
# TIME O(N)
# SPACE O(Height)
def distributeCoins(self, root: TreeNode) -> int:
    def dfs(node: TreeNode):
        if not node:
            return 0
        L = dfs(node.left)
        R = dfs(node.right)
        nonlocal ans
        ans += abs(L) + abs(R)
        return node.val + L + R - 1

    ans = 0
    dfs(root)
    return ans
