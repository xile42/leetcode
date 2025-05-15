class Solution:

    def runeReserve(self, runes: List[int]) -> int:

        ans = 0
        runes.sort()
        pre = runes[0]
        cnt = 1
        for n in runes[1:]:
            if n - pre <= 1:
                cnt += 1
                pre = n
            else:
                ans = max(ans, cnt)
                cnt = 1
                pre = n
        ans = max(ans, cnt)

        return ans
