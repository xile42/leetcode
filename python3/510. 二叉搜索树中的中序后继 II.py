"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""


class Solution:

    def inorderSuccessor(self, node: 'Node') -> 'Optional[Node]':

        def f(node):

            if node is None:
                return []

            return f(node.left) + [node.val] + f(node.right)

        head = node
        while head.parent:
            head = head.parent
        path = f(head)
        index = path.index(node.val)

        return None if index == len(path) - 1 else Node(path[index+1])
