# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        ans = 0

        def f(node, mx, mn):

            if node is None:
                return

            nonlocal ans
            ans = max(ans, abs(mx - node.val), abs(mn - node.val))
            f(node.left, max(mx, node.val), min(mn, node.val))
            f(node.right, max(mx, node.val), min(mn, node.val))

        if root is None:
            return 0
        else:
            f(root, root.val, root.val)

        return ans
