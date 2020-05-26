def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
    def helper(left, right):
        if left > right:
            return
        val = postorder.pop()
        node = TreeNode(val)
        ind = d[val]
        node.right = helper(ind + 1, right)
        node.left = helper(left, ind - 1)
        return node

    d = {v: k for k, v in enumerate(inorder)}
    return helper(0, len(d) - 1)
