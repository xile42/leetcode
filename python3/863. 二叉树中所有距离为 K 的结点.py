# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:

    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:

        ans = list()
        g = defaultdict(list)
        vis = set()

        def dfs1(node):

            if not node:
                return
            if node.left:
                g[node.val].append(node.left.val)
                g[node.left.val].append(node.val)
                dfs1(node.left)
            if node.right:
                g[node.val].append(node.right.val)
                g[node.right.val].append(node.val)
                dfs1(node.right)

        dfs1(root)

        def dfs2(i, d):

            vis.add(i)
            if d == k:
                ans.append(i)
                return

            for j in g[i]:
                if j not in vis:
                    dfs2(j, d + 1)

        dfs2(target.val, 0)

        return ans
