class Solution:

    def earliestAcq(self, logs: List[List[int]], n: int) -> int:

        ns = list(range(n))

        def find_p(v):

            cur = v
            while cur != ns[cur]:
                cur = ns[cur]

            return cur

        def merge(i, j):

            pi = find_p(i)
            pj = find_p(j)
            if pi != pj:
                ns[pi] = pj
                return True
            else:
                return False

        logs.sort(key=lambda x: x[0])
        cnt = 0
        for t, i, j in logs:
            if merge(i, j):
                cnt += 1
            if cnt == n - 1:
                return t

        return -1
