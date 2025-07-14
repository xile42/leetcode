class Solution:

    def predictPartyVictory(self, senate: str) -> str:

        cnt_r = cnt_d = 0
        deny_r = deny_d = 0
        invalid = set()

        while True:
            for i, c in enumerate(senate):
                if i in invalid:
                    continue
                if c == "R":
                    if deny_r > 0:
                        deny_r -= 1
                        invalid.add(i)
                    else:
                        cnt_r += 1
                        deny_d += 1
                else:
                    if deny_d > 0:
                        deny_d -= 1
                        invalid.add(i)
                    else:
                        cnt_d += 1
                        deny_r += 1
            if cnt_r > 0 and cnt_d == 0:
                return "Radiant"
            elif cnt_r == 0 and cnt_d > 0:
                return "Dire"
            cnt_r = cnt_d = 0
