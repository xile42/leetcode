class Solution:

    def maxTurbulenceSize(self, arr: List[int]) -> int:

        ns = [1 if arr[i] < arr[i - 1] else (-1 if arr[i] > arr[i - 1] else 0) for i in range(1, len(arr))]
        ans = 0
        pre = None
        cnt = 0
        for v in ns:
            if v and (pre is None or v + pre == 0):
                pre = v
                cnt += 1
            else:
                ans = max(ans, cnt + 1)
                pre = None if v == 0 else v
                cnt = 1 if pre else 0
        ans = max(ans, cnt + 1)

        return ans
