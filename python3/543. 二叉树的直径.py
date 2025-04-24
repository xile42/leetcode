# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        ans = 0

        def f(node):

            nonlocal ans
            if node is None:
                return -1

            left = f(node.left)
            right = f(node.right)
            ans = max(ans, left + right + 2)

            return max(left, right) + 1

        f(root)

        return ans
