# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:

        ans = 0

        def f(node):

            if node is None:
                return 0, 0

            nonlocal ans
            left_v, left_cnt = f(node.left)
            right_v, right_cnt = f(node.right)
            cur_v, cur_cnt = left_v + right_v + node.val, left_cnt + right_cnt + 1
            ans = max(ans, cur_v / cur_cnt)

            return cur_v, cur_cnt

        f(root)

        return ans
