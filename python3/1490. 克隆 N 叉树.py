"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:

    def cloneTree(self, root: 'Node') -> 'Node':

        def f(node):

            if node is None:
                return None

            ans = Node(val=node.val)
            for child in node.children:
                ans.children.append(f(child))

            return ans

        return f(root)
