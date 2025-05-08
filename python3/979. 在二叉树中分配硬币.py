# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def distributeCoins(self, root: Optional[TreeNode]) -> int:

        ans = 0

        def dfs(node):

            if not node:
                return 0, 0

            nonlocal ans
            val = node.val
            cnt = 1
            left_val, left_cnt = dfs(node.left)
            right_val, right_cnt = dfs(node.right)
            val = val + left_val + right_val
            cnt = cnt + left_cnt + right_cnt
            ans += abs(cnt - val)

            return val, cnt

        dfs(root)

        return ans
