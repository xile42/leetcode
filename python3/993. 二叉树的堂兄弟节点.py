# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:

        ps = set()
        ds = set()

        def f(node, par, depth):

            if node is None:
                return

            if node.val in [x, y]:
                ps.add(par)
                ds.add(depth)

            f(node.left, node.val, depth + 1)
            f(node.right, node.val, depth + 1)

        f(root, inf, 0)

        return len(ps) == 2 and len(ds) == 1
