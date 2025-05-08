# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        c = Counter()

        def f(node, d):

            if node is None:
                return

            nonlocal c
            if node.left is None and node.right is None:
                c[d] += 1
                return

            f(node.left, d + 1)
            f(node.right, d + 1)

        f(root, 1)
        mx = max(c.keys())
        ans = None

        def ff(node, d):

            nonlocal ans
            if node is None:
                return 0

            if node.left is None and node.right is None and d == mx:
                if c[mx] == 1:
                    ans = node
                return 1

            v = ff(node.left, d + 1) + ff(node.right, d + 1)
            if v == c[mx] and ans is None:
                ans = node

            return v

        ff(root, 1)

        return root if ans is None else ans
