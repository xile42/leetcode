# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        def f(node):

            if node is None:
                return 0

            v = 0
            if low <= node.val <= high:
                v += node.val
            if low < node.val:
                v += f(node.left)
            if high > node.val:
                v += f(node.right)

            return v

        return f(root)
