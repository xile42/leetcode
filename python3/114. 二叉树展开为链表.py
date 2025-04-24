# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        if root is None:
            return None
        
        nodes = list()

        def f(node):

            nonlocal nodes

            if node is None:
                return

            nodes.append(node)
            f(node.left)
            f(node.right)

        f(root)

        for i, node in enumerate(nodes):
            node.left = None
            if i < len(nodes) - 1:
                node.right = nodes[i + 1]

