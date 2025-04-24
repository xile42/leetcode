# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:

        ans = 0

        def f(node, cnt):

            nonlocal ans

            if node is None:
                return

            cnt[node.val] += 1

            if node.left is None and node.right is None:
                if sum(v & 1 for v in cnt.values()) <= 1:
                    ans += 1
                return

            f(node.left, cnt.copy())
            f(node.right, cnt.copy())

        f(root, Counter())

        return ans
