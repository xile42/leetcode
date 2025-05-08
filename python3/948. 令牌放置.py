class Solution:

    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:

        n = len(tokens)
        tokens.sort()
        curp = power
        curs = 0
        ans = 0
        l, r = 0, n - 1
        while l <= r:
            lv = tokens[l]
            if lv <= curp:
                curp -= lv
                l += 1
                curs += 1
                ans = max(ans, curs)
            elif curs:
                curs -= 1
                curp += tokens[r]
                r -= 1
            else:
                break

        return ans
