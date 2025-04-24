class Solution:

    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:

        result = 0
        n = len(arr)
        for idx in range(n):
            for jdx in range(idx+1, n):
                for kdx in range(jdx+1, n):
                    if abs(arr[idx] - arr[jdx]) <= a and abs(arr[jdx] - arr[kdx]) <= b and abs(arr[idx] - arr[kdx]) <= c:
                        result += 1

        return result
