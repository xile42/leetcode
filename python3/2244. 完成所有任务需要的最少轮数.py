class Solution:

    def minimumRounds(self, tasks: List[int]) -> int:

        ans = 0
        for _, v in Counter(tasks).items():
            if v == 1:
                return -1
            while v >= 1:
                ans += 1
                v -= 3

        return ans
