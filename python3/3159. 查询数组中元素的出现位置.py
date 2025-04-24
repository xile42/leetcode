class Solution:

    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:

        idxs = [i for i, n in enumerate(nums) if n == x]

        ans = list()
        for q in queries:
            ans.append(-1 if q > len(idxs) else idxs[q - 1])

        return ans
