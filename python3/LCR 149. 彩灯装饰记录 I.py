# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def decorateRecord(self, root: Optional[TreeNode]) -> List[int]:

        ans = list()
        q = list()
        if root is None:
            return list()
        q.append(root)
        while q:
            cur = q.pop(0)
            ans.append(cur.val)
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)

        return ans
