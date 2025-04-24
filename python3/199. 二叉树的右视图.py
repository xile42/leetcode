# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        ans = list()
        q = list()
        if root:
            q.append(root)
        while q:
            ans.append(q[-1].val)
            next_q = list()
            for node in q:
                if node.left:
                    next_q.append(node.left)
                if node.right:
                    next_q.append(node.right)
            q = next_q

        return ans
