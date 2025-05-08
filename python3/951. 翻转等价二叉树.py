# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        def f(n1, n2):

            if n1 is None and n2 is None:
                return True
            if not n1 or not n2 or n1.val != n2.val:
                return False

            return (f(n1.left, n2.left) and f(n1.right, n2.right)) or (f(n1.right, n2.left) and f(n1.left, n2.right))

        return f(root1, root2)
