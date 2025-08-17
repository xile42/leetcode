class Solution:

    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:

        edges_cnt = 0
        in_degrees = [0] * n
        out_degrees = [0] * n

        for u, v in enumerate(leftChild):
            if v == -1:
                continue
            edges_cnt += 1
            in_degrees[v] += 1
            out_degrees[u] += 1

        for u, v in enumerate(rightChild):
            if v == -1:
                continue
            edges_cnt += 1
            in_degrees[v] += 1
            out_degrees[u] += 1

        if edges_cnt != n - 1:
            return False

        c = Counter(in_degrees)
        if c[0] != 1 or c[1] != n - 1:
            return False

        if any(v > 2 for v in out_degrees):
            return False

        vis = [False] * n
        queue = deque()
        for i in range(n):
            if in_degrees[i] == 0:
                queue.append(i)
        while queue:
            u = queue.popleft()
            vis[u] = True
            for v in (leftChild[u], rightChild[u]):
                if v == -1:
                    continue
                if not vis[v]:
                    queue.append(v)

        if not all(vis):
            return False

        return True
