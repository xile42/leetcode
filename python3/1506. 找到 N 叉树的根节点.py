"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []
"""


class Solution:

    def findRoot(self, tree: List['Node']) -> 'Node':

        _all, child = set(), set()
        for node in tree:
            _all.add(node.val)
            for child_node in node.children:
                child.add(child_node.val)

        tar = list(_all - child)[0]
        for node in tree:
            if node.val == tar:
                return node
