# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:

        h = list()
        s = set()

        def f(node):

            if node is None:
                return

            if node.val not in s:
                heappush(h, -node.val)
                if len(h) > 2:
                    heappop(h)
                s.add(node.val)

            f(node.left)
            f(node.right)

        f(root)

        return -1 if len(h) < 2 else -h[0]
