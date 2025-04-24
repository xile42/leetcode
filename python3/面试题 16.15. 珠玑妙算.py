class Solution:

    def masterMind(self, solution: str, guess: str) -> List[int]:

        ans1 = sum(solution[i] == guess[i] for i in range(len(guess)))
        ans2 = 0
        c1, c2 = Counter(solution), Counter(guess)
        for k in "R", "Y", "G", "B":
            ans2 += min(c1[k], c2[k])
        ans2 -= ans1

        return [ans1, ans2]
