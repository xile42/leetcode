class Solution:

    def chalkReplacer(self, chalk: List[int], k: int) -> int:

        n = len(chalk)
        sum_chalk = sum(chalk)
        k = k % sum_chalk
        if k == 0:
            return 0

        prefix_sum = list()
        prefix_sum.append(chalk[0])
        for idx in range(1, n):
            prefix_sum.append(chalk[idx]+prefix_sum[-1])

        left, right = 0, n - 1
        while left <= right:
            mid = left + (right - left) // 2
            if prefix_sum[mid] == k:
                return (mid + 1) % n
            elif prefix_sum[mid] > k:
                right = mid - 1
            else:
                left = mid + 1

        return left % n
