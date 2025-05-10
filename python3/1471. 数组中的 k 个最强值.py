class Solution:

    def getStrongest(self, arr: List[int], k: int) -> List[int]:

        ans = list()
        arr.sort()
        m = arr[(len(arr) - 1) // 2]
        left = 0
        right = len(arr) - 1
        while left <= right and len(ans) < k:
            if abs(arr[left] - m) > abs(arr[right] - m):
                ans.append(arr[left])
                left += 1
            else:
                ans.append(arr[right])
                right -= 1

        return ans
