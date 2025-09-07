class Solution:

    def partitionArray(self, nums: List[int], k: int) -> bool:

        n = len(nums)

        if n % k != 0:
            return False

        group_cnt = n // k
        c = Counter(nums)

        if max(c.values()) <= group_cnt:
            return True

        return False
