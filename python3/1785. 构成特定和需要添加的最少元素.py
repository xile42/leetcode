class Solution:

    def minElements(self, nums: List[int], limit: int, goal: int) -> int:

        tar = abs(goal - sum(nums))

        return ceil(tar / limit)
