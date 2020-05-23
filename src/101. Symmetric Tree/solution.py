# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # BFS
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        dq = deque()
        dq.append(root)
        dq.append(root)
        while dq:
            l = dq.pop()
            r = dq.pop()
            if not l and not r: continue
            if not l or not r: break
            if l.val != r.val: break
            dq.append(l.left)
            dq.append(r.right)
            dq.append(l.right)
            dq.append(r.left)
        return True

    ''' dfs
    def isSymmetric(self, root: TreeNode) -> bool:
        def dfs(l: TreeNode, r: TreeNode) -> bool:
            if not l and not r:
                return True
            if not l or not r:
                return False
            return (l.val == r.val and dfs(l.left, r.right)
                    and dfs(l.right, r.left))

        if not root:
            return True
        return dfs(root.left, root.right)
    '''
