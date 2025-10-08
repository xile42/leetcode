class Solution:

    def subsequenceSumAfterCapping(self, nums: List[int], k: int) -> List[bool]:

        n = len(nums)
        cnt = Counter(nums)
        acc = [0] * (n + 2)
        for i in range(n, 0, -1):
            acc[i] = acc[i + 1] + cnt[i]

        mask = 1
        ans = [False] * n

        for x in range(1, n + 1):
            for t in range(0, min(acc[x], k // x) + 1):
                left = k - t * x
                if left < 0:
                    break
                if mask & (1 << left):
                    ans[x - 1] = True
                    break

            if x > k:
                continue
            if cnt[x] == 0:
                continue

            c = cnt[x]
            groups = list()
            base = 1
            while c >= base:
                groups.append(base)
                c -= base
                base <<= 1
            if c > 0:
                groups.append(c)

            for g in groups:
                v = g * x
                if v > k:
                    continue
                new_mask = mask << v
                new_mask &= (1 << (k + 1)) - 1
                mask |= new_mask

        return ans
