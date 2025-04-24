class Solution:

    def pairSums(self, nums: List[int], target: int) -> List[List[int]]:

        cnt = Counter()
        ans = list()
        for x in nums:
            if cnt[target - x]:
                ans += [[target - x, x]]
                cnt[target - x] -= 1
            else:
                cnt[x] += 1

        return ans
