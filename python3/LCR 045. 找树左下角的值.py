# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def findBottomLeftValue(self, root: TreeNode) -> int:

        mx = -inf
        ans = None

        def f(node, d):

            nonlocal ans, mx
            if node is None:
                return

            if d > mx:
                ans = node.val
                mx = d

            f(node.left, d + 1)
            f(node.right, d + 1)

        f(root, 0)

        return ans
