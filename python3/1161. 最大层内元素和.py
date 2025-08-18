# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def maxLevelSum(self, root: Optional[TreeNode]) -> int:

        cnt = Counter()

        def f(node, depth):

            if node is None:
                return

            cnt[depth] += node.val
            f(node.left, depth + 1)
            f(node.right, depth + 1)

        f(root, 1)

        tar = max(cnt.values())
        for i in range(1, len(cnt) + 1):
            if cnt[i] == tar:
                return i
