# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def equalToDescendants(self, root: Optional[TreeNode]) -> int:

        ans = 0

        def f(node):

            nonlocal ans
            if node is None:
                return 0

            left = f(node.left)
            right = f(node.right)
            if left + right == node.val:
                ans += 1

            return left + right + node.val

        f(root)

        return ans
