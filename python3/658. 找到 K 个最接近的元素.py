class Solution:

    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        i = bisect_left(arr, x)
        left = arr[max(i - k, 0):i][::-1]
        right = arr[i: i + k]
        ans_left = list()
        ans_right = list()
        for _ in range(k):
            left_value = inf if not left else abs(left[0] - x)
            right_value = inf if not right else abs(right[0] - x)
            if left_value <= right_value:
                ans_left.append(left.pop(0))
            else:
                ans_right.append(right.pop(0))

        return ans_left[::-1] + ans_right
