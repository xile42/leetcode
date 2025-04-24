# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:

        cnt1 = Counter()
        cnt2 = Counter()

        def f(node, n):

            nonlocal cnt1, cnt2
            cnt = cnt1 if n == 1 else cnt2

            if node is None:
                return

            cnt[node.val] += 1
            f(node.left, n)
            f(node.right, n)

        f(root1, 1)
        f(root2, 2)

        for k, v in cnt1.items():
            if cnt2[target - k]:
                return True

        return False
