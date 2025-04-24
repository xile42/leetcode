class Solution:

    def getSneakyNumbers(self, nums: List[int]) -> List[int]:

        from collections import Counter

        results = list()
        counter = Counter(nums)
        for k, v in counter.items():
            if v > 1:
                results.append(k)
                if len(results) == 2:
                    break

        return results
