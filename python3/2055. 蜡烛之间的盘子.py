class Solution:

    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:

        n = len(s)
        left = [-1] * n
        right = [-1] * n
        acc = list(accumulate([1 if c == "*" else 0 for c in s]))
        cur = -1
        for i, c in enumerate(s):
            if c == "|":
                cur = i
            left[i] = cur
        cur = -1
        for i in range(n - 1, -1, -1):
            c = s[i]
            if c == "|":
                cur = i
            right[i] = cur

        ans = list()
        for l, r in queries:
            l = right[l] if right[l] <= r else -1
            r = left[r] if left[r] >= l else -1
            if l == -1 or r == -1:
                ans.append(0)
            else:
                ans.append(acc[r] - (0 if l == 0 else acc[l - 1]))

        return ans
