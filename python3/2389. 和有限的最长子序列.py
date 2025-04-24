class Solution:

    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:

        acc = list(accumulate(sorted(nums)))

        return [bisect_right(acc, i) for i in queries]
