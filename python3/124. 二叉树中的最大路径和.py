# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        ans = -inf

        def f(node):

            nonlocal ans
            if node is None:
                return 0

            left_value = f(node.left)
            right_value = f(node.right)

            ans = max(ans, left_value + right_value + node.val)

            return max(max(left_value, right_value) + node.val, 0)

        f(root)

        return ans
