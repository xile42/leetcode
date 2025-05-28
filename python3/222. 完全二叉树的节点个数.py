# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def countNodes(self, root: Optional[TreeNode]) -> int:

        def f(node):

            if node is None:
                return 0

            return 1 + f(node.left) + f(node.right)

        return f(root)
