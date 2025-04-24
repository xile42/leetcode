# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def countPairs(self, root: Optional[TreeNode], distance: int) -> int:

        ans = 0

        def f(node, d):

            if node is None:
                return []

            if node.left is None and node.right is None:
                return [d]

            nonlocal ans
            left = f(node.left, d + 1)
            right = f(node.right, d + 1)

            for v1 in left:
                for v2 in right:
                    if v1 + v2 - 2 * d <= distance:
                        ans += 1

            return left + right

        f(root, 1)

        return ans
