class Solution:

    def numRabbits(self, answers: List[int]) -> int:

        c = Counter(answers)
        ans = 0
        for k, v in c.items():
            ans += ceil(v / (k + 1)) * (k + 1)

        return ans
