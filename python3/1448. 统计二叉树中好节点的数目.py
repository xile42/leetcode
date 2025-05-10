# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def goodNodes(self, root: Optional[TreeNode]) -> int:

        ans = 0

        def f(node, cur):

            nonlocal ans

            if node is None:
                return

            if node.val >= cur:
                ans += 1

            f(node.left, max(cur, node.val))
            f(node.right, max(cur, node.val))

        f(root, -inf)

        return ans
