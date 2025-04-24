class Solution:

    def numOfSubarrays(self, arr: List[int]) -> int:

        s = 0
        ans = 0
        cnt = Counter()
        cnt[0] += 1
        base = 10 ** 9 + 7
        for n in arr:
            s = (s + n) & 1
            ans = (ans + cnt[1 - s]) % base
            cnt[s] += 1

        return ans % base
