import Collections


class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res, queue = [], Collections.deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            res.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return res
