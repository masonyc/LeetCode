# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        #递归法
        res = []

        def dfs(node, level=0):
            if node:
                if len(res) <= level:
                    res.append([0, 0])
                res[level][0] += node.val
                res[level][1] += 1
                dfs(node.left, level + 1)
                dfs(node.right, level + 1)

        dfs(root)
        return (s / c for s, c in res)


# 迭代法
# if not root:return []
# queue, res= [root],[]

# while queue:
#     current_level = 0
#     next_level = []
#     for node in queue:
#         current_level += node.val
#         if node.left:
#             next_level.append(node.left)
#         if node.right:
#             next_level.append(node.right)
#     res.append(current_level/len(queue))
#     queue = next_level
# return res
