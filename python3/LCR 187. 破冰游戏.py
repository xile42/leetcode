class Solution:

    def iceBreakingGame(self, num: int, target: int) -> int:

        cur = 0
        guys = list(range(num))
        for i in range(num-1):
            kill = (cur + target - 1) % (num - i)
            guys.pop(kill)
            cur = 0 if kill == len(guys) else kill

        return guys[0]
