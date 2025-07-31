class Solution:

    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:

        ans = 0

        def check(i, j):

            pos_i = fruits[i][0]
            pos_j = fruits[j][0]
            dis = pos_j - pos_i + min(abs(pos_i - startPos), abs(pos_j - startPos))

            return dis <= k

        cur = left = 0
        for right, (pos, value) in enumerate(fruits):
            cur += value
            while left <= right and not check(left, right):
                cur -= fruits[left][1]
                left += 1
            ans = max(ans, cur)

        return ans
