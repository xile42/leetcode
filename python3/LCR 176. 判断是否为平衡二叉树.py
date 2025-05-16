# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        success = True

        def f(node):

            nonlocal success
            if not success:
                return 0

            if node is None:
                return 0

            left = f(node.left)
            right = f(node.right)
            if abs(left - right) > 1:
                success = False
                return 0

            return 1 + max(left, right)

        f(root)

        return success
