# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:

        c = Counter()

        def f(node, depth):

            if node is None:
                return

            c[depth] += node.val
            f(node.left, depth + 1)
            f(node.right, depth + 1)

        f(root, 1)

        vs = sorted(c.values(), reverse=True)

        return vs[k - 1] if k <= len(vs) else -1
