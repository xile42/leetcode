class Solution:

    def checkEqualPartitions(self, nums: List[int], target: int) -> bool:

        prod = reduce(mul, nums)
        if prod != target * target:
            return False

        success = False

        def f(i, cur):

            nonlocal success

            if cur == target:
                success = True
                return

            if i >= len(nums) or success:
                return

            f(i + 1, cur * nums[i])
            f(i + 1, cur)

        f(0, 1)

        return success
