import List

# Definition for a Node.


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        result = []
        if root == None:
            return result
        self.recursion(root, result)
        return result

    def recursion(self, root: 'Node', result: List[int]):
        for child in root.children:
            self.recursion(child, result)
        result.append(root.val)
        return result
