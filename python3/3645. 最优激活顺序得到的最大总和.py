class Solution:

    def maxTotal(self, value: List[int], limit: List[int]) -> int:

        vl = sorted(zip(value, limit), key=lambda x: [x[1], -x[0]])
        n = len(vl)
        q = deque()

        ans = 0
        idx = 0
        while idx < n and len(q) < vl[idx][1]:
            v, l = vl[idx]
            ans += v
            q.append(l)
            idx += 1

            cur_x = len(q)
            while idx < n and cur_x >= vl[idx][1]:
                idx += 1
            while q and q[0] <= cur_x:
                q.popleft()

        return ans
