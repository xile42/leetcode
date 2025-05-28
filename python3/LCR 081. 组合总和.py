class Solution:

    results = set()

    def search(self, nums, used, target):

        for num in nums:
            if num == target:
                self.results.add(tuple(sorted(used + [num])))
                return
            elif num > target:
                return
            else:
                self.search(nums, used+[num], target-num)

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        self.results = set()
        self.search(sorted(candidates), list(), target)

        return list(self.results)
