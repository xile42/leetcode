# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def longestZigZag(self, root: Optional[TreeNode]) -> int:

        ans = 0

        @cache
        def f(node, l, r):

            if node is None:
                return 0

            nonlocal ans
            ans = max(ans, l, r)
            if node.left:
                f(node.left, r + 1, 0)
            if node.right:
                f(node.right, 0, l + 1)

        f(root, 0, 0)

        return ans
