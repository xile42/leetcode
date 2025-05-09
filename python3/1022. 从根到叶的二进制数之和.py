# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:

        ans = 0

        def f(node, s):

            if node is None:
                return

            nonlocal ans
            s += str(node.val)
            if node.left is None and node.right is None:
                ans += int(s, 2)

            f(node.left, s)
            f(node.right, s)

        f(root, str())

        return ans
