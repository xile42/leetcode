class Solution:

    def shuffle(self, nums: List[int], n: int) -> List[int]:

        result = list()
        for idx in range(n):
            result.append(nums[idx])
            result.append(nums[n+idx])

        return result
