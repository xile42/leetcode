class Solution:

    def findKOr(self, nums: List[int], k: int) -> int:

        cnt = Counter()
        for n in nums:
            idx = 0
            cur = n
            while cur > 0:
                if cur & 1:
                    cnt[idx] += 1
                idx += 1
                cur >>= 1

        if not cnt:
            return 0
        s = str()
        for key in range(max(cnt.keys()) + 1):
            s += "1" if cnt[key] >= k else "0"

        return int(s[::-1], 2)
