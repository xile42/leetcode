class Solution:

    def minArrivalsToDiscard(self, arrivals: List[int], w: int, m: int) -> int:

        n = len(arrivals)
        cnt = Counter()
        ans = 0
        left = 0
        valid = [True] * n
        for right in range(n):
            cnt[arrivals[right]] += 1
            if right - left + 1 > w:
                if valid[left]:
                    cnt[arrivals[left]] -= 1
                left += 1
            if cnt[arrivals[right]] > m:
                ans += 1
                valid[right] = False
                cnt[arrivals[right]] -= 1

        return ans
