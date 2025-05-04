# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:

        c = Counter()

        def f(node):

            if node is None:
                return 0

            nonlocal c
            v = node.val + f(node.left) + f(node.right)
            c[v] += 1

            return v

        f(root)

        return [k for k in c if c[k] == max(c.values())]
