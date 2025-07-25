# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def flipTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def f(node):

            if node is None:
                return node

            left = f(node.left)
            right = f(node.right)
            node.left = right
            node.right = left

            return node

        return f(root)
