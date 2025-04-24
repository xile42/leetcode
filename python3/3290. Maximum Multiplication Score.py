class Solution:
    def maxScore(self, a: List[int], b: List[int]) -> int:

        max_scores = [float('-inf')] * 4
        for num in b:
            for i in range(3, -1, -1):
                if i > 0:
                    max_scores[i] = max(max_scores[i], max_scores[i - 1] + a[i] * num)
                else:
                    max_scores[i] = max(max_scores[i], a[i] * num)

        return max_scores[-1]
