# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if root is None:
            return list()

        ans = list()

        q = list()
        q.append(root)
        while q:
            vs = [node.val for node in q if node is not None]
            if vs:
                ans.append(vs)
            next_q = list()
            for node in q:
                if node is None:
                    continue
                next_q.append(node.left)
                next_q.append(node.right)
            q = next_q

        return ans
        
