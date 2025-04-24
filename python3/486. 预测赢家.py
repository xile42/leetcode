class Solution:

    def predictTheWinner(self, nums: List[int]) -> bool:

        def f(start, end, flag):

            if start == end:
                return flag * nums[start]

            else:
                score1 = flag * nums[start] + f(start + 1, end, -flag)
                score2 = flag * nums[end] + f(start, end - 1, -flag)

            return max(score1 * flag, score2 * flag) * flag
        
        return f(0, len(nums) - 1, 1) >= 0
