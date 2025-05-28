class Solution:

    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:

        cnt_sub = Counter()

        def f(k):

            nonlocal cnt_sub
            ans = 0
            cnt = Counter()
            for i, n in enumerate(s):
                cnt[n] += 1
                if i >= k:
                    cnt[s[i - k]] -= 1
                    if cnt[s[i - k]] == 0:
                        del cnt[s[i - k]]
                if i >= k - 1 and len(cnt) <= maxLetters:
                    cnt_sub[s[i - k + 1:i + 1]] += 1

            return ans

        [f(i) for i in range(minSize, maxSize + 1)]

        return 0 if not cnt_sub else max(cnt_sub.values())
