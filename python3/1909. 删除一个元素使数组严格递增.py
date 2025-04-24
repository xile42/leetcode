class Solution:

    def canBeIncreasing(self, nums: List[int]) -> bool:

        to_delete = set()
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                to_delete.add(i)
                to_delete.add(i - 1)

        def check(ns):
            return all(ns[i] - ns[i - 1] > 0 for i in range(1, len(ns)))

        if len(to_delete) == 0:
            return True
        elif len(to_delete) > 2:
            return False
        else:
            a, b = list(to_delete)
            return check(nums[:a] + nums[a + 1:]) or check(nums[:b] + nums[b + 1:])
