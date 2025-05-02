class Solution:

    def minOperations(self, nums: List[int], k: int) -> int:

        sn = sorted(set(nums))

        if len(sn) == 1:
            if sn[0] < k:
                return -1
            elif sn[0] == k:
                return 0
            else:
                return 1

        if not k <= sn[0]:
            return -1

        if k == sn[0]:
            return len(sn) - 1
        else:
            return len(sn)


