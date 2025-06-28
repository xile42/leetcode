# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def checkEqualTree(self, root: Optional[TreeNode]) -> bool:

        total = 0

        def f(node):

            if node is None:
                return

            nonlocal total
            total += node.val
            f(node.left)
            f(node.right)

        f(root)

        ans = False

        def g(node):

            if node is None:
                return 0

            left = g(node.left)
            right = g(node.right)
            cur = node.val + left + right

            nonlocal ans
            if cur == total - cur and node != root:
                ans = True

            return cur

        g(root)

        return ans
