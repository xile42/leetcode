# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        success = False

        def f(node, v):

            nonlocal success
            if success:
                return
            if node is None:
                return

            if node.left is None and node.right is None:
                if v + node.val == targetSum:
                    success = True
                    return
                return

            if node.left:
                f(node.left, v + node.val)
            if node.right:
                f(node.right, v + node.val)

            return

        f(root, 0)

        return success
