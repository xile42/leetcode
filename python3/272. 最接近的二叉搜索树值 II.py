class Solution:

    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:

        diff = []

        def dfs(node):

            if node == None:
                return
            u = node.val

            t = abs(u - target)
            if len(diff) == k:
                if -diff[0][0] > t:
                    heappop(diff)
                    heappush(diff, [-t, node.val])
            else:
                heappush(diff, [-t, node.val])

            dfs(node.left)
            dfs(node.right)
            return

        dfs(root)

        return [x[1] for x in diff]