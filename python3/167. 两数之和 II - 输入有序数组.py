class Solution:

    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        left = 0
        right = len(numbers) - 1
        while left < right:
            v = numbers[left] + numbers[right]
            if v == target:
                return [left + 1, right + 1]
            elif v > target:
                right -= 1
            else:
                left += 1
