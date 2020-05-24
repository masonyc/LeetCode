# DFS
def sumEvenGrandparent(self, root: TreeNode) -> int:
    res = 0

    def dfs(gp, p, node):
        if not node:
            return
        if gp % 2 == 0:
            nonlocal res
            res += node.val
        dfs(p, node.val, node.left)
        dfs(p, node.val, node.right)

    dfs(1, 1, root)
    return res


# BFS
def sumEvenGrandparent(self, root: TreeNode) -> int:
    if not root:
        return 0
    s, ans = [root], 0
    while s:
        node = s.pop()
        if node.val % 2 == 0:
            if node.left:
                if node.left.left:
                    ans += node.left.left.val
                if node.left.right:
                    ans += node.left.right.val
            if node.right:
                if node.right.left:
                    ans += node.right.left.val
                if node.right.right:
                    ans += node.right.right.val
        if node.left: s.append(node.left)
        if node.right: s.append(node.right)
    return ans
