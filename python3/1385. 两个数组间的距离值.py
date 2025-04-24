class Solution:

    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:

        ans = 0
        arr2.sort()
        for n in arr1:
            idx = bisect_left(arr2, n)
            dis = inf
            if idx > 0:
                dis = min(dis, abs(arr2[idx - 1] - n))
            if idx < len(arr2):
                dis = min(dis, abs(arr2[idx] - n))
            if dis > d:
                ans += 1

        return ans
