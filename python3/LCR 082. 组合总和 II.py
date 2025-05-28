class Solution:

    results = set()

    def search(self, nums, begin, used, target):

        for idx in range(begin, len(nums)):

            num = nums[idx]
            if idx > begin and nums[idx] == nums[idx-1]:
                continue
            if num == target:
                self.results.add(tuple(used+[num]))
                return
            elif num < target:
                self.search(nums, idx+1, used+[num], target-num)
            else:
                return

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        self.results = set()
        sorted_candidates = sorted(candidates)
        self.search(sorted_candidates, 0, list(), target)

        return sorted(list(self.results))
