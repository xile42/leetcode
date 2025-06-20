class Solution:

    def maximumNumber(self, num: str, change: List[int]) -> str:

        for i, c in enumerate(num):
            d = int(c)
            if change[d] > d:
                start = i
                break
        else:
            return num

        ans = list(num)
        for i in range(start, len(ans)):
            c = num[i]
            d = int(c)
            if change[d] >= d:
                ans[i] = str(change[d])
            else:
                break

        return "".join(ans)
