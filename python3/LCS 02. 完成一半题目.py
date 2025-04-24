class Solution:

    def halfQuestions(self, questions: List[int]) -> int:

        vs = sorted(Counter(questions).values(), reverse=True)
        ans = 0
        cnt = len(questions) // 2
        idx = 0
        while cnt > 0:
            cnt -= vs[idx]
            ans += 1
            idx += 1

        return ans
