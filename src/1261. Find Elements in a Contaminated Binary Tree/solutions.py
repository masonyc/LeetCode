# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class FindElements:
    def __init__(self, root: TreeNode):
        self.seen = set()

        def dfs(node, val=0):
            if node:
                node.val = val
                self.seen.append(val)
                dfs(node.left, val * 2 + 1)
                dfs(node.right, val * 2 + 2)

    def find(self, target: int) -> bool:
        return target in self.seen


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
