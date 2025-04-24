class Solution:

    def beautifulSubarrays(self, nums: List[int]) -> int:

        acc = list()
        acc.append(nums[0])
        for n in nums[1:]:
            acc.append(acc[-1] ^ n)

        cnt = Counter()
        cnt[0] += 1
        ans = 0
        for v in acc:
            ans += cnt[v]
            cnt[v] += 1

        return ans
