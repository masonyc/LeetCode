def flatten(self, root: TreeNode) -> None:
    """
    Do not return anything, modify root in-place instead.
    """
    while root:
        if root.left:
            mostRightInLeft = root.left
            while mostRightInLeft.right:
                mostRightInLeft = mostRightInLeft.right
            mostRightInLeft.right = root.right
            root.right = root.left
            root.left = None
        root = root.right

