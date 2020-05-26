def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
    def dfs(pre_left, pre_right, in_left, in_right):
        if pre_left > pre_right:
            return
        root_val = preorder[pre_left]
        root_index = d[root_val]

        node = TreeNode(root_val)
        node.left = dfs(pre_left + 1, pre_left + root_index - in_left, in_left,
                        root_index - 1)
        node.right = dfs(pre_left + root_index - in_left + 1, pre_right,
                         root_index + 1, in_right)
        return node

    d = {v: k for k, v in enumerate(inorder)}
    return dfs(0, len(d) - 1, 0, len(d) - 1)
