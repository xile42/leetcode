"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""


class Solution:

    def maxDepth(self, root: 'Node') -> int:

        def f(node):

            if node is None:
                return 0

            return 1 + max(f(child) for child in node.children) if node. children else 1

        return f(root)
