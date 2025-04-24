# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:

        v = root.val

        def f(node):

            if node is None:
                return True

            if node.val != v:
                return False

            return f(node.left) and f(node.right)

        return f(root)
