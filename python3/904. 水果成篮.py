class Solution:

    def totalFruit(self, fruits: List[int]) -> int:

        cnt = Counter()
        ans = left = 0
        for right, n in enumerate(fruits):
            cnt[n] += 1
            while len(cnt) > 2:
                cnt[fruits[left]] -= 1
                if cnt[fruits[left]] == 0:
                    del cnt[fruits[left]]
                left += 1
            ans = max(ans, right - left + 1)

        return ans
