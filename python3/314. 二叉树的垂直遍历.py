class Solution:

    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        nodes = defaultdict(list)

        q = deque([(root, 0)])

        while q:

            i, pos = q.popleft()

            if i is None:
                continue

            nodes[pos].append(i.val)
            q.append((i.left, pos - 1))
            q.append((i.right, pos + 1))

        ans = list()
        for k in sorted(nodes.keys()):
            ans.append(nodes[k])

        return ans
