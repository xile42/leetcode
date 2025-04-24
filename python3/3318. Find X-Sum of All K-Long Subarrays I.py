class Solution:

    def x_sum(self, nums, x):
        # print(nums)
        counter = Counter(nums)
        values = [[v, k] for k, v in counter.items()]
        values = sorted(values, reverse=True)
        # print(values)
        return sum([i[0] * i[1] for i in values][:x])

    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:

        results = list()
        for i in range(len(nums) - k + 1):
            results.append(self.x_sum(nums[i:i+k], x))

        return results
