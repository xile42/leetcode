class Solution:

    def checkSubarraySum(self, nums: List[int], k: int) -> bool:

        acc = list(accumulate(nums))
        cnt = Counter()
        cnt[0] += 1
        last_update = None
        for i, n in enumerate(acc):
            if cnt[n % k] and i > 0:
                return True
            if last_update is not None:
                cnt[last_update] += 1
            last_update = n % k

        return False
