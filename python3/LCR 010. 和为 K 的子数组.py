class Solution:

    def subarraySum(self, nums: List[int], k: int) -> int:

        ans = s = 0
        cnt = defaultdict(int)
        cnt[0] = 1
        for x in nums:
            s += x
            ans += cnt[s-k]
            cnt[s] += 1

        return ans
