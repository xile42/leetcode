# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        ans = None

        def f(node):

            if node is None:
                return 0

            found = 0
            if node in [p, q]:
                found = 1
            found += f(node.left)
            found += f(node.right)

            nonlocal ans
            if found == 2 and ans is None:
                ans = node

            return found

        f(root)

        return ans
