class Solution:

    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:

        ans = list()
        cur = 0
        colors = [-1] * n

        for i, c in queries:
            pre_c = colors[i]
            if pre_c == c:
                ans.append(cur)
                continue
            if pre_c != -1:
                if i > 0 and colors[i - 1] == pre_c:
                    cur -= 1
                if i < n - 1 and colors[i + 1] == pre_c:
                    cur -= 1
            if i > 0 and colors[i - 1] == c:
                cur += 1
            if i < n - 1 and colors[i + 1] == c:
                cur += 1
            ans.append(cur)
            colors[i] = c

        return ans
