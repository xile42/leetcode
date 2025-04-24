# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def convertBiNode(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        d = defaultdict(list)

        def f(node):

            if node is None:
                return

            d[node.val].append(node)
            f(node.left)
            f(node.right)

        if root is None:
            return None

        f(root)
        ks = sorted(d.keys())
        vs = [d[k] for k in ks]
        head = TreeNode()
        cur = head
        for v_list in vs:
            for v in v_list:
                v.left = None
                v.right = None
                cur.right = v
                cur = cur.right

        return head.right
