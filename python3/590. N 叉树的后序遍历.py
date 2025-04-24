"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""


class Solution:

    def postorder(self, root: 'Node') -> List[int]:

        def f(node):

            if node is None:
                return list()

            children_result = list()
            if not node.children is None:
                for child in node.children:
                    children_result += f(child)

            return children_result + [node.val]

        return f(root)

        
