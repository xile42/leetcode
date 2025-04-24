class Solution:

    def replaceElements(self, arr: List[int]) -> List[int]:

        n = len(arr)
        suf = [0] * n
        suf[-1] = arr[-1]
        for i in range(n - 2, -1, -1):
            suf[i] = max(arr[i], suf[i + 1])

        ans = list()
        for i, _ in enumerate(arr):
            ans.append(-1 if i == n - 1 else suf[i + 1])

        return ans