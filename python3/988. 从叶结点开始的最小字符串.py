# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:

        ans = None

        def f(node, cur):

            nonlocal ans

            if node is None:
                return

            cur += chr(ord("a") + node.val)

            if node.left is None and node.right is None:
                if ans is None or ans > cur[::-1]:
                    ans = cur[::-1]

            f(node.left, cur)
            f(node.right, cur)

        f(root, str())

        return ans
