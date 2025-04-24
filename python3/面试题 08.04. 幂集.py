class Solution:

    result = None

    def search(self, candidates, current):

        self.result.append(current)

        for idx, num in enumerate(candidates):
            self.search(candidates[idx+1:], current+[num])

    def subsets(self, nums: List[int]) -> List[List[int]]:

        self.result = list()
        self.search(nums, list())

        return self.result