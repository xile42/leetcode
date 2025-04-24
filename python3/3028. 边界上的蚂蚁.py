class Solution:

    def returnToBoundaryCount(self, nums: List[int]) -> int:

        acc = list(accumulate(nums))

        return Counter(acc)[0]
