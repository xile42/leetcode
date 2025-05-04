# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:

        def f(n1, n2):

            if n1 is None and n2 is None:
                return None

            v = 0
            v += n1.val if n1 else 0
            v += n2.val if n2 else 0
            n = TreeNode(v)

            n.left = f(n1.left if n1 else None, n2.left if n2 else None)
            n.right = f(n1.right if n1 else None, n2.right if n2 else None)

            return n

        return f(root1, root2)
