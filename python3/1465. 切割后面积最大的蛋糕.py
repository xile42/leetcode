class Solution:

    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:

        horizontalCuts.sort()
        verticalCuts.sort()

        hs = list()
        for i, v in enumerate(horizontalCuts):
            if i == 0:
                hs.append(v)
            else:
                hs.append(v - horizontalCuts[i - 1])
        hs.append(h - horizontalCuts[-1])

        ws = list()
        for i, v in enumerate(verticalCuts):
            if i == 0:
                ws.append(v)
            else:
                ws.append(v - verticalCuts[i - 1])
        ws.append(w - verticalCuts[-1])

        return max(hs) * max(ws) % (10 ** 9 + 7)
