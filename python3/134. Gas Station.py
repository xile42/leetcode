class Solution:

    def check(self, nums):

        value = 0
        for i in nums:
            value += i
            if value < 0:
                return False

        return True

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        raw = [gas[idx] - cost[idx] for idx in range(len(gas))]
        if sum(raw) < 0:
            return -1

        nums = list()
        left_idx = list()
        for idx, num in enumerate(raw):
            if num == 0:
                continue
            if len(nums) == 0:
                nums.append(num)
                left_idx.append(idx)
            elif nums[-1] * num > 0:
                nums[-1] += num
            else:
                nums.append(num)
                left_idx.append(idx)

        if len(nums) == 0:
            return 0

        for idx in range(len(nums)):
            if nums[idx] > 0 and self.check(nums[idx:] + nums[:idx]):
                return left_idx[idx]

        return -1
