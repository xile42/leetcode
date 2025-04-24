# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:

    def numColor(self, root: TreeNode) -> int:

        s = set()

        def f(node):

            nonlocal s
            
            if node is None:
                return

            s.add(node.val)
            
            f(node.left)
            f(node.right)

        f(root)

        return len(s)
