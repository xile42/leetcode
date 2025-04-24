# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def closestValue(self, root: Optional[TreeNode], target: float) -> int:

        mn, v = inf, inf

        def f(node):

            nonlocal mn, v

            if node is None:
                return

            cur = abs(node.val - target)
            if cur <= mn:
                v = min(v, node.val) if cur == mn else node.val
                mn = cur

            f(node.left)
            f(node.right)

        f(root)

        return v
