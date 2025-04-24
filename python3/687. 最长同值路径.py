# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:

        ans = 0

        def f(node):

            if node is None:
                return Counter()

            if node.left is None and node.right is None:
                c = Counter()
                c[node.val] += 1
                return c

            nonlocal ans
            left = f(node.left)
            right = f(node.right)
            v = node.val
            ans = max(ans, left[v] + right[v])

            c = Counter()
            c[v] = max(left[v], right[v]) + 1
            return c

        f(root)

        return ans
