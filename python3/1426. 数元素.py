class Solution:

    def countElements(self, arr: List[int]) -> int:

        s = set(arr)
        ans = 0
        for n in arr:
            ans += ((n + 1) in s)

        return ans
