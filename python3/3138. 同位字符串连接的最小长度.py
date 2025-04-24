class Solution:

    def minAnagramLength(self, s: str) -> int:

        n = len(s)
        d = dict()
        d[-1] = Counter()

        cnt = Counter()
        for idx, char in enumerate(s):
            cnt[char] += 1
            d[idx] = cnt.copy()

        for t in range(1, n // 2 + 1):
            if n % t == 0:
                c = d[t - 1]
                i = 1
                success = True
                while t * i < n:
                    if d[t * (i + 1) - 1] - d[t * i - 1] != c:
                        success = False
                        break
                    i += 1
                if success:
                    return t

        return n
