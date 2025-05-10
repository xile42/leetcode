# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def maxProduct(self, root: Optional[TreeNode]) -> int:

        def f(node):

            if node is None:
                return 0

            return node.val + f(node.left) + f(node.right)

        s = f(root)
        ans = -inf
        base = 10 ** 9 + 7

        def g(node):

            nonlocal ans
            if node is None:
                return 0

            left = g(node.left)
            right = g(node.right)
            ans = max(ans, (left * (s - left)))
            ans = max(ans, (right * (s - right)))

            return node.val + left + right

        g(root)

        return ans % base
