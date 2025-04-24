class Solution:

    def findMatrix(self, nums: List[int]) -> List[List[int]]:

        from collections import Counter

        counter = Counter(nums)
        value_max = max(list(counter.values()))
        results = list()

        for current_value in range(value_max, 0, -1):

            this_result = list()
            for key, value in counter.items():
                if value == current_value:
                    this_result.append(key)
                    counter[key] -= 1

            results.append(this_result)

        return results
