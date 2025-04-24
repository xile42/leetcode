# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def f(node):

            if node is None:
                return list()

            return f(node.left) + [node.val] + f(node.right)

        nodes = f(root)
        head = TreeNode(nodes[0])
        cur = head
        for v in nodes[1:]:
            cur.right = TreeNode(v)
            cur = cur.right

        return head
        
