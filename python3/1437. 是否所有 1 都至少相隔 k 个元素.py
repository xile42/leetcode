class Solution:

    def kLengthApart(self, nums: List[int], k: int) -> bool:

        idxs = [i for i in range(len(nums)) if nums[i] == 1]
        diffs = [b - a - 1 for a, b in pairwise(idxs)]

        return all(i >= k for i in diffs)
