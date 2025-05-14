class Solution:

    def maximumLength(self, s: str) -> int:

        c = Counter(s)
        if all(v < 3 for v in c.values()):
            return -1

        def check(x):

            cnt = Counter()
            for c, ite in groupby(s):
                l = len(list(ite))
                if l >= x:
                    cnt[c] += l - x + 1

            return any(v >= 3 for v in cnt.values())

        left = 1
        right = len(s)
        while left <= right:
            mid = left + (right - left) // 2
            if check(mid):
                left = mid + 1
            else:
                right = mid - 1

        return right
