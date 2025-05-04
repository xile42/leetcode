# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        vs = defaultdict(list)

        def f(node, d):

            if node is None:
                return

            vs[d].append(node.val)

            f(node.left, d + 1)
            f(node.right, d + 1)

        f(root, 0)

        return [sum(vs[k]) / len(vs[k]) for k in sorted(vs.keys())]
