class Solution:

    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:

        for i in range(len(arr) - k * m + 1):
            s = arr[i:i + m]
            if s * k == arr[i:i + k * m]:
                return True

        return False
