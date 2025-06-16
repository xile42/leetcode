class Solution:

    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:

        if p == q:
            return 0

        d = dict()
        ans = None

        def f(node, depth):

            nonlocal ans
            if ans or node is None:
                return 0

            v = node.val
            d[v] = depth
            left = f(node.left, depth + 1)
            right = f(node.right, depth + 1)
            cur = 1 if v == p or v == q else 0
            if cur + left + right == 2 and not ans:
                ans = d[p] + d[q] - 2 * depth

            return cur + left + right

        f(root, 1)

        return ans
