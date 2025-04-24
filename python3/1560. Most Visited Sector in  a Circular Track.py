class Solution:

    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:

        nums = list(range(1, n+1))
        nums = nums[rounds[0]-1:] + nums[:rounds[0]-1]
        results = list()
        for idx, value in enumerate(nums):
            results.append(value)
            if value == rounds[-1]:
                break

        return sorted(results)
