class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        # 迭代法
        if not root: return []
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            res.append(node.val)
            for child in reversed(node.children):
                stack.append(child)
        return res


# 递归法
# res = []

# def recursive(node: 'Node'):
#     if not node: return
#     res.append(node.val)
#     for child in node.children:
#         recursive(child)

# recursive(root)
# return res
