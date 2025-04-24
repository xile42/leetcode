class Solution:

    def validMountainArray(self, arr: List[int]) -> bool:

        if len(arr) <= 2:
            return False

        mid = arr.index(max(arr[1:-1]))

        return all(arr[i] - arr[i + 1] < 0 for i in range(mid)) and all(arr[i] - arr[i + 1] > 0 for i in range(mid, len(arr) - 1))
