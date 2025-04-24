# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def findMode(self, root: Optional[TreeNode]) -> List[int]:

        ns = list()

        def f(node):

            nonlocal ns

            if node is None:
                return

            ns.append(node.val)

            f(node.left)
            f(node.right)

        f(root)

        c = Counter(ns)
        mx = max(c.values())
        ans = list()
        for k, v in c.items():
            if v == mx:
                ans.append(k)

        return ans
            
