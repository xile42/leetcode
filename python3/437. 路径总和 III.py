# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        c = Counter()
        c[0] = 1
        ans = 0

        def f(node, cur):

            nonlocal c, ans
            if node is None:
                return

            v = node.val
            tar = (v if cur is None else cur + v) - targetSum
            ans += c[tar]

            c[v if cur is None else cur + v] += 1
            f(node.left, cur + v if cur is not None else v)
            f(node.right, cur + v if cur is not None else v)
            c[v if cur is None else cur + v] -= 1

        f(root, None)

        return ans
