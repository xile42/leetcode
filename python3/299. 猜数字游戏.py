class Solution:

    def getHint(self, secret: str, guess: str) -> str:

        ans1 = sum(secret[i] == guess[i] for i in range(len(guess)))
        ans2 = 0
        c1, c2 = Counter(secret), Counter(guess)
        for k in c1.keys() | c2.keys():
            ans2 += min(c1[k], c2[k])
        ans2 -= ans1

        return "{}A{}B".format(ans1, ans2)
