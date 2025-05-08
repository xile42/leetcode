# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        if root is None:
            return TreeNode(val=val)

        def f(node):

            v = node.val
            if v > val:
                if node.left is None:
                    node.left = TreeNode(val=val)
                    return
                else:
                    f(node.left)
            else:
                if node.right is None:
                    node.right = TreeNode(val=val)
                    return
                else:
                    f(node.right)

        f(root)

        return root
