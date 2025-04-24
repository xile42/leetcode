# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def evaluateTree(self, root: Optional[TreeNode]) -> bool:

        def f(node):

            v = node.val
            if v == 0 or v == 1:
                return v == 1

            if v == 2:
                return f(node.left) or f(node.right)

            return f(node.left) and f(node.right)

        ans = f(root)

        return ans
